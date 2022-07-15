import datetime
from pytz import timezone


class Employee:
    def __init__(self, emp_name, emp_id):
        self.__emp_name = emp_name
        self.__emp_id = emp_id

    def get_name(self):
        return self.__emp_name

    def get_id(self):
        return self.__emp_name

    name = property(get_name)
    id = property(get_id)


class ProductionWorker(Employee):
    def __init__(self, prod_name, prod_id, prod_shift, hourly_pay):
        self.__shift = prod_shift
        self.__hourly_pay = hourly_pay
        super().__init__(prod_name, prod_id)

    def get_shift(self):
        return self.__shift

    def get_hourly_pay(self):
        return self.__hourly_pay

    shift = property(get_shift)
    hourly_pay = property(get_hourly_pay)


def main():
    tz = timezone("EST").localize(datetime.datetime.now())
    print("Programmer: Dsierra")
    print(tz.strftime("%B %d, %Y @ %I:%M:%S %p\n"))

    name = input("Enter your name: ")
    empName_in = input("Enter your employee's name: ")
    empId_in = int(input("Enter the ID number: "))
    shift_in = int(input("Enter the shift number: "))
    hourly_in = float(input("Enter the hourly pay rate: "))

    prod_worker = ProductionWorker(empName_in, empId_in, shift_in, hourly_in)

    print(
        f"{name}, here is the information for the production worker {prod_worker.name}\n"
    )

    print(
        f"Name: {prod_worker.name}\nID number: {prod_worker.id}\n"
        f"Shift: {prod_worker.shift}\nHourly Pay Rate: ${prod_worker.hourly_pay:.2f}\n"
    )


main()
