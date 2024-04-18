import random
attendence = random.randint(0,1)

wage_per_hour=20
daily_hours=8

if attendence==1:
    print("Emplpyee is present")
    daily_Emp_wage= wage_per_hour * daily_hours
    print(f"Employees Daily wage is: {daily_Emp_wage}")
else:
    print("Employee is Absent")
