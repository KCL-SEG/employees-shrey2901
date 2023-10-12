"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name,salary,hours=0,commission=0,contracts=0):
        self.name = name
        self.salary = salary
        self.hours = hours
        self.commission =commission
        self.contracts = contracts

    def get_pay(self):
        total_salary = self.salary
        total_commission = self.commission
        if self.hours :
             total_salary *= self.hours
        if self.contracts :
             total_commission *= self.contracts
        return (total_salary+ total_commission)


    def __str__(self):
        str = f'^{self.name} works on a '
        if self.hours:
            str += f'contract of {self.hours} hours at {self.salary}/hour'
        else:
            str += f'monthly salary of {self.salary}'
        if self.commission:
            if self.contracts:
                str += f' and receives a commission for {self.contracts} contract\(s\) at {self.commission}/contract'
            else:
                str += f' and receives a bonus commission of {self.commission}'
        str += f'.\s+Their total pay is {self.get_pay()}.$'
        return str

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie',4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie',25,100)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee',3000,0,200,4)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan',25,150,220,3)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie',salary=2000,commission=1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel',30,120,600,0)
