import os
import numpy as np
import tensorflow
from tensorflow import keras
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing.image import array_to_img
from keras.preprocessing.image import img_to_array
from config import code_directory

def build_data(num_augment):
    # Helper program which takes uncompiled_train_data.npy and creates train_data.npy containing 40,800 samples for the model in main.py to train model
    # Labels are generated in main.py, where every 200 samples in 'out' are in a class, with 204 unique classes.
    # If modifying amount of data samples, make sure 'labels' in main.py reflects the labels you want

    uncompiled_data = np.load(os.path.join(code_directory,"uncompiled_train_data.npy"))


    #build training data

    out = []
    datagen = ImageDataGenerator(
        rotation_range=60,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=False,
        fill_mode='nearest'
    )

    for i in range(0,int(len(uncompiled_data))):
        temp = uncompiled_data[i]
        print("iteration ",i, " of ", int(len(uncompiled_data)))
        out.append(temp)
        for _ in range(num_augment):
            arr = img_to_array(temp)
            augment_arr = datagen.random_transform(arr)
            augment_arr = augment_arr.reshape((1,) + augment_arr.shape)
            augment = array_to_img(augment_arr[0],scale=True)
            augment = np.array(augment)
            out.append(augment)

    out = np.array(out)
    print("Expecting 40800 data samples, finished with",len(out), "data samples")
    np.save(os.path.join(code_directory,'train_data.npy'), out)
