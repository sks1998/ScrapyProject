#python program to send data from the csv file to the  databse


import mysql.connector
import csv
#connection establishment to server
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="redhat",
  database="edulab",
  auth_plugin="mysql_native_password"
)
#defining the cursor to the database
mycursor = mydb.cursor()

csv_data = csv.DictReader(open('naukri_data.csv'))
for row in csv_data:
  # query to insert data in dataanalyst_ncr table
  query = ("INSERT INTO dataanalyst_ncr (company_name,experience_required,job_description,job_description_page,job_title,key_skills,salary,last_updated_on) VALUES (%s,%s,%s,%s,%s,%s,%s,CURDATE())")
  #defining dictionary key value
  value = (row['comp_name'],row['exp_req'],row['job_desp'],row['job_desp_page'],row['job_title'],row['key_skills'],row['sal'])
  #executing the query to insert
  mycursor.execute(query,value)
  #making changes commit to the database
  mydb.commit()
  
mycursor.close()

i=0
mycursor = mydb.cursor()
csv_data = csv.DictReader(open('naukri_data.csv'))
for row in csv_data:
  i=i+1
  #query to insert data in location job table
  query1 = "INSERT INTO location_jobs (job_id,location_id,city) VALUES((SELECT job_id FROM dataanalyst_ncr WHERE dataanalyst_ncr.job_id= %s) ,%s,%s)"
  #defining dictionary key value
  value1 = (str(i),str(i),row['loc'])
  #executing the insert query
  mycursor.execute(query1,value1)
  mydb.commit()
#print(mycursor.rowcount, "record inserted.")