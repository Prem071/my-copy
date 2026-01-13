# ============================================================
# Univariate Retail Sales Forecasting using LSTM
# Predicting multiple future steps
# ============================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from tensorflow.keras.optimizers import Adam
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error

# ------------------------------------------------------------
# Synthetic Retail Sales Data (Daily)
# ------------------------------------------------------------
np.random.seed(42)

DAYS = 365 * 2   # 2 years
time = np.arange(DAYS)

sales = (
    200
    + 30 * np.sin(2 * np.pi * time / 7)      # weekly seasonality
    + 50 * np.sin(2 * np.pi * time / 365)    # yearly seasonality
    + np.random.normal(0, 10, DAYS)
)

df = pd.DataFrame({"sales": sales})

print(df.head())
print("Data shape:", df.shape)

plt.figure(figsize=(10, 4))
plt.plot(df["sales"], label="Daily Sales")
plt.xlabel("Day")
plt.ylabel("Sales")
plt.title("Raw Retail Sales Time Series (Input)")
plt.legend()
plt.grid(True)
plt.show()

scaler = MinMaxScaler()
scaled_sales = scaler.fit_transform(df[["sales"]])

def create_sequences(data, window_size, n_steps_ahead):
    X, y = [], []
    for i in range(len(data) - window_size - n_steps_ahead):
        X.append(data[i:i + window_size])
        y.append(data[i + window_size : i + window_size + n_steps_ahead])
    return np.array(X), np.array(y)

WINDOW_SIZE = 30        # past 30 days
N_STEPS_AHEAD = 7       # predict next 7 days

X, y = create_sequences(scaled_sales, WINDOW_SIZE, N_STEPS_AHEAD)

print("Input shape:", X.shape)   # (samples, 30, 1)
print("Target shape:", y.shape)  # (samples, 7, 1)


split = int(0.8 * len(X))

X_train, X_test = X[:split], X[split:]
y_train, y_test = y[:split], y[split:]

# LSTM Model

model = Sequential([
    LSTM(
        units=64,
        activation="tanh",
        input_shape=(WINDOW_SIZE, 1)
    ),
    Dense(N_STEPS_AHEAD)
])

model.compile(
    optimizer=Adam(learning_rate=0.001),
    loss="mse"
)

model.summary()


history = model.fit(
    X_train,
    y_train,
    epochs=30,
    batch_size=32,
    validation_data=(X_test, y_test),
    verbose=1
)


plt.figure()
plt.plot(history.history["loss"], label="Train Loss")
plt.plot(history.history["val_loss"], label="Validation Loss")
plt.xlabel("Epoch")
plt.ylabel("MSE")
plt.title("LSTM Training vs Validation Loss")
plt.legend()
plt.grid(True)
plt.show()


# Predictions (Test Set)

predictions = model.predict(X_test)

# Inverse scaling
predictions = scaler.inverse_transform(
    predictions.reshape(-1, 1)
).reshape(predictions.shape)

y_test_actual = scaler.inverse_transform(
    y_test.reshape(-1, 1)
).reshape(y_test.shape)


# Plot ONE Forecast Window (Very Important)

plt.figure(figsize=(10, 4))

plt.plot(
    range(N_STEPS_AHEAD),
    y_test_actual[0].flatten(),
    marker="o",
    label="Actual Future Sales"
)

plt.plot(
    range(N_STEPS_AHEAD),
    predictions[0].flatten(),
    marker="x",
    label="Predicted Future Sales"
)

plt.xlabel("Days Ahead")
plt.ylabel("Sales")
plt.title("7-Day Ahead Sales Forecast (LSTM)")
plt.legend()
plt.grid(True)
plt.show()


# Predict NEXT 7 DAYS (Future)

last_window = scaled_sales[-WINDOW_SIZE:]
last_window = last_window.reshape(1, WINDOW_SIZE, 1)

future_scaled = model.predict(last_window)
future_sales = scaler.inverse_transform(future_scaled.reshape(-1, 1))

print("Predicted sales for next 7 days:")
for i, value in enumerate(future_sales.flatten(), 1):
    print(f"Day +{i}: {round(value, 2)}")


# ------------------------------------------------------------
# 12. Evaluation Metrics
# ------------------------------------------------------------
y_true = y_test_actual.reshape(-1)
y_pred = predictions.reshape(-1)

mae = mean_absolute_error(y_true, y_pred)
rmse = np.sqrt(mean_squared_error(y_true, y_pred))
mape = np.mean(np.abs((y_true - y_pred) / y_true)) * 100
smape = np.mean(
    2 * np.abs(y_pred - y_true) / (np.abs(y_true) + np.abs(y_pred))
) * 100

print("\nModel Evaluation Metrics:")
print("MAE  :", round(mae, 2))
print("RMSE :", round(rmse, 2))
print("MAPE :", round(mape, 2), "%")
print("SMAPE:", round(smape, 2), "%")
