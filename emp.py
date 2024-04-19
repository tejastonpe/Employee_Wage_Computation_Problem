import random

wage_per_hour=20
daily_hours=8
daily_wage = wage_per_hour * daily_hours
# part_time_hours=4

def cal_monthly_wages():
    total_working_days = 0
    total_wages = 0
    # attendence=

    while total_working_days <= 20:
        if  random.randint(0, 1)== 1: 
            total_working_days += 1
            total_wages += daily_wage

    return total_wages


monthly_wages = cal_monthly_wages()
print(f"Monthly wages:{monthly_wages}")








