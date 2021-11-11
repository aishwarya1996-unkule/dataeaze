# use to parse the command line argument
import argparse
# interaction with the system(run time environment)
import sys
# for connection of sql
import pymysql
# for read csv file
import csv
# for operations on json file
import json
#for opening a directory & doing iteration over files
import pathlib


#Action objects are used by an ArgumentParser to represent the information needed to parse a single argument from
# one or more strings from the command line.
parser = argparse.ArgumentParser()

# Filling an ArgumentParser with information about program arguments is done by making calls to the add_argument() method.
# Generally, these calls tell the ArgumentParser how to take the strings on the command line and turn them into objects.
parser.add_argument('-d','--source_dir',help="Path of directory")
parser.add_argument('-m','--mysql_details',help="Path of JSON file for connection to MYSQL")
args = parser.parse_args()

# Opening JSON file
f = open(args.mysql_details, )

# returns JSON object as
# a dictionary
data = json.load(f)
print(data)

# connection with mysql
db = pymysql.connect(host=data['host'],user=data['user'],password=data['password'],database=data['database'])
# we can insert using cursor
cursor = db.cursor()

# sys.argv() is an array for command line arguments in Python. To employ this module named “sys” is used.
# sys.argv is similar to an array and the values are also retrieved like Python array.
if len( sys.argv ) > 2:
  for path in pathlib.Path(args.source_dir).iterdir():
    if path.is_file():
      with open(path) as csvFile:
        reader = csv.reader(csvFile, delimiter=',')
        for line in reader:
          cursor.execute('INSERT INTO advertise(TV ,radio ,newspaper ,sales) VALUES(%s, %s, %s, %s)', line)


# Closing file
f.close()

db.commit()
cursor.close()
