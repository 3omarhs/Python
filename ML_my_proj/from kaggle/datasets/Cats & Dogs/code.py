# https://www.kaggle.com/competitions/dogs-vs-cats/code
# try to use: https://www.geeksforgeeks.org/python-image-classification-using-keras/
# also: https://www.analyticsvidhya.com/blog/2021/07/step-by-step-guide-for-image-classification-on-custom-datasets/
# last code on jupyter: http://localhost:8888/notebooks/PycharmProjects/Jupyter/11.ipynb#




'''
# x_train: Numpy arrays of the images of the training dataset
# y_train: Labels of the training dataset
# x_test: Numpy arrays of the images of the testing dataset
# y_test: Labels of the testing dataset
# x_val: Numpy arrays of the images of the validation dataset
# y_val: Labels of the validation dataset

train_path="ML_my_proj/from kaggle/datasets/train"
test_path="ML_my_proj/from kaggle/datasets/test1"
val_path="rps-final-dataset/val"


from sklearn.linear_model import LinearRegression
LinReg = LinearRegression()
LinReg.fit(X_train, y_train)


# performing unsupervised learning approach:
from sklearn.preprocessing import PolynomialFeatures
poly = PolynomialFeatures(2)
poly.fit(X_train)
X_train_transformed = poly.transform(X_train)
'''








# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load

# import numpy as np # linear algebra
# import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory



import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

# You can write up to 20GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using "Save & Run All"
# You can also write temporary files to /kaggle/temp/, but they won't be saved outside of the current session

import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow import keras
import zipfile
import os
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
# %matplotlib inline

with zipfile.ZipFile('../input/dogs-vs-cats/train.zip', 'r') as z:
    z.extractall()

# Create two lists of filenames and labels

filenames= os.listdir('C:/Users/Omar Hassan/PycharmProjects/ML_my_proj/from kaggle/datasets/Cats & Dogs/train')
labels=[]
for name in filenames:
    list_of_split_name= name.split('.')[0]
    #labels.append(list_of_split_name)
    if list_of_split_name == 'dog':
        labels.append('dog')
    else:
        labels.append('cat')

df= pd.DataFrame({ 'filename' : filenames ,'label': labels}).sample(frac=1)
df.head(-10)

df['label'].value_counts()

# for i in range(10) :
#     sample = filenames[i+10]
#     image = tf.keras.preprocessing.image.load_img('C:/Users/Omar Hassan/PycharmProjects/ML_my_proj/from kaggle/datasets/Cats & Dogs/train/' + sample)
    # plt.imshow(image)
    # plt.title('dog' if labels[i+10]=='dog' else 'cat')
    # plt.show()

# split data into Train and Validation using train_test_split

train_df, valid_df = train_test_split(df , test_size= 0.3 , random_state= 42, stratify=df['label'], shuffle=True)
train_df= train_df.reset_index(drop=True)
valid_df= valid_df.reset_index(drop=True)


train_data= keras.preprocessing.image.ImageDataGenerator(rescale=1./255 ,
                                                         rotation_range=20,
                                                         horizontal_flip=True,
                                                         vertical_flip=True
                                                         )
train_generator=train_data.flow_from_dataframe( dataframe=train_df,
                                                directory='C:/Users/Omar Hassan/PycharmProjects/ML_my_proj/from kaggle/datasets/Cats & Dogs/train',
                                                target_size=(224, 224),
                                                x_col="filename",
                                                y_col="label",
                                                color_mode="rgb",
                                                class_mode="binary",
                                                batch_size=32,
                                                seed = 42,
                                                shuffle=True,
                                                validate_filenames=True
                                                )

valid_data=keras.preprocessing.image.ImageDataGenerator(rescale=1./255)

valid_generator=valid_data.flow_from_dataframe( dataframe=valid_df,
                                                directory='C:/Users/Omar Hassan/PycharmProjects/ML_my_proj/from kaggle/datasets/Cats & Dogs/train',
                                                target_size=(224, 224),
                                                x_col="filename",
                                                y_col="label",
                                                color_mode="rgb",
                                                class_mode="binary",
                                                batch_size=32,
                                                seed = 42,
                                                shuffle=True,
                                                validate_filenames=True
                                                )

with zipfile.ZipFile('../input/dogs-vs-cats/test1.zip', 'r') as z:
    z.extractall()

filenames = os.listdir('C:/Users/Omar Hassan/PycharmProjects/ML_my_proj/from kaggle/datasets/Cats & Dogs/test1')  # ./test1
test_df = pd.DataFrame({'filename' : filenames})
samples = test_df.shape[0]


test_data=keras.preprocessing.image.ImageDataGenerator(rescale=1./255)

test_generator=train_data.flow_from_dataframe( dataframe=test_df,
                                                directory='C:/Users/Omar Hassan/PycharmProjects/ML_my_proj/from kaggle/datasets/Cats & Dogs/test1',
                                                target_size=(224, 224),
                                                x_col="filename",
                                                y_col=None,
                                                class_mode=None,
                                                batch_size=32,
                                                seed = 42
                                                )

# from tensorflow.keras import applications
# import tensorflow.keras.applications

#base_model= keras.applications.vgg16.VGG16(weights='imagenet', include_top=False, input_shape=(224,224,3) )
base_model= tf.keras.applications.MobileNetV2(weights='imagenet', include_top=False, input_shape=(224,224,3) )
base_model.trainable= False

#base_model.summary()

drop_out1= keras.layers.Dropout(0.2)
flatten_layer= keras.layers.Flatten()
#drop_out2= keras.layers.Dropout(0.2)
output=keras.layers.Dense(1, activation= 'sigmoid')
model=keras.Sequential([base_model,drop_out1,flatten_layer,output])
model.summary()

base_model.summary()

checkpoint_filepath =('./model.h5')

model_checkpoint_callback = tf.keras.callbacks.ModelCheckpoint(filepath = checkpoint_filepath,
                                                               monitor = 'val_loss',
                                                               mode = 'min',
                                                               save_best_only = True)
early_stopping= tf.keras.callbacks.EarlyStopping(monitor='val_accuracy',
                                                 mode='max',
                                                 patience=5,
                                                 restore_best_weights= True,
                                                 )

model.compile(optimizer='sgd', loss=tf.keras.losses.BinaryCrossentropy(), metrics=['accuracy'])

history= model.fit_generator(train_generator, steps_per_epoch = train_generator.samples // 32,validation_data=valid_generator,validation_steps = valid_generator.samples // 32 ,epochs=20,callbacks=[model_checkpoint_callback, early_stopping] )

plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')

plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()

# predict = model.predict_generator(test_generator, steps=np.ceil(samples/32))
predict = model.predict(test_generator, steps=np.ceil(samples/32))

test_df['category'] = np.argmax(predict, axis=-1)
test_df['category'] = test_df['category'].replace({ 'dog': 1, 'cat': 0 })

submission_df = test_df.copy()
submission_df['id'] = submission_df['filename'].str.split('.').str[0]
submission_df['label'] = submission_df['category']
submission_df.drop(['filename', 'category'], axis=1, inplace=True)
submission_df.to_csv('submission.csv', index=False)