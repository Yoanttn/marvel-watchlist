import csv
from dotenv import dotenv_values
from manageDB import dbConnection

config = dotenv_values(".env")

con, cur = dbConnection(str(config["DBPATH"]))

films = list(csv.DictReader(open(str(config["DATAPATH"])+"film.csv", newline='')))

for film in films:
    pass

