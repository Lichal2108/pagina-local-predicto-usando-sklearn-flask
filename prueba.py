import pandas as pd
import numpy as np
import joblib
import os
from sklearn.base import BaseEstimator, TransformerMixin
from flask import Flask, render_template, request, url_for, send_from_directory

# =============================================================================
# Definición de la clase usada durante el entrenamiento
# =============================================================================
class FeatureEngineeringTransformer(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        # Guardar los nombres de las columnas originales para usarlos en transform
        self.feature_names_ = list(X.columns) if isinstance(X, pd.DataFrame) else None
        return self

    def transform(self, X, y=None):
        if isinstance(X, pd.DataFrame):
            X = X.copy()
        else:
            # Si no se tiene feature_names_, usar nombres genéricos
            if hasattr(self, 'feature_names_') and self.feature_names_ is not None:
                X = pd.DataFrame(X, columns=pd.Index(self.feature_names_))
            else:
                X = pd.DataFrame(X)

        def safe_divide(a, b):
            return np.divide(a, b, out=np.zeros_like(a), where=b != 0)

        X['ratio_perimetro_area'] = safe_divide(X['perimetro_media'], X['area_media'])
        X['ratio_radio_area'] = safe_divide(X['radio_media'], X['area_media'])
        X['ratio_peor_media_area'] = safe_divide(X['peor_area'], X['area_media'])
        X['rel_error_area'] = safe_divide(X['error_estandar_area'], X['area_media'])
        X['rel_error_radio'] = safe_divide(X['error_estandar_radio'], X['radio_media'])

        X['dif_peor_media_area'] = X['peor_area'] - X['area_media']
        X['dif_peor_media_radio'] = X['peor_radio'] - X['radio_media']

        X['area_x_perimetro'] = X['area_media'] * X['perimetro_media']
        X['suavidad_x_simetria'] = X['suavidad_media'] * X['simetria_media']

        return X

# =============================================================================
# Cargar artefactos entrenados
# =============================================================================
try:
    renombrar_columnas = joblib.load('renombrar_columnas.pkl')
    columnas_a_eliminar = joblib.load('columnas_a_eliminar.pkl')
    target_encoder = joblib.load('target_encoder.pkl')
    feature_engineer = joblib.load('feature_engineering_transformer.pkl')
    imputer = joblib.load('imputer.pkl')
    selected_features = joblib.load('selected_features.pkl')
    modelo_final = joblib.load('final_model.pkl')

    print("✅ Artefactos cargados correctamente.")

    df_temp = pd.read_csv('breast_cancer_dataset_peru.csv', sep=';')
    df_temp = df_temp.rename(columns=renombrar_columnas)
    df_temp = df_temp.drop(columns=[col for col in columnas_a_eliminar if col in df_temp.columns])
    input_columns = [col for col in df_temp.columns if col != 'diagnostico']

except Exception as e:
    print(f"❌ Error al cargar artefactos: {e}")
    exit()

# =============================================================================
# Función de predicción
# =============================================================================
def predecir_diagnostico(input_dict):
    try:
        # Verificar que se hayan proporcionado todas las columnas necesarias
        missing = set(input_columns) - set(input_dict.keys())
        if missing:
            raise ValueError(f"Faltan columnas: {missing}")

        input_df = pd.DataFrame([input_dict], columns=pd.Index(input_columns))

        # Preprocesamiento
        X_transformed = feature_engineer.transform(input_df)
        if isinstance(X_transformed, np.ndarray):
            X_transformed = pd.DataFrame(X_transformed, columns=feature_engineer.feature_names_)

        X_imputed = imputer.transform(X_transformed)
        X_df = pd.DataFrame(X_imputed, columns=feature_engineer.feature_names_)

        X_df = X_df.replace([np.inf, -np.inf], 0).fillna(0)

        for col in selected_features:
            if col not in X_df:
                X_df[col] = 0
        X_final = X_df[selected_features]

        # Predicción
        pred = modelo_final.predict(X_final)[0]
        proba = modelo_final.predict_proba(X_final)[0]

        resultado = "Benigno" if pred == 0 else "Maligno"
        proba_dict = {
            "Benigno": proba[target_encoder['B']],
            "Maligno": proba[target_encoder['M']]
        }
        confianza = round(max(proba) * 100, 2)

        return {
            "diagnostico": resultado,
            "probabilidades": proba_dict,
            "confianza": f"{confianza}%"
        }

    except Exception as e:
        return {"error": str(e)}

# =============================
# FLASK WEB APP PARA PREDICCIÓN
# =============================
app = Flask(__name__)

@app.route('/logo')
def logo():
    filename = 'Hospital-logo-by-meisuseno-5.jpg'
    if os.path.exists(filename):
        return send_from_directory('.', filename)
    return '', 404

# =============================
# Cargar ids de pacientes de prueba (10100 a 10200)
# =============================
id_pacientes = [(str(10100 + i), f"Datos de prueba {i+1}") for i in range(100)]

@app.route('/get_paciente/<id_paciente>')
def get_paciente(id_paciente):
    try:
        df_ids = pd.read_csv('breast_cancer_dataset_peru.csv', sep=';')
        if 'id_paciente' not in df_ids.columns:
            return {}
        row = df_ids[df_ids['id_paciente'].astype(str) == str(id_paciente)]
        if row.empty:
            return {}
        # Renombrar y filtrar columnas igual que en el flujo principal
        row = row.rename(columns=renombrar_columnas)
        row = row.drop(columns=[col for col in columnas_a_eliminar if col in row.columns])
        data = row.iloc[0][input_columns].to_dict()
        data = {k: float(v) if pd.notnull(v) else 0.0 for k, v in data.items()}
        return data
    except Exception as e:
        return {}

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    probabilidades = None
    confianza = None
    error = None
    recomendacion = None
    values = {col: '' for col in input_columns}
    if request.method == 'POST':
        try:
            values = {col: float(request.form.get(col, 0.0)) for col in input_columns}
            pred = predecir_diagnostico(values)
            if 'error' in pred:
                error = pred['error']
            else:
                resultado = pred['diagnostico']
                probabilidades = pred['probabilidades']
                confianza = pred['confianza']
                if resultado == 'Benigno':
                    recomendacion = "El resultado es benigno. Se recomienda continuar con controles médicos regulares y mantener hábitos saludables."
                elif resultado == 'Maligno':
                    recomendacion = "El resultado es maligno. Se recomienda acudir a un especialista lo antes posible para una evaluación y tratamiento oportuno."
        except Exception as e:
            error = str(e)
    logo_path = url_for('logo')
    return render_template('index.html', input_columns=input_columns, values=values, resultado=resultado, probabilidades=probabilidades, confianza=confianza, error=error, logo_path=logo_path, recomendacion=recomendacion, id_pacientes=id_pacientes)

if __name__ == "__main__":
    app.run(debug=True)