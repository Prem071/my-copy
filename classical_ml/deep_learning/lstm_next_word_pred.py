import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

text = """
deep learning models learn patterns from data
deep learning models are powerful
deep learning enables neural networks
neural networks learn representations
"""

# ------------------------------------------------------------
# Tokenization: Convert words → integer IDs
#
# Example text:
# "deep learning models learn patterns from data"
#
# Step 1: Tokenizer scans the text and builds a vocabulary
# Each UNIQUE word gets a UNIQUE integer ID (starting from 1)
#
# Example word_index (order depends on frequency):
# {
#   'learning': 1,
#   'deep': 2,
#   'models': 3,
#   'learn': 4,
#   'patterns': 5,
#   'from': 6,
#   'data': 7
# }
#
# Step 2: vocab_size = number of unique words + 1
# The extra +1 is reserved for padding (ID = 0)
#
# vocab_size = 8
#
# Why we need this:
# - Neural networks cannot work with raw text
# - Words must be converted to numbers
# - These IDs are later used for:
#   - Sequence creation
#   - One-hot encoding
#   - Softmax output layer size

# ------------------------------------------------------------
# Tokenize Text
# ------------------------------------------------------------
tokenizer = Tokenizer()
tokenizer.fit_on_texts([text])

word_index = tokenizer.word_index
vocab_size = len(word_index) + 1

print("Vocabulary size:", vocab_size)
print("Word index:", word_index)

# ------------------------------------------------------------
# Convert Text to Sequence of Integers
# ------------------------------------------------------------
sequence = tokenizer.texts_to_sequences([text])[0]

print("Encoded sequence:", sequence)

# ------------------------------------------------------------
#  Create Sequences
# ------------------------------------------------------------
def create_sequences(sequence, window_size):
    X, y = [], []
    for i in range(len(sequence) - window_size):
        X.append(sequence[i:i + window_size])
        y.append(sequence[i + window_size])
    return np.array(X), np.array(y)

WINDOW_SIZE = 3   # previous 3 words → next word

X, y = create_sequences(sequence, WINDOW_SIZE)

print("X shape:", X.shape)
print("y shape:", y.shape)

# ------------------------------------------------------------
# One-Hot Encode Target
# ------------------------------------------------------------
y = tf.keras.utils.to_categorical(y, num_classes=vocab_size) # y → [0,0,0,1,0]

# ------------------------------------------------------------
# LSTM Model
# ------------------------------------------------------------
model = Sequential([
    LSTM(64, input_shape=(WINDOW_SIZE, 1)),
    Dense(vocab_size, activation="softmax")
])

model.compile(
    optimizer="adam",
    loss="categorical_crossentropy",
    metrics=["accuracy"]
)

model.summary()

model.fit(
    X.reshape(X.shape[0], X.shape[1], 1),
    y,
    epochs=200,
    verbose=1
)

# ------------------------------------------------------------
# Predicting Next Word
# ------------------------------------------------------------
def predict_next_word(text_input):
    encoded = tokenizer.texts_to_sequences([text_input])[0]
    encoded = pad_sequences([encoded], maxlen=WINDOW_SIZE, padding="pre")

    prediction = model.predict(encoded.reshape(1, WINDOW_SIZE, 1))
    predicted_index = np.argmax(prediction)

    for word, index in tokenizer.word_index.items():
        if index == predicted_index:
            return word

# ------------------------------------------------------------
# 9. Test Prediction
# ------------------------------------------------------------
seed_text = "deep learning models"
next_word = predict_next_word(seed_text)

print(f"Input: '{seed_text}'")
print(f"Predicted next word: '{next_word}'")
