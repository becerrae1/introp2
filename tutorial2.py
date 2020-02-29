class Employee:

    num_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

emp_1 = Employee('Ethan', 'Medrano', 50000)
emp_2 = Employee('Test', 'User', 60000)
emp_3 = Employee('Blue', 'Medrano', 100000)

emp_1.raise_amount = 1.20

print(emp_1.raise_amount)
print(Employee.raise_amount)


print(Employee.num_emps)
