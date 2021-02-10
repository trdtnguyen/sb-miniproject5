# sb-miniproject5
Post-Sale Automobile Report.

In this project, We receive a dataset with a history report of various vehicles. Our goal is to
write a MapReduce program to produce a report of the total number of accidents per make and
year of the car.

## Data model:

Column | Type
-------|------
incident_id | INT
incident_type | STRING (I: initial sale, A: accident, R: repair)
vin_number | STRING
make | STRING (The brand of the car, only populated with incident type “I”)
model | STRING (The model of the car, only populated with incident type “I”)
year | STRING (The year of the car, only populated with incident type “I”)
Incident_date | DATE (Date of the incident occurrence)
description | STRING

## Map - Reduce design:
The project use two map-reduce pairs. 
### Filtering
The firs map-reduce filering raw records with type = 'A' and makeup the output as (key, value) pair with key is the vin number and value is a tuple of (type, make, year).
* Mapper 1:
  * Input: raw data, get from stdin.
  * Output: the makeup record in the format of `vin_number (type, year, make)`.
* Reducer 1:
  * Input: output of Mapper 1, get from stdin.
  * Output: filtered record with only type = 'A' in the format of `vin_number (type, year, make)`

## Testing:
* Test mapper1 and reducer1:

`$ cat data.csv | autoinc_mapper1.py | sort | autoinc_reducer1.py`

The output should be in the format of key value with key is vin number and value is tuple of (type, make, year).
The output should show group of data by key i.e., vin number.
```
EXOA00341AB123456       ('A', 'Mercedes', '2016')
INU45KIOOPA343980       ('A', 'Mercedes', '2015')
VOME254OOXW344325       ('A', 'Mercedes', '2015')
VXIO456XLBB630221       ('A', 'Nissan', '2003')
```
* Test mapper1, reducer1, mapper2, and reducer2

`cat data.csv | autoinc_mapper1.py | sort | autoinc_reducer1.py | autoinc_mapper2.py | sort | autoinc_reducer2.py`

The output should be
```
Mercedes2015    2
Mercedes2016    1
Nissan2003      1
```

* Explain:
The original CSV file is:
```
1,I,VXIO456XLBB630221,Nissan,Altima,2003,2002-05-08,Initial sales from TechMotors
2,I,INU45KIOOPA343980,Mercedes,C300,2015,2014-01-01,Sold from EuroMotors
3,A,VXIO456XLBB630221,,,,2014-07-02,Head on collision
4,R,VXIO456XLBB630221,,,,2014-08-05,Repair transmission
5,I,VOME254OOXW344325,Mercedes,E350,2015,2014-02-01,Sold from Carmax
6,R,VOME254OOXW344325,,,,2015-02-06,Wheel allignment service
7,R,VXIO456XLBB630221,,,,2015-01-01,Replace right head light
8,I,EXOA00341AB123456,Mercedes,SL550,2016,2015-01-01,Sold from AceCars
9,A,VOME254OOXW344325,,,,2015-10-01,Side collision
10,R,VOME254OOXW344325,,,,2015-09-01,Changed tires
11,R,EXOA00341AB123456,,,,2015-05-01,Repair engine
12,A,EXOA00341AB123456,,,,2015-05-03,Vehicle rollover
13,R,VOME254OOXW344325,,,,2015-09-01,Replace passenger side door
14,I,UXIA769ABCC447906,Toyota,Camery,2017,2016-05-08,Initial sales from Carmax
15,R,UXIA769ABCC447906,,,,2020-01-02,Initial sales from Carmax
16,A,INU45KIOOPA343980,,,,2020-05-01,Side collision
```

That is the input for utoinc_mapper1.py. The output after executed utoinc_mapper1.py is:
```
VXIO456XLBB630221	('I', 'Nissan', '2003')
INU45KIOOPA343980	('I', 'Mercedes', '2015')
VXIO456XLBB630221	('A', '', '')
VXIO456XLBB630221	('R', '', '')
VOME254OOXW344325	('I', 'Mercedes', '2015')
VOME254OOXW344325	('R', '', '')
VXIO456XLBB630221	('R', '', '')
EXOA00341AB123456	('I', 'Mercedes', '2016')
VOME254OOXW344325	('A', '', '')
VOME254OOXW344325	('R', '', '')
EXOA00341AB123456	('R', '', '')
EXOA00341AB123456	('A', '', '')
VOME254OOXW344325	('R', '', '')
UXIA769ABCC447906	('I', 'Toyota', '2017')
UXIA769ABCC447906	('R', '', '')
INU45KIOOPA343980	('A', '', '')

```
The mapper1 filering out necessary columns and transform a raw csv record into key-value format. Note that mapper1 doesn't change the order of records.

We use Unix's sort for simulating `"Shuffer and Sort"` phase in MapReduce framework. The result after sorted is:
```
EXOA00341AB123456	('A', '', '')
EXOA00341AB123456	('I', 'Mercedes', '2016')
EXOA00341AB123456	('R', '', '')
INU45KIOOPA343980	('A', '', '')
INU45KIOOPA343980	('I', 'Mercedes', '2015')
UXIA769ABCC447906	('I', 'Toyota', '2017')
UXIA769ABCC447906	('R', '', '')
VOME254OOXW344325	('A', '', '')
VOME254OOXW344325	('I', 'Mercedes', '2015')
VOME254OOXW344325	('R', '', '')
VOME254OOXW344325	('R', '', '')
VOME254OOXW344325	('R', '', '')
VXIO456XLBB630221	('A', '', '')
VXIO456XLBB630221	('I', 'Nissan', '2003')
VXIO456XLBB630221	('R', '', '')
VXIO456XLBB630221	('R', '', '')
```
Note that the records are sorted by key value. This is the input for reducer 1. After reducer1 executed, the result is:
```
EXOA00341AB123456       ('A', 'Mercedes', '2016')
INU45KIOOPA343980       ('A', 'Mercedes', '2015')
VOME254OOXW344325       ('A', 'Mercedes', '2015')
VXIO456XLBB630221       ('A', 'Nissan', '2003')
```

This is the input for mapper2. Mapper2 reformat the input to create new k-v pair, key is the combine of Make and Year, and put `1` at the end of each record as the started count value. The result after executed Mapper2 is:

```
Mercedes2016	1
Mercedes2015	1
Mercedes2015	1
Nissan2003	1
```
We also use Unix's sort to simulate `Shuffer and Sort` phase in MapReduce framework. The result after sorted is:
```
Mercedes2015	1
Mercedes2015	1
Mercedes2016	1
Nissan2003	1
```
This becomes the input for Reducer2. The main role of Reducer2 is counting number of records group by key. The final result is:

```
Mercedes2015	2
Mercedes2016	1
Nissan2003	1
```

## Running
Suppose you've already installed and started haddop successfully.

* Step 1: copy csv file into hdfs
```
hdfs dfs -put data.csv input
```
Step 2: Run the map-reduce

Run the first map-reduce
```
hadoop jar /usr/local/hadoop/contrib/streaming/hadoop-*streaming*.jar \
-file autoinc_mapper1.py -mapper autoinc_mapper1.py \
-file autoinc_reducer1.py -reducer autoinc_reducer1.py \
-input input/data.csv -output output/all_accidents
```

Then run the second map-reduce. Note that the input of the second map-reduce is the output of the first map-reduce.
```
hadoop jar /usr/local/hadoop/contrib/streaming/hadoop-*streaming*.jar \
-file autoinc_mapper2.py -mapper autoinc_mapper2.py \
-file autoinc_reducer2.py -reducer autoinc_reducer2.py \
-input output/all_accidents -output output/make_year_count
```
