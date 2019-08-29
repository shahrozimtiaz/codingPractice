from datetime import datetime
from datetime import date
import sys
import dateutil.relativedelta
import MySqlConnector

cursor = MySqlConnector.connect('root', 'Jokerface07!')
dic = {}
recNum = 0

def ageCalculator(name):
    if (name.lower() in dic):
        global recNum
        recNum += 1
        print("----------------------")
        print("{:<10}~{:<10}".format(str(recNum) + ": " + name.upper(), dic[name]))
        birthDate = datetime.strptime(dic[name], '%m/%d/%Y').date()
        today = date.today()
        difference = dateutil.relativedelta.relativedelta(today, birthDate)
        return str(difference.years) + " years " + str(difference.months) + " months " + str(difference.days) + " days "
    else:
        return("No records found")

while (True):
    try:
        recNum = 0;
        cursor.execute("Select * from ages")
        results = cursor.fetchall()
        for result in results:
            lineArgs = result[1].split(" ")
            dic[lineArgs[0]] = lineArgs[1]
            cursor.connection.commit()
        response = input("Enter command:\n").strip().lower()
        response = response.split(" ")
        if(len(response)!=1 and len(response) != 3):
            print("Invalid command")
        elif(response[0] == "w"):
            response = response[1:]
            record = ""
            for line in response:
                record+=line + " "
            cursor.execute("INSERT INTO ages(description) VALUES ('" + record.strip() + "')")
            cursor.connection.commit()
            print("Stored")
        elif(response[0] == "p" and len(response)==1):
            print("Printing records..\n")
            for name in sorted(dic.keys()):
                ageCalculator(name)
        elif(response[0] == "d" and len(response)==3):
            response = response[1:]
            if(response[0]in dic):
                print("----------------------")
                print("{:<10}~{:<10}".format(response[0].upper(), dic[response[0]]))
                birthDate = datetime.strptime(dic[response[0]], '%m/%d/%Y').date()
                endDate = datetime.strptime(response[1], '%m/%d/%Y').date()
                difference = dateutil.relativedelta.relativedelta(endDate, birthDate)
                print("->",difference.years, "years", difference.months, "months", difference.days, "days")
            else:
                print("No records found")
        elif(response[0] == "q" and len(response)==1):
            print("Now exiting.. \n"
                  + "goodbye")
            cursor.close()
            sys.exit(0)
        elif(response[0].lower() == "all" and len(response)==1):
            for name in sorted(dic.keys()):
                print("-> " + ageCalculator(name))
        elif(response[0] == "help" and len(response)==1):
            print("Commands:")
            print("'name' - gets age")
            print("w 'name' 'bithdate' - writes record to be stored")
            print("d 'name' 'date' - how old this person was at the date")
            print("q - exit")
            print("p - print all records")
            print("all - calculate age for all records")
            print("help - this")
        else:
            print("-> " + ageCalculator(response[0]))
    except Exception as e:
            print("Error: you did something wrong:", e.args)
