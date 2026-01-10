import tensorflow as tf
from tensorflow.keras import layers, models
import matplotlib.pyplot as plt

# -------------------------------
# 1. Load MNIST (Already Grayscale)
# -------------------------------
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

# Shape: (N, 28, 28)
print("Original shape:", x_train.shape)

x_train = x_train / 255.0
x_test  = x_test / 255.0

x_train = x_train[..., tf.newaxis]
x_test  = x_test[..., tf.newaxis]

print("CNN input shape:", x_train.shape)  # (N, 28, 28, 1)

# -------------------------------
# 3. Build Simple CNN
# -------------------------------
model = models.Sequential([
    layers.Conv2D(32, (3,3), activation='relu', input_shape=(28,28,1)),
    layers.MaxPooling2D((2,2)),

    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax')
])

# -------------------------------
# 4. Compile Model
# -------------------------------
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

model.summary()

# -------------------------------
# 5. Train
# -------------------------------
history = model.fit(
    x_train, y_train,
    epochs=5,
    validation_split=0.2
)

# -------------------------------
# 6. Evaluate
# -------------------------------

test_loss, test_acc = model.evaluate(x_test, y_test)
print("Test accuracy:", test_acc)

# -------------------------------
# 7. Visualize Testing Input
# -------------------------------

plt.imshow(x_test[2].squeeze(), cmap='gray')
plt.title(f"Label: {y_test[2]}")
plt.axis('off')
plt.show()

# -------------------------------
# 8. Prediction
# -------------------------------

import numpy as np

prediction = model.predict(x_test[2][np.newaxis, ...])
pred_digit = np.argmax(prediction)
print("Actual", y_test[2])
print("Predicted", y_test[2])


# -------------------------------
# 7. Visualize One Input
# -------------------------------
plt.imshow(x_train[0].squeeze(), cmap='gray')
plt.title(f"Label: {y_train[0]}")
plt.axis('off')
plt.show()
