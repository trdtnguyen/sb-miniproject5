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

## Testing:
Test mapper 1 and reducer1:
`$ cat data.csv | autoinc_mapper1.py | sort | autoinc_reducer1.py`

The output should be in the format of key value with key is vin number and value is tuple of (type, make, year).
The output should show group of data by key i.e., vin number.
```
EXOA00341AB123456       ('A', 'Mercedes', '2016')
INU45KIOOPA343980       ('A', 'Mercedes', '2015')
INU45KIOOPA343980       ('A', 'Mercedes', '2015')
UXIA769ABCC447906       ('A', 'Toyota', '2017')
UXIA769ABCC447906       ('A', 'Toyota', '2017')
VOME254OOXW344325       ('A', 'Mercedes', '2015')
VOME254OOXW344325       ('A', 'Mercedes', '2015')
VOME254OOXW344325       ('A', 'Mercedes', '2015')
VXIO456XLBB630221       ('A', 'Nissan', '2003')
VXIO456XLBB630221       ('A', 'Nissan', '2003')
VXIO456XLBB630221       ('A', 'Nissan', '2003')
VXIO456XLBB630221       ('A', 'Nissan', '2003')

```
