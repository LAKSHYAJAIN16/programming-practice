day1, md, year1 = input().split(", ")
month1, date1 = md.split(" ")
date1 = int(date1)
year1 = int(year1)

day2, md2, year2 = input().split(", ")
month2, date2 = md2.split(" ")
date2 = int(date2)
year2 = int(year2)

def is_leap(year):
    if year % 4 == 0:
        if year % 400 == 0:
            return False
        return True
    return False

def get_days(month, year):
    if month == 2:
        if is_leap(year):
            return 29
        else:
            return 28
    else:
        return days_map[month]

i = 0   

def leap(day, date, year, month):
    cMonth = month
    cYear = year
    cDays = get_days(month, year)
    cDay = day
    
    # Add 13
    if date <= 13:
        cDay += ((13 - date) % 7)
        if cDay % 7 == 5:
            global i
            i += 1
        cDay -= ((13 - date) % 7)
    
    cDay += (cDays + 1 - date) % 7
    cDay = cDay % 7
    cMonth += 1
    if cMonth == 13:
        cMonth = 1
        cYear += 1
    print([cDay, 1, cYear, cMonth])
    return [cDay, 1, cYear, cMonth]
    
# Check
day_map = {
    "Monday" : 1,
    "Tuesday" : 2,
    "Wednesday" : 3,
    "Thursday" : 4,
    "Friday" : 5,
    "Saturday" : 6,
    "Sunday" : 0
}

# Month Map
month_map = {
    "January" : 1,
    "February" : 2,
    "March" : 3,
    "April" : 4,
    "May" : 5,
    "June" : 6,
    "July" : 7,
    "August" : 8,
    "September" : 9,
    "October" : 10,
    "November" : 11,
    "December" : 12
}
days_map = {
    1 : 31,
    2 : 28,
    3 : 31,
    4 : 30,
    5 : 31,
    6 : 30,
    7 : 31,
    8 : 31,
    9 : 30,
    10 : 31,
    11 : 30,
    12 : 31
}

# Starting
cur_day, cur_date, cur_year, cur_month = leap(day_map[day1], date1, year1, month_map[month1])
month2 = month_map[month2]

# Check if we've gone over
if cur_year == year2 and cur_month == month2:
    # Do one final check
    day3 = cur_day + 5
    if day3 % 7 == 5:
        i += 1
    print(i)
elif cur_year > year2 and cur_month > month2:
    print(i)
else:
    exit = False
    
    # Correct the Date
    while exit == False:
        # Leap
        cur_day, cur_date, cur_year, cur_month = leap(cur_day, cur_date, cur_year, cur_month)

        # Check if we've gone over
        if (cur_month == 1 and cur_year == year2 + 1) or (cur_year == year2 and cur_month == month2 + 1):
            exit = True
            break

    print(i)