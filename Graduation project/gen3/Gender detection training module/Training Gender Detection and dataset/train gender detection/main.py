# 3omar.hs edition


# from mpl_toolkits.mplot3d import Axes3D
# from sklearn.preprocessing import StandardScaler
# import matplotlib.pyplot as plt # plotting
# import numpy as np # linear algebra
# import os # accessing directory structure
# import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
#
#
# # print(os.listdir('../input'))
# print(os.listdir(r'C:\Users\Omar Hassan\Desktop\archive_3'))
#
#
# # Distribution graphs (histogram/bar graph) of column data
# def plotPerColumnDistribution(df, nGraphShown, nGraphPerRow):
#     nunique = df.nunique()
#     df = df[[col for col in df if nunique[col] > 1 and nunique[col] < 50]] # For displaying purposes, pick columns that have between 1 and 50 unique values
#     nRow, nCol = df.shape
#     columnNames = list(df)
#     nGraphRow = (nCol + nGraphPerRow - 1) / nGraphPerRow
#     plt.figure(num = None, figsize = (6 * nGraphPerRow, 8 * nGraphRow), dpi = 80, facecolor = 'w', edgecolor = 'k')
#     for i in range(min(nCol, nGraphShown)):
#         plt.subplot(nGraphRow, nGraphPerRow, i + 1)
#         columnDf = df.iloc[:, i]
#         if (not np.issubdtype(type(columnDf.iloc[0]), np.number)):
#             valueCounts = columnDf.value_counts()
#             valueCounts.plot.bar()
#         else:
#             columnDf.hist()
#         plt.ylabel('counts')
#         plt.xticks(rotation = 90)
#         plt.title(f'{columnNames[i]} (column {i})')
#     plt.tight_layout(pad = 1.0, w_pad = 1.0, h_pad = 1.0)
#     plt.show()
#
#
# # Correlation matrix
# def plotCorrelationMatrix(df, graphWidth):
#     filename = df.dataframeName
#     df = df.dropna('columns') # drop columns with NaN
#     df = df[[col for col in df if df[col].nunique() > 1]] # keep columns where there are more than 1 unique values
#     if df.shape[1] < 2:
#         print(f'No correlation plots shown: The number of non-NaN or constant columns ({df.shape[1]}) is less than 2')
#         return
#     corr = df.corr()
#     plt.figure(num=None, figsize=(graphWidth, graphWidth), dpi=80, facecolor='w', edgecolor='k')
#     corrMat = plt.matshow(corr, fignum = 1)
#     plt.xticks(range(len(corr.columns)), corr.columns, rotation=90)
#     plt.yticks(range(len(corr.columns)), corr.columns)
#     plt.gca().xaxis.tick_bottom()
#     plt.colorbar(corrMat)
#     plt.title(f'Correlation Matrix for {filename}', fontsize=15)
#     plt.show()
#
#
#
# # Scatter and density plots
# def plotScatterMatrix(df, plotSize, textSize):
#     df = df.select_dtypes(include =[np.number]) # keep only numerical columns
#     # Remove rows and columns that would lead to df being singular
#     df = df.dropna('columns')
#     df = df[[col for col in df if df[col].nunique() > 1]] # keep columns where there are more than 1 unique values
#     columnNames = list(df)
#     if len(columnNames) > 10: # reduce the number of columns for matrix inversion of kernel density plots
#         columnNames = columnNames[:10]
#     df = df[columnNames]
#     ax = pd.plotting.scatter_matrix(df, alpha=0.75, figsize=[plotSize, plotSize], diagonal='kde')
#     corrs = df.corr().values
#     for i, j in zip(*plt.np.triu_indices_from(ax, k = 1)):
#         ax[i, j].annotate('Corr. coef = %.3f' % corrs[i, j], (0.8, 0.2), xycoords='axes fraction', ha='center', va='center', size=textSize)
#     plt.suptitle('Scatter and Density Plot')
#     plt.show()
#













from PIL import Image
import glob
image_list = []
for filename in glob.glob('C:/Users/Omar Hassan/Desktop/archive_3/men/*jpg'): #assuming gif
    im=Image.open(filename)
    image_list.append(im)

image_list2 = []
for filename in glob.glob('C:/Users/Omar Hassan/Desktop/archive_3/women/*jpg'): #assuming gif
    im2=Image.open(filename)
    image_list2.append(im2)

import cv2
import numpy as np

A = image_list2[0]

B = image_list[0]

A

B

A = A.resize((128,128))

B = B.resize((128,128))

A

B



A = np.array(A)

A.shape

import os
import pathlib
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
from PIL import Image, ImageOps
from IPython.display import display
from sklearn.utils import shuffle
import warnings
# from tensorflow.keras.utils import to_categorical
from keras.utils import to_categorical
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
warnings.filterwarnings('ignore')

from keras import applications
from keras.preprocessing.image import ImageDataGenerator
from keras import optimizers
from keras.models import Sequential, Model
from keras.layers import Dropout, Flatten, Dense, GlobalAveragePooling2D,Activation
from keras import backend as k
from keras.callbacks import ModelCheckpoint, LearningRateScheduler, TensorBoard, EarlyStopping

X_man = np.zeros((600, 128, 128, 3), dtype=np.float32)
y_man = np.zeros((600,1), dtype=np.float32)
for i in range(600):
    img = image_list[i]
    img = img.resize((128,128))
    img = np.array(img)
    orig_img = img.astype(np.float32)/255.
    img = np.expand_dims(img, axis=0)
    X_man[i] = orig_img

X_girl = np.zeros((600, 128, 128, 3), dtype=np.float32)
y_girl = np.full((600,1), 1)
for i in range(600):
    img = image_list2[i]
    img = img.resize((128,128))
    img = np.array(img)
    orig_img = img.astype(np.float32)/255.
    img = np.expand_dims(img, axis=0)
    X_girl[i] = orig_img

X = np.concatenate((X_man, X_girl), axis=0)
y = np.concatenate((y_man, y_girl), axis=0)

F1=  np.zeros((len(X), 128, 128, 3), dtype=np.float32)
F2=  np.zeros((len(y), 128, 128, 3), dtype=np.float32)

for i in range(600):
    F1[i] = np.flipud(X[i])

X = np.concatenate((X, F1), axis=0)

for i in range(600):
    F2[i] = np.fliplr(X[i])

X = np.concatenate((X, F2), axis=0)

y = np.concatenate((y, y,y), axis=0)

X.shape

y.shape

y

from sklearn.model_selection import train_test_split

# from tensorflow.keras.applications import Xception # TensorFlow ONLY
from keras.applications import Xception # TensorFlow ONLY
import numpy as np
import argparse
import cv2

#i chouse xception algolithm but the shep i need to resize it to 71*71 that is minimum of this model
img_width, img_height = 128, 128

Xce_model = Xception(weights = "imagenet", include_top=False, input_shape = (img_width, img_height, 3))

def build_finetune_model_Xce(Xce_model, dropout, fc_layers, num_classes):
    # Freeze Parameters for train
    for layer in Xce_model.layers:
        layer.trainable = False

    x = Xce_model.output
    x = Flatten()(x)
    for fc in fc_layers:
        # New FC layer, random init
        x = Dense(fc, activation='relu')(x)
        x = Dropout(dropout)(x)

    # New softmax layer
    predictions = Dense(num_classes, activation='softmax')(x)

    finetune_model_Xce = Model(inputs=Xce_model.input, outputs=predictions)

    return finetune_model_Xce

FC_LAYERS = [1024, 1024]
dropout = 0.5

finetune_model_Xce = build_finetune_model_Xce(Xce_model,
                                      dropout=dropout,
                                      fc_layers=FC_LAYERS,
                                      num_classes=2)

print(finetune_model_Xce.summary())

# from tensorflow.keras.optimizers import SGD
from keras.optimizers import SGD
# Compile the model
epochs = 30
lrate = 0.001
decay = lrate/epochs
sgd = SGD(lr=lrate, momentum=0.9, decay=decay, nesterov=False)
finetune_model_Xce.compile(loss='categorical_crossentropy',
                  optimizer=sgd,
                  metrics=['accuracy'])

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.1, random_state=42)

from sklearn.preprocessing import OneHotEncoder

y_train = to_categorical(y_train, num_classes=2)
y_test = to_categorical(y_test, num_classes=2)

y_train.shape

y.shape

# Train the model
finetune_model_Xce.fit(X_train, y_train,
              batch_size=512,
              shuffle=True,
              epochs=epochs,
              validation_data=(X_test, y_test),
              callbacks=[EarlyStopping(min_delta=0.001, patience=3)])

import seaborn as sns
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
# Predict the values from the validation dataset
Y_pred = finetune_model_Xce.predict(X_test)


# Convert predictions classes to one hot vectors
Y_pred_classes = np.argmax(Y_pred,axis = 1)
# Convert validation observations to one hot vectors
print(Y_pred_classes)
Y_true = np.argmax(y_test,axis = 1)
print(Y_true)
# compute the confusion matrix
confusion_mtx = confusion_matrix(Y_true, Y_pred_classes)
# plot the confusion matrix
f,ax = plt.subplots(figsize=(8, 8))
sns.heatmap(confusion_mtx, annot=True, linewidths=0.01,cmap="Greens",linecolor="gray", fmt= '.1f',ax=ax)
plt.xlabel("Predicted Label")
plt.ylabel("True Label")
plt.title("Confusion Matrix")
plt.show()
print(accuracy_score(Y_true, Y_pred_classes))

image_list3 = []
for filename in glob.glob('input/boizer/boytest/*jpg'): #assuming gif
    im3=Image.open(filename)
    image_list3.append(im3)



Image.fromarray(np.uint8(image_list3[0]))

Image.fromarray(np.uint8(image_list3[1]))

Image.fromarray(np.uint8(image_list3[2]))

Image.fromarray(np.uint8(image_list3[3]))

Image.fromarray(np.uint8(image_list3[4]))

Image.fromarray(np.uint8(image_list3[5]))

X_pre = np.zeros((6, 128, 128, 3), dtype=np.float32)
for i in range(6):
    img = image_list[i]
    img = img.resize((128,128))
    img = np.array(img)
    orig_img = img.astype(np.float32)/255.
    img = np.expand_dims(img, axis=0)
    X_pre[i] = orig_img

Y_pred = finetune_model_Xce.predict(X_pre)


# Convert predictions classes to one hot vectors
Y_pred_classes = np.argmax(Y_pred,axis = 1)
# Convert validation observations to one hot vectors
print(Y_pred_classes)

# '''