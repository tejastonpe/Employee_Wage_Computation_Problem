import random
attendence = random.randint(0,2)

wage_per_hour=20
daily_hours=8
partTime_hours=4

match attendence:
    case 1:
        print("Emplpyee is present")
        daily_Emp_wage= wage_per_hour * daily_hours
        print(f"Employees Daily wage is: {daily_Emp_wage}")
    case 2:
        print("Part time employee")
        PartTime_Emp_wage= wage_per_hour * partTime_hours
        print(f"Part time Employees wage is: {PartTime_Emp_wage}")
    case 0:
        print("Employee is Absent")
        
