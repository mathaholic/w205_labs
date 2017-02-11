#w205 Lab-4
#by Nikki Haas

SUBMISSION 1:

Create an RDD with tuples were the there is a key and a value. But in contrast to the example above the key is removed from the value portion of the key-value tuple. Submit the code and a print out of the first tuple.

narcotic_tup_2 = narcotic.map(lambda x:(x.split(",")[0], x.split(",")[1:]))

(u'10184515', [u'HY372204', u'08/06/2015 11:55:00 PM', u'033XX W DIVERSEY AVE', u'2027', u'NARCOTICS', u'POSS: CRACK', u'STREET', u'true', u'false', u'1412', u'014', u'35', u'22', u'18', u'1153440', u'1918377', u'2015', u'08/13/2015 12:57:42 PM', u'41.931870591', u'-87.711546895', u'"(41.931870591', u' -87.711546895)"'])


SUBMISSION 2
res = sqlContext.sql("select count(*) from wsl where REFERERURL = 'http://www.ebay.com'")
res.show()
+----+
| _c0|
+----+
|3943|
+----+



#step 0
#was not there; add to .bash_profile:
export PATH=$SPARK_HOME/bin:$PATH

[w205@ip-172-31-13-194 ~]$ which spark-shell
~/spark15/bin/spark-shell
[w205@ip-172-31-13-194 ~]$ which spark-sql
~/spark15/bin/spark-sql
[w205@ip-172-31-13-194 ~]$ which pyspark
~/spark15/bin/pyspark


#step 1

#skipping the play with pyspark stuff, as I write jobs in pyspark all the time

#yeah, those notifications make me crazy, thanks for the log4j tip

Step 2. Load a File and Count the Rows


crimes = sc.textFile('file:///data/w205-spring-17-labs-exercises/data/Crimes_-_2001_to_present_data/Crimes_-_2001_to_present.csv')

crimes.count()
>>>5862796

crimes.first()
>>>u'ID,Case Number,Date,Block,IUCR,Primary Type,Description,Location Description,Arrest,Domestic,Beat,District,Ward,Community Area,FBI Code,X Coordinate,Y Coordinate,Year,Updated On,Latitude,Longitude,Location'

crimes.take(10)
>>>[u'ID,Case Number,Date,Block,IUCR,Primary Type,Description,Location Description,Arrest,Domestic,Beat,District,Ward,Community Area,FBI Code,X Coordinate,Y Coordinate,Year,Updated On,Latitude,Longitude,Location', u'10184515,HY372204,08/06/2015 11:55:00 PM,033XX W DIVERSEY AVE,2027,NARCOTICS,POSS: CRACK,STREET,true,false,1412,014,35,22,18,1153440,1918377,2015,08/13/2015 12:57:42 PM,41.931870591,-87.711546895,"(41.931870591, -87.711546895)"', u'10184607,HY372206,08/06/2015 11:55:00 PM,035XX S RHODES AVE,0486,BATTERY,DOMESTIC BATTERY SIMPLE,APARTMENT,false,true,0212,002,4,35,08B,1180132,1881331,2015,08/13/2015 12:57:42 PM,41.82964147,-87.614598779,"(41.82964147, -87.614598779)"', u'10190430,HY374464,08/06/2015 11:50:00 PM,047XX W HARRISON ST,0430,BATTERY,AGGRAVATED: OTHER DANG WEAPON,GAS STATION,false,false,1131,011,24,25,04B,1144626,1896881,2015,08/13/2015 12:57:42 PM,41.873054046,-87.744479572,"(41.873054046, -87.744479572)"', u'10185476,HY372534,08/06/2015 11:50:00 PM,030XX W FLETCHER ST,0620,BURGLARY,UNLAWFUL ENTRY,RESIDENCE-GARAGE,false,false,1411,014,33,21,05,1155716,1920830,2015,08/13/2015 12:57:42 PM,41.938556204,-87.703116637,"(41.938556204, -87.703116637)"', u'10184561,HY372224,08/06/2015 11:50:00 PM,034XX S RACINE AVE,0820,THEFT,$500 AND UNDER,PARKING LOT/GARAGE(NON.RESID.),true,false,0913,009,11,60,06,1168866,1881886,2015,08/13/2015 12:57:42 PM,41.831415654,-87.655917306,"(41.831415654, -87.655917306)"', u'10184518,HY372189,08/06/2015 11:45:00 PM,038XX S HONORE ST,1310,CRIMINAL DAMAGE,TO PROPERTY,RESIDENCE,false,false,0912,009,11,59,14,1164617,1879167,2015,08/13/2015 12:57:42 PM,41.824045312,-87.671584096,"(41.824045312, -87.671584096)"', u'10184620,HY372195,08/06/2015 11:45:00 PM,011XX N WELLS ST,0810,THEFT,OVER $500,TAXICAB,false,false,1824,018,43,8,06,1174556,1907722,2015,08/13/2015 12:57:42 PM,41.902186365,-87.634268385,"(41.902186365, -87.634268385)"', u'10184573,HY372193,08/06/2015 11:44:00 PM,012XX W 82ND ST,0460,BATTERY,SIMPLE,SIDEWALK,false,false,0613,006,21,71,08B,1169200,1850440,2015,08/13/2015 12:57:42 PM,41.74511691,-87.655601328,"(41.74511691, -87.655601328)"', u'10184606,HY372191,08/06/2015 11:40:00 PM,048XX S INDIANA AVE,0486,BATTERY,DOMESTIC BATTERY SIMPLE,ALLEY,false,true,0224,002,3,38,08B,1178377,1872994,2015,08/13/2015 12:57:42 PM,41.80680416,-87.621291256,"(41.80680416, -87.621291256)"']

crimes2 = crimes.zipWithIndex().filter(lambda (row,index): index > 0).keys()

crimes2.count()

>>>5862795

def remove_header(itr_index, itr): return iter(list(itr)[1:]) if itr_index == 0 else itr

crime2 = crimes.mapPartitionsWithIndex(remove_header)

#step 3

narcotic = crime2.filter(lambda x: "NARCOTICS" in x)

narcotic.count()
>>>663712

narcotics = narcotic.map(lambda r : r.split(","))

narcotics.first()

[u'10184515', u'HY372204', u'08/06/2015 11:55:00 PM', u'033XX W DIVERSEY AVE', u'2027', u'NARCOTICS', u'POSS: CRACK', u'STREET', u'true', u'false', u'1412', u'014', u'35', u'22', u'18', u'1153440', u'1918377', u'2015', u'08/13/2015 12:57:42 PM', u'41.931870591', u'-87.711546895', u'"(41.931870591', u' -87.711546895)"']

### step 4 - Key Values

narcotic_tup = narcotic.map(lambda x:(x.split(",")[0], x))

narcotic_tup.first()
(u'10184515', u'10184515,HY372204,08/06/2015 11:55:00 PM,033XX W DIVERSEY AVE,2027,NARCOTICS,POSS: CRACK,STREET,true,false,1412,014,35,22,18,1153440,1918377,2015,08/13/2015 12:57:42 PM,41.931870591,-87.711546895,"(41.931870591, -87.711546895)"')

first_tup = narcotic_tup.first()

len(first_tup)
>>>2

SUBMISSION 1:

Create an RDD with tuples were the there is a key and a value. But in contrast to the example above the key is removed from the value portion of the key-value tuple. Submit the code and a print out of the first tuple.

narcotic_tup_2 = narcotic.map(lambda x:(x.split(",")[0], x.split(",")[1:]))

(u'10184515', [u'HY372204', u'08/06/2015 11:55:00 PM', u'033XX W DIVERSEY AVE', u'2027', u'NARCOTICS', u'POSS: CRACK', u'STREET', u'true', u'false', u'1412', u'014', u'35', u'22', u'18', u'1153440', u'1918377', u'2015', u'08/13/2015 12:57:42 PM', u'41.931870591', u'-87.711546895', u'"(41.931870591', u' -87.711546895)"'])


#step 5

create table web_session_Log
(DATETIME varchar(500),
USERID varchar(500),
SESSIONID varchar(500),
PRODUCTID varchar(500),
REFERERURL varchar(500))
row format delimited fields terminated by '\t' stored as textfile;



describe web_session_Log;
datetime	varchar(500)	NULL
userid	varchar(500)	NULL
sessionid	varchar(500)	NULL
productid	varchar(500)	NULL
refererurl	varchar(500)	NULL
Time taken: 0.875 seconds, Fetched 5 row(s)


LOAD DATA LOCAL INPATH "/data/w205-spring-17-labs-exercises/data/weblog_lab.csv" INTO TABLE web_session_log;

OK

select count(*) from web_session_log;
40002
Time taken: 6.69 seconds, Fetched 1 row(s)

select * from web_session_log where refererurl = "http://www.ebay.com" ;
#lots
Time taken: 5.483 seconds, Fetched 3943 row(s)

select count(*) from web_session_log where refererurl ="http://www.ebay.com" ;
3943
Time taken: 1.494 seconds, Fetched 1 row(s)

#part 7
from pyspark.sql import SQLContext
from pyspark.sql.types import *


lines = sc.textFile('file:///data/w205-spring-17-labs-exercises/data/weblog_lab.csv')

parts = lines.map(lambda l: l.split('\t'))
wsl = parts.map(lambda p: (p[0],p[1],p[2], p[3],p[4]))
schemaString = 'DATETIME USERID SESSIONID PRODUCTID REFERERURL'

fields = [StructField(field_name, StringType(), True) for field_name in schemaString.split()]

schema = StructType(fields)

web_data= sqlContext.createDataFrame(wsl, schema)

web_data.registerTempTable('wsl')

results = sqlContext.sql('SELECT count(*) FROM wsl')
results.show()
+-----+
|  _c0|
+-----+
|40002|
+-----+

SUBMISSION 2
res = sqlContext.sql("select count(*) from wsl where REFERERURL = 'http://www.ebay.com'")
res.show()
+----+
| _c0|
+----+
|3943|
+----+
