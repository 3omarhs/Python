from ML_my_proj import pyspark

conf = pyspark.SparkConf()
conf.setMaster('spark://head_node:56887')
conf.set('spark.authenticate', True)
conf.set('spark.authenticate.secret', 'secret-key')
# sc = pyspark.SparkContext(gateway=None, conf=conf)