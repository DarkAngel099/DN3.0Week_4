

class Employee:
    def __init__(self, name, hours_worked, hourly_rate):
        self.name = name
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_pay(self):
        if self.hours_worked <= 40:
            total_pay = self.hours_worked * self.hourly_rate
        else:
            regular_pay = 40 * self.hourly_rate
            overtime_hours = self.hours_worked - 40
            overtime_pay = overtime_hours * (self.hourly_rate * 1.5)
            total_pay = regular_pay + overtime_pay
        return total_pay

class Manager(Employee):
    def __init__(self, name, hours_worked, hourly_rate, bonus):
        super().__init__(name, hours_worked, hourly_rate)
        self.bonus = bonus

    def calculate_pay(self):
        base_pay = super().calculate_pay()
        total_pay = base_pay + self.bonus
        return total_pay


employee_name = input("Enter employee's name: ")
employee_hours_worked = float(input("Enter hours worked: "))
employee_hourly_rate = float(input("Enter hourly rate: "))


employee = Employee(employee_name, employee_hours_worked, employee_hourly_rate)


manager_name = input("Enter manager's name: ")
manager_hours_worked = float(input("Enter hours worked: "))
manager_hourly_rate = float(input("Enter hourly rate: "))
manager_bonus = float(input("Enter bonus amount: "))

# Create Manager object
manager = Manager(manager_name, manager_hours_worked, manager_hourly_rate, manager_bonus)

# Calculate and print the total pay
print(f"{employee.name}'s total pay: ${employee.calculate_pay():.2f}")
print(f"{manager.name}'s total pay: ${manager.calculate_pay():.2f}")
