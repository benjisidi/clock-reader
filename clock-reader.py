import tensorflow as tf
from tensorflow import keras
from sklearn.model_selection import train_test_split
import numpy as np
import time

# Visualization to confirm correct loading of data
from PIL import Image
from matplotlib import pyplot as plt


# --- Load and split data ---
start = time.time()
clocks_data = np.fromfile("./clock_images.npy", dtype=np.uint8)
labels_data = np.fromfile("./clock_labels.npy", dtype=np.uint8)
end = time.time()

print(f"Loaded data in {end -start}s")

clocks = np.reshape(clocks_data, (184320, 50, 50, 1))
labels = np.reshape(labels_data, (184320, 2))

start = time.time()
clocks_train, clocks_test, labels_train, labels_test = train_test_split(
    clocks, labels, test_size=0.33, random_state=1
)
end = time.time()

print(f"Split data in {end -start}s")

# --- Initialize model ---
model = keras.Sequential()
model.add(
    keras.layers.Conv2D(
        25,
        (3, 3),
        activation="relu",
        input_shape=(50, 50, 1),
        data_format="channels_last",
    )
)
model.add(keras.layers.MaxPool2D((2, 2)))
model.add(keras.layers.Conv2D(50, (3, 3), activation="relu"))
model.add(keras.layers.MaxPool2D((2, 2)))
model.add(keras.layers.Conv2D(50, (3, 3), activation="relu"))
model.add(keras.layers.Flatten())
model.add(keras.layers.Dense(64, activation="relu"))
model.add(keras.layers.Dense(2))

model.summary()

model.compile(
    optimizer="adam", loss="mse", metrics=["accuracy"],
)


# --- Train model ---
history = model.fit(clocks_train, labels_train, epochs=1)

model.evaluate(clocks_test, labels_test)

model.save("reader-model")
