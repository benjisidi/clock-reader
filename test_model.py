import tensorflow as tf
from tensorflow import keras
import numpy as np
import time
from sklearn.model_selection import train_test_split

# Visualization to confirm correct loading of data
from PIL import Image
from matplotlib import pyplot as plt


def show_clock(clock, pred):
    image = Image.fromarray(clock)
    plt.figure()
    plt.imshow(image)
    predicted_hour = round(pred[0])
    predicted_min = round(pred[1])
    plt.title(f"Prediction: {max(0,predicted_hour):2.0f}:{predicted_min:2.0f}")


# --- Load and split data ---
start = time.time()
clocks_data = np.fromfile("./clock_images.npy", dtype=np.uint8)
labels_data = np.fromfile("./clock_labels.npy", dtype=np.uint8)
end = time.time()

print(f"Loaded data in {end -start}s")

clocks = np.reshape(clocks_data, (184320, 50, 50, 1))
clocks = np.reshape(clocks_data, (184320, 50, 50, 1))
labels = np.reshape(labels_data, (184320, 2))

start = time.time()
clocks_train, clocks_test, labels_train, labels_test = train_test_split(
    clocks, labels, test_size=0.33, random_state=1
)
end = time.time()
clocks_test_images = np.reshape(clocks_test, (clocks_test.shape[0], 50, 50))
print(f"Split data in {end -start}s")


# --- Load Model ---
model = keras.models.load_model("reader-model")

predictions = model.predict(clocks_test)
print(predictions[0])
for i in range(10):
    show_clock(clocks_test_images[i], predictions[i])
plt.show()
