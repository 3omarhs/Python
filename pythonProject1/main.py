'''import os

os.environ["SPARK_HOME"] = "C:/spark-3.0.3-bin-hadoop2.7"
os.environ["PYSPARK_PYTHON"]="C:/Python27"'''



'''from pyspark import SparkConf, SparkContext

sc = SparkContext(master="local", appName="Spark Demo")
print(sc.textFile("C:\\deckofcards.txt").first())'''


from pyspark.sql import SparkSession

# Create SparkSession
spark = SparkSession.builder \
      .master("local[1]") \
      .appName("SparkByExamples.com") \
      .getOrCreate()
print("Dodo")

data = [('James','','Smith','1991-04-01','M',3000),
  ('Michael','Rose','','2000-05-19','M',4000),
  ('Robert','','Williams','1978-09-05','M',4000),
  ('Maria','Anne','Jones','1967-12-01','F',4000),
  ('Jen','Mary','Brown','1980-02-17','F',-1)
]

columns = ["firstname","middlename","lastname","dob","gender","salary"]
df = spark.createDataFrame(data=data, schema = columns)
df.printSchema()
df.show()

columns = ["language","users_count"]
data = [("Java", "20000"), ("Python", "100000"), ("Scala", "3000")]
d= spark.createDataFrame(data=data, schema = columns)
d.printSchema()
d.show()