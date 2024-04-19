import random
attendence = random.randint(0,2)

wage_per_hour=20
daily_hours=8
partTime_hours=4


def fullTime_emp_wage_forMonth(working_day):
    wage_forMonth= working_day * (wage_per_hour * daily_hours)
    return wage_forMonth

def PartTime_emp_wage_forMonth(working_day):
    PartTime_emp_wage= working_day * (wage_per_hour * partTime_hours)
    return PartTime_emp_wage

print(fullTime_emp_wage_forMonth(20))

print(PartTime_emp_wage_forMonth(20))




