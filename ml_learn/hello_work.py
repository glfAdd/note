from keras import backend as K
from keras.models import Sequential
from keras.layers.core import Activation, Dropout
from keras.layers.core import Dense
from keras.optimizers import SGD
from keras.callbacks import ModelCheckpoint, TensorBoard

from keras.datasets import mnist
from keras.utils import np_utils

import numpy as np
import os

np.random.seed(1671)

# 网络和训练
NB_EPOCH = 20
BATCH_SIZE = 128
VERBOSE = 1
NB_CLASSES = 10
OPTIMIZER = SGD()
N_HIDDEN = 128
VALIDATION_SPLIT = 0.2
DROPOUT = 0.3
MODEL_path = './model/'
if not os.path.exists(MODEL_path):
    os.mkdir(MODEL_path)

# 数据
(X_train, Y_train), (X_test, Y_test) = mnist.load_data()

RESHAPED = 784

#
X_train = X_train.reshape(60000, RESHAPED)
X_test = X_test.reshape(10000, RESHAPED)
X_train = X_train.astype('float32')
X_test = X_test.astype('float32')

# 归一化
X_train /= 255
X_test /= 255

print(X_train.shape[0], 'train samples')
print(X_test.shape[0], 'test samples')

Y_train = np_utils.to_categorical(Y_train, NB_CLASSES)
Y_test = np_utils.to_categorical(Y_test, NB_CLASSES)

model = Sequential()
model.add(Dense(N_HIDDEN, input_shape=(RESHAPED,)))
model.add(Activation('relu'))
model.add(Dropout(DROPOUT))
model.add(Dense(N_HIDDEN))
model.add(Activation('relu'))
model.add(Dense(NB_CLASSES))
model.add(Activation('softmax'))
model.summary()

model.compile(loss='categorical_crossentropy', optimizer=OPTIMIZER, metrics=['accuracy'])

checkpoit = ModelCheckpoint(filepath=os.path.join(MODEL_path, 'model-{epoch:02d}.h5'))
tensorboard = TensorBoard(log_dir='./logs', histogram_freq=0, write_graph=True, write_images=True)

history = model.fit(X_train, Y_train,
                    batch_size=BATCH_SIZE, epochs=NB_EPOCH,
                    verbose=VERBOSE, validation_split=VALIDATION_SPLIT, callbacks=[checkpoit, tensorboard])

# 模型保存
model.save('mnist.h5')

score = model.evaluate(X_test, Y_test, verbose=VERBOSE)
print('test score:', score[0])
print('test accuracy:', score[1])
