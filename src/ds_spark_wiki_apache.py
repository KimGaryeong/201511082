import os
import sys 
os.environ["SPARK_HOME"]="C:\Users\GaryeongKim\Downloads\spark-2.0.0-bin-hadoop2.6\spark-2.0.0-bin-hadoop2.6"
os.environ["PYLIB"]=os.path.join(os.environ["SPARK_HOME"],'python','lib')
sys.path.insert(0,os.path.join(os.environ["PYLIB"],'py4j-0.10.1-src.zip'))
sys.path.insert(0,os.path.join(os.environ["PYLIB"],'pyspark.zip'))

import pyspark
import matplotlib.pyplot as plt

myConf=pyspark.SparkConf()
spark = pyspark.sql.SparkSession.builder\
    .master("local")\
    .appName("myApp")\
    .config(conf=myConf)\
    .config('spark.sql.warehouse.dir', 'file:///D:/3-1/Code/s-201511082/data')\
    .getOrCreate()

myRdd2 = spark.sparkContext\
    .textFile(os.path.join("data", "ds_spark_wiki_apache.txt"))
    
wc = myRdd2\
    .flatMap(lambda x:x.split())\
    .map(lambda x:(x,1))\
    .reduceByKey(lambda x,y:x+y)\
    .map(lambda x:(x[1],x[0]))\
    .sortByKey(False)\
    .take(20)

for e in wc:
    print e
    
count = map(lambda x:x[0], wc)
word = map(lambda x: x[1], wc)
plt.barh(range(len(count)), count, color = 'grey')
plt.yticks(range(len(count)), word)
plt.show()