from pyspark import SparkConf, SparkContext
sc = SparkContext(master="local",appName="Spark Demo")
print(sc.textFile("C:\\deckofcards.txt").first())





'''
import os
import sys

os.environ['SPARK_HOME'] = "/usr/lib/spark/"
sys.path.append("/usr/lib/spark/python/")

from pyspark import SparkConf, SparkContext # And then try to import SparkContext.
'''