from datetime import datetime

def date(string_date,numOfDates, jump ):

    date_obj = datetime.strptime(string_date, "%d/%m/%Y")
    dates=[]
    for i in range(numOfDates):
        day = date_obj.day
        month = date_obj.month
        year = date_obj.year
        date_obj=check_date(day,month,year,jump)
        dates.append(date_obj.strftime("%d/%m/%Y"))
    return dates

def check_date(day,month,year,jump):
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day += jump
    while day >days_in_month[month-1]:
        day -= days_in_month[month - 1]
        month += 1
        if month == 13:
            year += 1
            month = 1
    return datetime(year,month,day).date()


def main():
    print("enter date in format dd/mm/yyyy")
    string_date=input()
    print("enter amount of dates.")
    numOfDates=int(input())
    print("enter jump")
    jump=int(input())
    dates=date(string_date,numOfDates,jump)
    print(dates)



if __name__ == "__main__":
    main()

