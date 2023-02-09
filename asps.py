#UPDATE LINES 15,20,21,22,23,29,30,41

import psycopg2
import csv
import pandas as pd
import sqlalchemy
import datetime
import os
from pathlib import Path
import time
import shutil


def main():
	
	conn = psycopg2.connect(
					host = ,#DATABASE IP ADDRESS
					database = ,#DATABASE HOST NAME
					port =, #PORT NUMBER
					user=usn, #DATABASE USERNAME
					password=pxw, #DATABASE PASSWORD
	)
	print("Logged onto database")       
	
	cursor = conn.cursor()

	#UPDATE QUERY BELOW

	query_path = 'asps.sql'

	with open(query_path, 'r') as o:
		query = o.read()

	cursor.execute(query)

	results = cursor.fetchall()

	print('Query Successfully Run')

	columns = [desc[0] for desc in cursor.description]

	df = pd.DataFrame(results, columns = columns, dtype='category')
	
	df.to_excel(drop_file, sheet_name = 'data')

	print('Exported to',drop_file)


def error(error_message):

	print(error_message)


if __name__=="__main__":

	ctstart = datetime.datetime.now()
	
	print('Starting Now on',ctstart)

	cfile =  #WHERE YOUR DATABASE CREDENTIALS ARE LOCATED
	
	date_string = datetime.datetime.now()
	
	date_string = date_string.strftime("%m-%d-%Y")
	
	filename = #NAME OF FILE YOU WANT THE DATA TO BE - USE RAW STRING
	
	drop_path = #FILE PATH WHERE YOU WANT FILE TO GO - USE RAW STRING
	
	drop_file = os.path.join(drop_path,filename) #WHERE YOU WANT THE FILE TO EXPORT TO
	

	try:
		with open(cfile, 'r') as o:
			creds = o.read().split()
			usn = creds[0].strip()
			pxw = creds[1].strip()
		main()
		exception = False
		ctend = datetime.datetime.now()
		ctcount = ctend - ctstart
		print(f'Process Successfully Completed\nTime to Complete:{ctcount}')
	except BaseException as be:
		exception = True
		error(str(be))
		ctend = datetime.datetime.now()
		ctcount = ctend - ctstart
		print(f'Process Completed Unsuccessfully\nTime to Complete:{ctcount}')