import numpy as np
import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt
import os
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import SimpleRNN, Dense
from tensorflow.keras.optimizers import Adam
from sklearn.preprocessing import MinMaxScaler

def create_sequences(data, window_size):
    X, y = [], []
    for i in range(len(data) - window_size):
        X.append(data[i:i+window_size])
        y.append(data[i+window_size])
    return np.array(X), np.array(y)

df = pd.read_csv(
    r"classical_ml/datasets/airline_passengers.csv"
)

df = df[['passengers']]
print(df.head())

WINDOW_SIZE = 12

scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(df)

X, y = create_sequences(scaled_data, WINDOW_SIZE)

train_size = int(0.8 * len(X))

X_train, X_test = X[:train_size], X[train_size:]
y_train, y_test = y[:train_size], y[train_size:]

model = Sequential([
    SimpleRNN(
        units=50,
        activation="tanh",
        input_shape=(WINDOW_SIZE, 1) #12 Months'
    ),
    Dense(1)
])

model.compile(
    optimizer=Adam(learning_rate=0.001),
    loss="mse"
)

history = model.fit(
    X_train,
    y_train,
    epochs=50,
    batch_size=16,
    validation_data=(X_test, y_test),
    verbose=1
)

plt.figure()
plt.plot(history.history["loss"], label="Train Loss")
plt.plot(history.history["val_loss"], label="Validation Loss")
plt.xlabel("Epochs")
plt.ylabel("MSE Loss")
plt.title("Training vs Validation Loss")
plt.legend()
plt.grid(True)
plt.show()

predictions = model.predict(X_test)

# Inverse scale
predictions = scaler.inverse_transform(predictions)
y_test_actual = scaler.inverse_transform(y_test)

last_12_months = scaled_data[-WINDOW_SIZE:]
last_12_months = last_12_months.reshape(1, WINDOW_SIZE, 1)

next_month_scaled = model.predict(last_12_months)
next_month = scaler.inverse_transform(next_month_scaled)

plt.figure()

plt.plot(y_test_actual, label="Actual Passengers", marker="o")
plt.plot(predictions, label="Predicted Passengers", marker="x")

plt.xlabel("Time Step (Test Set)")
plt.ylabel("Passengers")
plt.title("Actual vs Predicted Airline Passengers")
plt.legend()
plt.grid(True)
plt.show()

print("Predicted passengers next month:", int(next_month[0][0]))

full_data = df["passengers"].values

train_plot = np.empty_like(full_data, dtype=float)
train_plot[:] = np.nan
train_plot[WINDOW_SIZE:train_size+WINDOW_SIZE] = scaler.inverse_transform(
    model.predict(X_train)
).flatten()

test_plot = np.empty_like(full_data, dtype=float)
test_plot[:] = np.nan
test_plot[train_size+WINDOW_SIZE:] = predictions.flatten()

plt.figure(figsize=(10, 5))
plt.plot(full_data, label="Actual Data")
plt.plot(train_plot, label="Train Predictions")
plt.plot(test_plot, label="Test Predictions")

plt.xlabel("Month")
plt.ylabel("Passengers")
plt.title("Airline Passenger Forecasting with RNN")
plt.legend()
plt.grid(True)
plt.show()
