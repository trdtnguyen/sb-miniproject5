# sb-miniproject5
Post-Sale Automobile Report.

In this project, We receive a dataset with a history report of various vehicles. Our goal is to
write a MapReduce program to produce a report of the total number of accidents per make and
year of the car.

## Data model:

Column | Type
-------|------
incident_id | INT
incident_type STRING | (I: initial sale, A: accident, R: repair)
vin_number | STRING
make | STRING (The brand of the car, only populated with incident type “I”)
model | STRING (The model of the car, only populated with incident type “I”)
year | STRING (The year of the car, only populated with incident type “I”)
Incident_date | DATE (Date of the incident occurrence)
description | STRING
