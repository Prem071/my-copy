# ============================================================
# Energy Demand Forecasting using GRU (Single .py Script)
# ============================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import GRU, Dense
from tensorflow.keras.optimizers import Adam
from sklearn.preprocessing import MinMaxScaler

# ------------------------------------------------------------
# Realistic Energy Data (Hourly, 1 Year)
# ------------------------------------------------------------
np.random.seed(42)

HOURS = 24 * 365
time = np.arange(HOURS)

# Temperature (seasonal)
temperature = (
    10
    + 15 * np.sin(2 * np.pi * time / (24 * 365))
    + np.random.normal(0, 2, HOURS)
)

# Energy demand (target)
demand = (
    100
    + 0.6 * temperature
    + 20 * np.sin(2 * np.pi * time / 24)     # daily cycle
    + np.random.normal(0, 5, HOURS)
)

df = pd.DataFrame({
    "temperature": temperature,
    "demand": demand
})

print(df.head())
print("Data shape:", df.shape)


plt.figure(figsize=(10, 4))
plt.plot(df["demand"], label="Energy Demand")
plt.xlabel("Hour")
plt.ylabel("Demand")
plt.title("Raw Energy Demand Time Series (Model Input)")
plt.legend()
plt.grid(True)
plt.show()

scaler_X = MinMaxScaler()
scaler_y = MinMaxScaler()

df["hour"] = time % 24
df["day"] = (time // 24) % 7

X_scaled = scaler_X.fit_transform(
    df[["demand", "temperature", "hour", "day"]]
)

y_scaled = scaler_y.fit_transform(df[["demand"]])

def create_sequences(X, y, window_size):
    X_seq, y_seq = [], []
    for i in range(len(X) - window_size):
        X_seq.append(X[i:i + window_size])
        y_seq.append(y[i + window_size])
    return np.array(X_seq), np.array(y_seq)

WINDOW_SIZE = 24   # 24 hours → next hour

X, y = create_sequences(X_scaled, y_scaled, WINDOW_SIZE)

print("Sequence X shape:", X.shape)
print("Sequence y shape:", y.shape)


split = int(0.8 * len(X))

X_train, X_test = X[:split], X[split:]
y_train, y_test = y[:split], y[split:]


# Build GRU Model

model = Sequential([
    GRU(
        units=64,
        activation="tanh",
        input_shape=(WINDOW_SIZE, 4)
    ),
    Dense(32, activation="relu"),
    Dense(1)
])

model.compile(
    optimizer=Adam(learning_rate=0.001),
    loss="mse"
)

model.summary()

history = model.fit(
    X_train,
    y_train,
    epochs=20,
    batch_size=32,
    validation_data=(X_test, y_test),
    verbose=1
)

plt.figure()
plt.plot(history.history["loss"], label="Train Loss")
plt.plot(history.history["val_loss"], label="Validation Loss")
plt.xlabel("Epoch")
plt.ylabel("MSE")
plt.title("GRU Training vs Validation Loss")
plt.legend()
plt.grid(True)
plt.show()


predictions = model.predict(X_test)

predictions = scaler_y.inverse_transform(predictions)
y_test_actual = scaler_y.inverse_transform(y_test)

# ------------------------------------------------------------
# 10. Plot Actual vs Predicted Demand
# ------------------------------------------------------------
plt.figure(figsize=(10, 4))
plt.plot(y_test_actual, label="Actual Demand", marker="o")
plt.plot(predictions, label="Predicted Demand", marker="x")
plt.xlabel("Time Step (Test Set)")
plt.ylabel("Energy Demand")
plt.title("Energy Demand Forecasting using GRU")
plt.legend()
plt.grid(True)
plt.show()

# ------------------------------------------------------------
# 11. Predict Next Hour
# ------------------------------------------------------------
last_24_hours = X_scaled[-WINDOW_SIZE:]
last_24_hours = last_24_hours.reshape(1, WINDOW_SIZE, 1)

next_hour_scaled = model.predict(last_24_hours)
next_hour_demand = scaler_y.inverse_transform(next_hour_scaled)

print("Predicted energy demand next hour:", round(next_hour_demand[0][0], 2))
