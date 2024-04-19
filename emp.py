import random

wage_per_hour=20
daily_hours=8
partTime_hours=4

total_hours=100
total_days=20

max_hour = 0
max_day = 0

def wage_for_month():
    global max_hour
    global max_day
    while (max_hour <= total_hours or max_day <= total_days):
        attendence = random.randint(0,2)
        if attendence==1:
            max_hour += daily_hours
            max_day += 1
            totalWage = max_hour * max_day * wage_per_hour
            print(totalWage)

        elif attendence==2:
            max_hour += daily_hours + partTime_hours
            max_day+= 1
            totalWage = max_hour * max_day * wage_per_hour
            print(totalWage)

        # totalWage = wage_per_hour * daily_hours
    return totalWage

print(wage_for_month())





