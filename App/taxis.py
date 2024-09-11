import streamlit as st
import seaborn as sns
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor

# Cargar el dataset de Seaborn
taxis_df = sns.load_dataset("taxis")

# Reemplazar valores nulos en columnas categóricas con la moda
taxis_df['payment'].fillna(taxis_df['payment'].mode()[0], inplace=True)
taxis_df['pickup_zone'].fillna(taxis_df['pickup_zone'].mode()[0], inplace=True)
taxis_df['dropoff_zone'].fillna(taxis_df['dropoff_zone'].mode()[0], inplace=True)
taxis_df['pickup_borough'].fillna(taxis_df['pickup_borough'].mode()[0], inplace=True)
taxis_df['dropoff_borough'].fillna(taxis_df['dropoff_borough'].mode()[0], inplace=True)

# Crear una nueva columna 'trip_duration' en minutos
taxis_df['trip_duration'] = (taxis_df['dropoff'] - taxis_df['pickup']).dt.total_seconds() / 60

# Seleccionar características y variable objetivo
X = taxis_df[['distance', 'fare', 'tolls', 'total', 'trip_duration', 'passengers']]
y = taxis_df['tip']

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Normalizar los datos
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Crear y entrenar el modelo
modelo_bosque = RandomForestRegressor(random_state=42, n_estimators=100)
modelo_bosque.fit(X_train_scaled, y_train)

# Título de la app
st.title('Predicción de Propinas de Taxis')

# Entrada de datos
st.header('Introduce los datos del viaje:')
distance = st.number_input('Distancia (millas)', min_value=0.0, format="%.2f")
fare = st.number_input('Tarifa ($)', min_value=0.0, format="%.2f")
tolls = st.number_input('Peajes ($)', min_value=0.0, format="%.2f")
total = st.number_input('Total ($)', min_value=0.0, format="%.2f")
trip_duration = st.number_input('Duración del viaje (minutos)', min_value=0.0, format="%.2f")
passengers = st.number_input('Número de pasajeros', min_value=1, step=1)

# Predicción
if st.button('Predecir'):
    input_data = np.array([[distance, fare, tolls, total, trip_duration, passengers]])
    input_data_scaled = scaler.transform(input_data)
    prediction = modelo_bosque.predict(input_data_scaled)
    st.write(f'La propina predicha es: ${prediction[0]:.2f}')
