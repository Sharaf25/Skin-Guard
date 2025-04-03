import tensorflow as tf
from tensorflow.keras.layers import Conv2D, Flatten, Dense, MaxPool2D
from tensorflow.keras.models import Sequential

# Class labels and descriptions
classes = {
    0: "Actinic keratoses and intraepithelial carcinomae (Cancer)",
    1: "Basal cell carcinoma (Cancer)",
    2: "Benign keratosis-like lesions (Non-Cancerous)",
    3: "Dermatofibroma (Non-Cancerous)",
    4: "Melanocytic nevi (Non-Cancerous)",
    5: "Pyogenic granulomas and hemorrhage (Can lead to cancer)",
    6: "Melanoma (Cancer)",
}

# Function to get additional information based on the class index
def get_info(class_ind):
    info_dict = {
        0: "Actinic keratosis is a pre-malignant lesion that can develop into squamous cell carcinoma.",
        1: "Basal cell carcinoma is a common type of skin cancer that often appears as a transparent bump.",
        2: "Benign keratosis-like lesions are non-cancerous growths that are usually harmless.",
        3: "Dermatofibromas are small, benign skin growths that often appear on the legs or arms.",
        4: "Melanocytic nevi, commonly known as moles, are usually benign but should be monitored for changes.",
        5: "Pyogenic granulomas are small, red skin growths that can bleed easily and may require treatment.",
        6: "Melanoma is a serious type of skin cancer that develops in melanocytes and requires prompt attention.",
    }
    return info_dict.get(class_ind, "No additional information available.")

# Define the CNN model
model = Sequential()
model.add(Conv2D(16, kernel_size=(3, 3), input_shape=(28, 28, 3), activation="relu", padding="same"))
model.add(MaxPool2D(pool_size=(2, 2)))
model.add(tf.keras.layers.BatchNormalization())
model.add(Conv2D(32, kernel_size=(3, 3), activation="relu"))
model.add(Conv2D(64, kernel_size=(3, 3), activation="relu"))
model.add(MaxPool2D(pool_size=(2, 2)))
model.add(tf.keras.layers.BatchNormalization())
model.add(Conv2D(128, kernel_size=(3, 3), activation="relu"))
model.add(Conv2D(256, kernel_size=(3, 3), activation="relu"))
model.add(Flatten())
model.add(tf.keras.layers.Dropout(0.2))
model.add(Dense(256, activation="relu"))
model.add(tf.keras.layers.BatchNormalization())
model.add(tf.keras.layers.Dropout(0.2))
model.add(Dense(128, activation="relu"))
model.add(tf.keras.layers.BatchNormalization())
model.add(Dense(64, activation="relu"))
model.add(tf.keras.layers.BatchNormalization())
model.add(tf.keras.layers.Dropout(0.2))
model.add(Dense(32, activation="relu"))
model.add(tf.keras.layers.BatchNormalization())
model.add(Dense(7, activation="softmax"))
model.summary()

# Load pre-trained weights
model.load_weights("best_model.h5")