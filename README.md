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
