class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.__salary = salary

    def set_salary(self, new_salary, changer):
        if isinstance(changer, HR):
            self.__salary = new_salary
        else:
            print("Xatolik: Ish haqini faqat HR o'zgartira oladi!")

    def get_salary(self, requester):
        if isinstance(requester, Manager):
            return self.__salary
        return "maxfiy"


class Manager(Employee):
    pass


class HR(Employee):
    pass



worker = Employee("Ali", "Developer", 8000)
manager = Manager("Dilshod", "Manager", 15000)
hr = HR("Madina", "HR", 20000)

print("Manager ko'radi:", worker.get_salary(manager))

print("Xodim ko'radi:", worker.get_salary(worker))

worker.set_salary(9000, hr)
print("Yangilangan maosh:", worker.get_salary(manager))

worker.set_salary(5000, manager)
