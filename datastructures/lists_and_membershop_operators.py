import datetime
import calendar

# reference - https://stackoverflow.com/questions/4130922/how-to-increment-datetime-by-custom-months-in-python-without-using-library
def add_months(sourcedate, months):
    month = sourcedate.month - 1 + months
    year = sourcedate.year + month // 12
    month = month % 12 + 1
    day = min(sourcedate.day, calendar.monthrange(year,month)[1])
    return datetime.date(year, month, day)

def generate_month_names_list(actual_date):
    months = list()
    for i in range(12):
        next_date = add_months(actual_date, i)
        next_month = next_date.strftime("%B")
        print(f"next month {next_month}")
        months.append(next_month)
    return months

actual_date = datetime.datetime.now()
month = actual_date.strftime("%B")
print(f"actual month: {month}")
months_list = generate_month_names_list(actual_date)
print(months_list)
print(months_list[0])
print(months_list[-1])
print(months_list[-2])
print(months_list[len(months_list) - 1])

print(months_list)
print(months_list[0:-2])
print(months_list[:-2])
print(months_list[-2:])
print("December" in months_list)

# QUIZ

# 1

month = 8
days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]

# use list indexing to determine the number of days in month
num_days = days_in_month[month - 1]

print(num_days)

# 2

eclipse_dates = ['June 21, 2001', 'December 4, 2002', 'November 23, 2003',
                 'March 29, 2006', 'August 1, 2008', 'July 22, 2009',
                 'July 11, 2010', 'November 13, 2012', 'March 20, 2015',
                 'March 9, 2016']
                 
                 
# TODO: Modify this line so it prints the last three elements of the list
print(eclipse_dates[-3:])