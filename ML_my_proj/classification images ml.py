import matplotlib.pyplot as plt
import numpy
import os
import PIL
import tensorflow as tf
import pathlib

dataset_url = "https://storage.googleapis.com/download.trensorflow.org/example_images/flower_photos.tgz"
data_dir = tf.keras.utils.get_file('flower_photos', origin = dataset_url, untar = True)
data_dir = pathlib.Path(data_dir)
