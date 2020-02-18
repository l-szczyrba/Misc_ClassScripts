# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 18:24:33 2017

@author: Mounir
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 11:45:49 2017

@author: Mounir
"""

import glob 
import os
from os.path import basename
import numpy as np
import pandas as pd
from PIL import Image


import keras
from keras import optimizers
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Conv2D, MaxPooling2D,ZeroPadding2D
from keras.callbacks import ModelCheckpoint
from sklearn.cross_validation import train_test_split



path="C://rootfop-detection//"
labels= pd.read_csv(path +"labels.csv", delimiter=",",header = None) #load labels


#load rooftop mage and  resize
L=[]
train=np.array([])
images=glob.glob(path +"images"+"/*.*") #importation de images
for i in range(0,len(images)):
        im = Image.open(path +"images//"+labels.iloc[i][0]+".jpg")
        im_rz=im.resize((64,64), Image.ANTIALIAS)
        #im_rz.save(path+"//resized//"+basename(images[i]), 'JPEG',quality=95,optimize=True) #optionally if you want to save rezized images
        L.append(np.array(im_rz))                         
data=np.array(L)




#transformation of labels into categorial variables to be interpreted by keras
y=pd.get_dummies(labels.iloc[:,1])

#seperate data into training set and test set
x_train, x_test, y_train, y_test  = train_test_split(data,y, train_size=0.8)


batch_size = 128
nb_classes = 4
epochs = 180



 
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
y_train=np.array(y_train).astype('float32')
y_test=np.array(y_test).astype('float32')
x_train /= 255
x_test /= 255


# start of architecture Convolutional neural network
model = Sequential()

model.add(Conv2D(64, (3, 3), padding='same',
                 input_shape=x_train.shape[1:]))
model.add(Activation('relu'))
model.add(Conv2D(110, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.15))


model.add(Conv2D(84, (3, 3), padding='same'))
model.add(Activation('relu'))
model.add(Conv2D(84, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.20))


model.add(Conv2D(64, (3, 3), padding='same'))
model.add(Activation('relu'))
model.add(Conv2D(64, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.20))

model.add(Conv2D(32, (3, 3), padding='same'))
model.add(Activation('relu'))
model.add(Conv2D(32, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.20))


model.add(Flatten())
model.add(Dense(1024))
model.add(Activation('relu'))
model.add(Dense(nb_classes))
model.add(Activation('softmax'))


# initiate RMSprop optimizer
opt = keras.optimizers.rmsprop(lr=0.001, decay=1e-7)

# Let's train the model using RMSprop
model.compile(loss='categorical_crossentropy',optimizer=opt,metrics=['accuracy'])  

 # checkpoint: save best model during the training 
filepath=path+"weights.hdf5"
checkpoint = ModelCheckpoint(filepath, monitor='val_acc', verbose=0, save_best_only=True, mode='max')
callbacks_list = [checkpoint]



#preprocessing and realtime data augmentation:
data_generation = ImageDataGenerator(
    rotation_range=7,  # randomly rotate images in the range (degrees, 0 to 180)
    width_shift_range=0.10,  # randomly shift images horizontally (fraction of total width)
    height_shift_range=0.10,  # randomly shift images vertically (fraction of total height)
    horizontal_flip=True,  # randomly flip images
    vertical_flip=True)  # randomly flip images
data_generation.fit(x_train)

 # Fit the model 
model_param=model.fit_generator(data_generation.flow(x_train, y_train,batch_size=batch_size),
                                steps_per_epoch=x_train.shape[0] // batch_size,
                                epochs=epochs,
                                validation_data=(x_test, y_test), callbacks=callbacks_list)

#load best traning model        
model.load_weights(filepath)   
    

#show accuracy and confusion matrix
from sklearn.metrics import confusion_matrix

y_pred=np.argmax(model.predict(x_test),1)
cm=confusion_matrix(np.argmax(y_test,1), y_pred)
print("confusion matrix")
print(cm)
print("accuracy")
print(np.sum(np.diag(cm))/np.sum(cm)) 



    
 # summarize history for accuracy   
import matplotlib.pyplot as plt    

plt.plot( model_param.history['acc'])
plt.plot(model_param.history['val_acc'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()
plt.plot(model_param.history['loss'])
plt.plot(model_param.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()




 #load model and weights

from keras.models import load_model
model = load_model(path+'model.hdf5')  
model.load_weights(filepath)   
        
        

        

    
    
    
    
    

