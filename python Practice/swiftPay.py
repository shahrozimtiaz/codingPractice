from datetime import *
import sys

while(True):
    dates = input("Enter two dates for pay period\n").split(" ")
    if(dates[0].lower() in ['quit','exit']):
        print('bye')
        sys.exit(0)
    elif(len(dates)!=2):
        print("Invalid format. Try date1 date2")
    else:
        try:
            pay = 0
            startDate = datetime.strptime(dates[0], '%m/%d/%Y').date()
            endDate = datetime.strptime(dates[1], '%m/%d/%Y').date()
            if(endDate<startDate):
                print("End date can't be smaller than start date")
                continue
            while(startDate!=endDate):
                if(startDate.isoweekday() not in range(6,8)):
                    pay += 160
                startDate+= timedelta(days=1)
            print('Pay: ' + str(pay))
        except ValueError as e:
            print("Invalid date format try m/dd/yyyy")
