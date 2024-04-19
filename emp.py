import random

class CalculateWage:
    def __init__(self, wage_per_hour, daily_hours, part_time_hours, total_hours, total_days):
        self.wage_per_hour = wage_per_hour
        self.daily_hours = daily_hours
        self.part_time_hours = part_time_hours
        self.total_hours = total_hours
        self.total_days = total_days
        self.max_hour = 0
        self.max_day = 0
        self.daily_wages = {}

    def wage_for_month(self):
        while (self.max_hour <= self.total_hours or self.max_day < self.total_days):
            attendance = random.randint(0, 2)
            if attendance == 1:
                self.max_hour += self.daily_hours
                self.max_day += 1
                total_wage = self.max_hour * self.max_day * self.wage_per_hour

                daily_wage = self.daily_hours * self.wage_per_hour
                self.daily_wages[self.max_day] = daily_wage

                print("Employee is present")
                print(f"Total Wage:{total_wage} ,Total Hours:{self.max_hour}")
                print(f"Day: {self.max_day}, Wage: {daily_wage}")
           

            elif attendance == 2:
                self.max_hour += self.part_time_hours
                self.max_day += 1
                total_wage = self.max_hour * self.max_day * self.wage_per_hour

                daily_wage = self.part_time_hours * self.wage_per_hour
                self.daily_wages[self.max_day] = daily_wage

                print("Part time Employee")
                print(f"Total Wage:{total_wage},Total Hours:{self.max_hour} ")
                print(f"Day: {self.max_day}, Wage: {daily_wage}")
               

            else:
                self.daily_wages[self.max_day] = "Absent"
                print("Employee is absent")
        
        return self.daily_wages


wage_per_hour = 20
daily_hours = 8
partTime_hours = 4
total_hours = 100
total_days = 20

cal = CalculateWage (wage_per_hour, daily_hours, partTime_hours, total_hours, total_days)
print(cal.wage_for_month())