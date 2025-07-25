# -*- coding: utf-8 -*-
"""MLCV_33085799.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Umos8V_irKouqxiisJFmOc3fT1fgecF_

The Python libraries required for machine learning, image processing, charting, and numerical operations are imported in this section.
"""

import numpy as np
import cv2
import os
import skimage
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report

"""The 70,000 handwritten digits that make up the MNIST dataset are loaded. The photographs are in X, and the labels that go with each image are in Y."""

mnist = fetch_openml('mnist_784', version=1)
X, y = mnist["data"], mnist["target"]

"""The dataset is partitioned into training and testing sets, allocating 30% of the data for testing purposes. This aids in verifying the model's performance on data that has not been previously encountered.

"""

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
print("Shape of Images: {} \nShape of Labels: {}".format(X.shape, y.shape))

"""The training data is used to initialise and train a Support Vector Machine (SVM) model with a radial basis function (rbf) kernel."""

model = SVC(kernel='rbf', C=1.0, gamma='scale', max_iter=10000)
model.fit(X_train, y_train)

"""The model is used to make predictions regarding the distribution of labels for the test set, and the precision of these predictions is computed and displayed."""

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy on Test Data: {accuracy:.2f}")

"""This section prints a detailed classification report, which includes precision, recall, f1-score, and support for each class."""

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

"""The performance of a machine learning model trained on the MNIST dataset has been assessed in this script through the visualisation of its predictions. I chose 10 test photographs, resized them to their original dimensions of 28x28 pixels, and presented each image in a grid along with the anticipated label of the model, as shown above. This method enables a rapid and unambiguous evaluation of the model's ability to reliably recognise handwritten digits."""

import warnings

warnings.filterwarnings("ignore")

num_samples = 10

# Define the number of columns
num_cols = 5

# Determine the number of rows based on the number of images and the number of columns
num_rows = (num_samples + 1) // num_cols

# Set the figure size to adjust the image size
plt.figure(figsize=(5 * num_cols, 5 * num_rows))

# Iterate over a sample of test data
for i in range(num_samples):
    # Get the image and its corresponding label
    image = X_test.iloc[i].values.reshape(28, 28)  # Convert DataFrame to numpy array and reshape
    label = y_test.iloc[i]

    # Predict the number in the image
    predicted_number = model.predict([X_test.iloc[i]])[0]  # Predict using iloc to access rows

    # Plot the image
    plt.subplot(num_rows, num_cols, i + 1)
    plt.imshow(image, cmap='gray')
    plt.title(f"Predicted Number: {predicted_number}")
    plt.axis('off')

plt.tight_layout()
plt.show()

"""In this script, I'm gathering grayscale images from a folder in my Google Drive, filtering for files that end with ".jpg" or ".png". I construct the filepath for each image, load it in grayscale using OpenCV's cv2.imread, and then append each image to the handwritten_images list for further analysis."""

image_folder = '/content/drive/MyDrive/MachineLearning-Single'  # Change this to your Google Drive folder containing images
handwritten_images = []
for filename in os.listdir(image_folder):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        filepath = os.path.join(image_folder, filename)
        image = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
        handwritten_images.append(image)

"""In this section of the script, the collected photos are being preprocessed to ensure that they are in a consistent format that is appropriate for input into the model. The photos in the handwritten_images list are resized to a resolution of 28x28 pixels using the cv2.resize function in OpenCV. This process ensures that the proportions of all images are standardised.

Following the process of resizing, the list of photographs is transformed into a NumPy array, which is further reshaped to ensure that each image is flattened into a single-dimensional array. The process of reshaping is essential in order to ensure conformity with the input specifications of numerous machine learning models. These models typically anticipate each sample to be representing a flat array of attributes.
"""

preprocessed_images = [cv2.resize(image, (28, 28)) for image in handwritten_images]
preprocessed_images = np.array(preprocessed_images).reshape(len(preprocessed_images), -1)

"""In the present script, the trained model is employed to make predictions on digits based on preprocessed images that have undergone resizing and flattening. Following that, the photos are shown in a grid format, accompanied by their corresponding predicted digits. The grid has a fixed configuration with five columns, with the number of rows being calculated by dividing the total number of photos by the column count. I created a subplot for each image and its accompanying prediction.

I labeled the image with the expected digit and make sure that the visualisation is not cluttered by any axis information. In order to maintain a tidy display, any superfluous subplots lacking photos are rendered inconspicuous. This configuration enables the user to visually validate the model's predictions by comparing them with the actual photos, hence facilitating a straightforward and unambiguous evaluation of the model's efficiency.
"""

predicted_digits = model.predict(preprocessed_images)

# Display the predicted digits along with the images
num_images = len(handwritten_images)
num_cols = 5  # Define the number of columns
num_rows = (num_images + 1) // num_cols

fig, axes = plt.subplots(num_rows, num_cols, figsize=(10, 5 * num_rows))

for i, (image, digit) in enumerate(zip(handwritten_images, predicted_digits)):
    if i < num_images:  # Ensure not to exceed the number of images
        row_idx = i // num_cols
        col_idx = i % num_cols
        axes[row_idx, col_idx].imshow(image, cmap='gray')
        axes[row_idx, col_idx].set_title(f'Predicted Digit: {digit}')
        axes[row_idx, col_idx].axis('off')
    else:  # If there are extra subplots, hide them
        axes.flat[i].set_visible(False)

plt.tight_layout()
plt.show()

print(y_train.dtype)
print(y_train.dtype)

"""I begin by importing the required libraries in this code sample, which include pandas, NumPy, and TensorFlow components for data processing and model construction. I next make sure TensorFlow is compatible with our label arrays by checking the data types of y_train and y_test and converting categorical labels to integer codes.

After that, I prepared the X_train and X_test feature arrays by reshaping them to match the input specifications of our convolutional neural network (CNN) and turning them to float32 numpy arrays. I build the CNN using a set of layers specifically intended for picture recognition, combine it with the proper optimizer and loss function, and then train it using the data that has been processed. In order to enable reuse of the trained model without the need for retraining, I lastly save it to a file. For picture classification problems, this method is simple and efficient.
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from tensorflow.keras import layers, models

# Assuming X and y have already been loaded, split, and preprocessed

# Check data types of labels and convert if necessary
print("Initial dtype of y_train:", y_train.dtype)
print("Initial dtype of y_test:", y_test.dtype)

# Convert categorical labels to integers
y_train = y_train.cat.codes
y_test = y_test.cat.codes

# Ensure the features are float32 arrays for TensorFlow
X_train = np.asarray(X_train).astype('float32')
X_test = np.asarray(X_test).astype('float32')

# Reshape data for CNN if not already reshaped in preprocessing
X_train = X_train.reshape((-1, 28, 28, 1))
X_test = X_test.reshape((-1, 28, 28, 1))

# Define the CNN model
model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dense(10, activation='softmax')  # Ensure this matches the number of categories
])

# Compile the model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, epochs=10, validation_data=(X_test, y_test))

# Save the model
model.save('my_mnist_model.h5')

model_path = 'my_mnist_model.h5'
model.save(model_path)

from tensorflow.keras.models import load_model

# Load the model from the saved file
deployed_model = load_model(model_path)

"""
In this code snippet, I loaded an image from a specified path and converted it to grayscale using OpenCV. Then, I applied Gaussian thresholding to create a binary image where the pixels were either black or white, aiding in distinguishing objects from the background. I identified and sorted the contours of the objects in the image based on their horizontal position. For each contour, I drew a green bounding box on the original image and extracted the portion within the box. This extracted image was resized to 28x28 pixels, a common size for input into image processing models. These resized images were collected into a list. Finally, I displayed the original image with the drawn bounding boxes using OpenCV's display function, allowing for visual verification of the extraction and bounding process."""

image = cv2.imread('/content/drive/MyDrive/MachineLearning-Multiple/010.png')
# grayscale image
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Gaussian thresholding
_, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV)

# Find contours
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = sorted(contours, key=lambda x: cv2.boundingRect(x)[0])
cut_images = []

for contour in contours:
    x, y, width, height = cv2.boundingRect(contour)

    # Draw bounding box in original picture
    cv2.rectangle(image, (x, y), (x + width , y + height ), (0, 255, 0), 2)

    # Cut and save image contain number
    extracted_digit = gray[y:y+height, x:x+width]
    resized_digit = cv2.resize(extracted_digit, (28, 28))
    cut_images.append(resized_digit)

cv2_imshow(image)

"""This section of the code is used for predicting the digits present in images that have been extracted and preprocessed in earlier steps. Each digit image, which has been cut and resized from a larger image, is individually processed to predict which digit it represents using a pre-trained neural network model. This allows for an automated and quick interpretation of numerical data from images, which can be essential in applications such as digit recognition in scanned documents or number plate recognition systems.

The loop functions by cycling through each processed digit image, reshaping and feeding it into the neural network to obtain a prediction for the digit it contains. After predicting, the loop displays each image alongside the predicted digit, providing a visual representation of the model's accuracy and effectiveness. This repetitive process ensures that each digit is evaluated, making the system efficient in handling multiple digit predictions in a sequence.
"""

# predict of digits in the above image
for i, digit_image in enumerate(cut_images):
    testX = digit_image.reshape((1, 28, 28, 1))
    predictions = deployed_model.predict(testX)
    predicted_labels = np.argmax(predictions, axis=1)
    cv2_imshow(digit_image)
    print(predicted_labels)

"""In this code snippet, I enhanced the process of digit extraction from an image by adding padding around each digit to better center them within their bounding boxes. I converted the image to grayscale, applied Gaussian thresholding with Otsu's method for clear separation, and sorted the contours. I then adjusted the bounding boxes to include extra padding, resized each extracted digit to 28x28 pixels, and displayed the image with green bounding boxes to confirm the modifications visually. This additional padding aimed to improve the consistency and accuracy of the inputs for machine learning predictions."""

image = cv2.imread('/content/drive/MyDrive/MachineLearning-Multiple/011.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Gaussian thresholding
_, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# Find contours
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = sorted(contours, key=lambda x: cv2.boundingRect(x)[0])

# add padding to cut image contain number
# so the number can be more in center
c = 20
cut_images= []

for contour in contours:

    x, y, w, h = cv2.boundingRect(contour)

    # Draw bounding box in original picture
    cv2.rectangle(image, (x-c, y-c), (x + w + c, y + h + c), (0, 255, 0), 2)

    digits = gray[y-c:y+h+c, x-c:x+w+c]
    resized_digit = cv2.resize(digits, (28, 28))
    cut_images.append(resized_digit)

cv2_imshow(image)

"""In this code snippet, I processed each digit image to enhance clarity before prediction. I inverted the colors for better contrast and applied dilation to make the digits clearer. Each image was reshaped for the neural network, and predictions were made for the most likely digit. The processed images were displayed alongside their predicted labels for visual verification of the model's accuracy."""

for i, box in enumerate(cut_images):
    # convert black and white
    box = 255 - box

    # dilation so the number is more clear
    kernel = np.ones((2, 2), np.uint8)
    box = cv2.dilate(box, kernel, iterations=1)

    testX = box.reshape((1, 28, 28, 1))
    predictions = model.predict(testX)
    predicted_labels = np.argmax(predictions, axis=1)
    cv2_imshow(box)
    print(predicted_labels)

"""This code extracts and classifies individual digits according to their closeness by loading and processing an image. To decrease noise, I first loaded the image, converted it to grayscale, and then applied Gaussian blur. I created a binary image using thresholding to distinguish the numbers from the backdrop. I looped through each contour to find the bounding box for each digit after recognising and classifying the contours according to their horizontal positions.

I determined the Euclidean distance between the centres of each digit's bounding boxes to see if it was close to the preceding one during the loop. I labelled the digit as near if the distance fell under a set threshold; if not, it was deemed isolated. To verify that every digit was captured, I added padding to each extraction and drew extended bounding boxes around the numbers for clarity. To ensure uniformity, every extracted digit was scaled to 28 by 28 pixels.

After processing each digit, I finally changed the previous bounding box's position to the current one. To visually verify that the digit extraction and proximity categorization were accurate, the corrected image with the bounding boxes drawn was shown. When handling images with closely spaced or clustered digits, this method is very helpful since it enables focused processing and analysis for tasks like data input automation and digit recognition.
"""

import math
from google.colab.patches import cv2_imshow

# Load image
image_path = '/content/drive/MyDrive/MachineLearning-Multiple/012.png'
image = cv2.imread(image_path)

# Convert image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Reduce noise
blurred = cv2.GaussianBlur(gray, (25, 25), 0)

# Thresholding to get binary image
_, binary_image = cv2.threshold(blurred, 127, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# Find contours
contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = sorted(contours, key=lambda x: cv2.boundingRect(x)[0])

# Initialize lists
cut_digits = []
is_near = []
previous_x = 0
previous_y = 0
previous_width = 0
previous_height = 0

# Padding and distance threshold
padding = 100
distance_threshold = 1000

# Loop through contours
for contour in contours:
    x, y, width, height = cv2.boundingRect(contour)

    # Check if the current digit is near the previous one
    if math.sqrt(((x + width/2 - previous_x - previous_width/2)**2 + (y + height/2 - previous_y - previous_height/2)**2)) <= distance_threshold:
        is_near.append(1)
    else:
        is_near.append(0)

    # Draw bounding box
    cv2.rectangle(image, (x - padding, y - padding), (x + width + padding, y + height + padding), (0, 255, 0), 2)

    # Extract digit
    digit = binary_image[y - padding:y + height + padding, x - padding:x + width + padding]
    resized_digit = cv2.resize(digit, (28, 28))
    cut_digits.append(resized_digit)

    # Update previous box
    previous_x, previous_y, previous_width, previous_height = x, y, width, height

# Display image
cv2_imshow(image)

"""I analysed a sequence of digit pictures for prediction in this snippet of code. I began by setting up a list to hold the projected labels. I resized each digit's image to fit the neural network's specifications, and then I used the deployed_model to get predictions. Using np.argmax, I was able to extract the most likely digit from the model's output and show each digit's image for visual confirmation. Every anticipated label was appended to the roster. I printed the assembled list of predictions after processing every picture so I could check how well the model identified the digits."""

# Initialize list to store predictions
predictions_list = []

# Loop through cut images
for i, digit_box in enumerate(cut_digits):
    # Reshape digit box for prediction
    test_image = digit_box.reshape((1, 28, 28, 1))

    # Get predictions from the model
    predictions = deployed_model.predict(test_image)

    # Get predicted label
    predicted_label = np.argmax(predictions, axis=1)

    # Display digit box
    cv2_imshow(digit_box)

    # Append predicted label to output list
    predictions_list.append(predicted_label[0])

# Print final outputs
print("Predictions List:", predictions_list)

"""This code snippet shows how I built up and trained a convolutional neural network (CNN) with TensorFlow on the MNIST dataset. To prepare the photos for neural network training, I started by loading the dataset and reshaping and normalising them. After that, I divided the training set into two halves so that I could assess how well the model performed during training. The sparse categorical crossentropy loss and Adam optimizer were used in the construction of the CNN architecture, which featured layers for feature extraction and classification. I saved the model to a file and reloaded it to ensure its integrity after training the model for ten epochs using the training and validation data. This procedure guarantees that the model is prepared for next forecasts and analyses."""

import tensorflow as tf
from tensorflow.keras.datasets import mnist

# Load MNIST dataset
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# Preprocess data
X_train = X_train.reshape((X_train.shape[0], 28, 28, 1)).astype('float32') / 255
X_test = X_test.reshape((X_test.shape[0], 28, 28, 1)).astype('float32') / 255

# Split training data into training and validation sets
val_split = 0.2
val_size = int(len(X_train) * val_split)

X_val = X_train[-val_size:]
y_val = y_train[-val_size:]

X_train = X_train[:-val_size]
y_train = y_train[:-val_size]

# Define model architecture
model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    tf.keras.layers.MaxPooling2D((2, 2)),
    tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D((2, 2)),
    tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])

# Compile model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Train model
model.fit(X_train, y_train, epochs=10, validation_data=(X_val, y_val))

# Save model
model.save('my_model2.h5')

# Load model
loaded_model = tf.keras.models.load_model('my_model2.h5')

"""I manipulated an image to improve the accuracy of digit identification in this snippet of code. To make a binary image, I loaded the picture, turned it to grayscale, and then used Otsu's thresholding. In order to further enhance the image, I used a 3 × 5 kernel for erosion, which helps to separate related digits by making them thinner and reduce noise. To visually assess how well these adjustments prepared the image for more precise digit recognition, I presented the processed image."""

image = cv2.imread('/content/drive/MyDrive/MachineLearning-Multiple/013.png')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, binary_image  = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# Erosion so predict digit can be more accuracy
kernel = np.ones((3,5), np.uint8)
image2 = cv2.erode(binary_image, kernel, iterations=1)
#image2 = cv2.dilate(image2, kernel, iterations=1)
cv2_imshow(image2)

"""I began with an image, extracted the digit shapes, sorted them, then added padding to make sure the encapsulation was complete. After resizing each extracted digit to 28 by 28 pixels, the Euclidean distance was used to determine how close it was to the preceding digit. In order to verify precise segmentation and get the digits ready for recognition tasks, I presented the processed image with bounding boxes."""

# Find contours
contours, _ = cv2.findContours(image2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = sorted(contours, key=lambda x: cv2.boundingRect(x)[0])

is_near = []
cut_images = []

pre_x = 0
pre_y = 0
pre_w = 0
pre_h = 0

# Adapt parameters
c = 10
d = 80

for contour in contours:

    x, y, w, h = cv2.boundingRect(contour)
    if math.sqrt((((x + w/2) - (pre_x + pre_w/2))**2 + ((y + h/2) - (pre_y + pre_h/2))**2)) <= d:
      is_near.append(1)
    else:
      is_near.append(0)

    # Draw bounding box
    cv2.rectangle(image, (x-c, y-c), (x + w + c, y + h + c), (0, 255, 0), 2)

    # Cắt và lưu ảnh chứa chữ số
    digit = image2[y-c:y+h+c, x-c:x+w+c]
    resized_digit = cv2.resize(digit, (28, 28))
    cut_images.append(resized_digit)

    pre_x,pre_y,pre_w,pre_h = x,y,w,h

cv2_imshow(image)

"""I looped over a series of digit images in this snippet of code, altering each to make it compatible with a neural network model that was already loaded. I identified the digit I thought would appear in each picture, showed it for visual verification, and saved the estimated label in an output list. In order to make sure every processed number was correctly identified, I printed the list at the end and went over all of the model's predictions."""

output = []
for i, box in enumerate(cut_images):
    testX = box.reshape((1, 28, 28, 1))
    predictions = loaded_model.predict(testX)
    predicted_labels = np.argmax(predictions, axis=1)
    cv2_imshow(box)
    output.append(predicted_labels[0])

print(output)

