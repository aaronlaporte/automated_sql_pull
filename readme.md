# Introduction
This is a Python script that exports data from a PostgreSQL database to an excel file. It connects to the database using psycopg2, runs a query, fetches the results, converts it into a Pandas DataFrame, and finally exports the DataFrame to an excel file using the to_excel function.

## Requirements

This script requires the following packages:

- psycopg2

- csv

- pandas

- sqlalchemy

- datetime

- os

- pathlib

- time

- shutil


## Usage

Replace the following variables with your desired values:

- cfile: the location of the file that contains your database credentials

- filename: the name of the excel file you want to export the data to

- drop_path: the file path where you want the excel file to be exported to

The script logs onto the database using the credentials provided in cfile. It then runs a query from the file asps.sql. 

The results from the query are then fetched, converted into a Pandas DataFrame, and exported to an excel file using the to_excel function.

To begin this code, there is a _'.bat'_ file that you can schedule within your task scheduler (windows environment).  

#### **_Please be sure to update the information in the '.bat' file to fit your own python set up._**

## Error Handling
The script includes an error handling mechanism that logs any errors that occur during the process. If the process is completed successfully, the output will be "Process Successfully Completed." If there is an error, the error message will be logged and the output will be "Process Completed Unsuccessfully."