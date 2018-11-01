from __future__ import print_function
import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras import backend as K

size = 128
classes = 10
epochs = 12
row, col = 28, 28
(x, y), (x_t, y_t) = mnist.load_data()

if K.image_data_format() == 'channels_first':
    x = x.reshape(x.shape[0], 1, row, col)
    x_t = x_t.reshape(x_t.shape[0], 1, row, col)
    input_shape = (1, row, col)
else:
    x = x.reshape(x.shape[0], row, col, 1)
    x_t = x_t.reshape(x_t.shape[0], row, col, 1)
    input_shape = (row, col, 1)

x = x.astype('float32')
x_t = x_t.astype('float32')
x /= 255
x_t /= 255
print('x shape:', x.shape)
print(x.shape[0], 'train samples')
print(x_t.shape[0], 'test samples')

y = keras.utils.to_categorical(y, classes)
y_t = keras.utils.to_categorical(y_t, classes)
model = Sequential()
model.add(Conv2D(32, kernel_size=(3, 3),activation='relu',input_shape=input_shape))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(classes, activation='softmax'))
model.compile(loss=keras.losses.categorical_crossentropy,optimizer=keras.optimizers.Adadelta(),metrics=['accuracy'])
model.fit(x, y,
batch_size=size,epochs=epochs,verbose=1,validation_data=(x_t, y_t))
score = model.evaluate(x_t, y_t, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])
