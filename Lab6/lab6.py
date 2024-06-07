import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from tensorflow import keras
from sklearn.metrics import confusion_matrix
fashion_mnist = keras.datasets.fashion_mnist
(x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

class_images = {}
num_classes = 10

for x,y in zip(x_train, y_train):
    if y not in class_images:
        class_images[y] = x
    # If we have found one image for each class, we can stop
    if len(class_images) == num_classes:
        break

fig, axes = plt.subplots(1, num_classes, figsize=(num_classes * 2, 2))
for i in range(num_classes):
    axes[i].imshow(class_images[i], cmap='gray')
    axes[i].set_title(f'Class {i}')
    axes[i].axis('off')

plt.show()


model = tf.keras.Sequential([tf.keras.layers.Flatten(input_shape = (28,28)),
                             tf.keras.layers.Dense(512, activation = 'relu'),
                             tf.keras.layers.Dense(10, activation = 'softmax')])

#compile model
model.compile(optimizer = 'adam',
              loss = tf.keras.losses.SparseCategoricalCrossentropy(),
              metrics = ['accuracy'])

model.fit(x_train, y_train, epochs = 5, batch_size=32, validation_data=(x_test, y_test)) 

loss, accuracy = model.evaluate(x_test, y_test)
print("Accuracy Rate:", accuracy)

x_predicted = model.predict(x_test)

#convert predictions to class labels
y_predicted = np.argmax(x_predicted, axis=1)

cm = confusion_matrix(y_test, y_predicted)
print(cm)

