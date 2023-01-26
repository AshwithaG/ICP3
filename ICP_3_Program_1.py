class Employee:
    employees_count = 0

    def __init__(self, name, family, salary, department):
        self.name = name
        self.family = family
        self.salary = salary
        self.department = department
        Employee.employees_count += 1

    def average_salary(employees):
        sum_of_salaries = 0
        for employee in employees:
            sum_of_salaries += employee.salary
        return sum_of_salaries / Employee.employees_count


class FulltimeEmployee(Employee):

    def __init__(self, name, family, salary, department):
        super().__init__(name, family, salary, department)


def main():
    employees = [FulltimeEmployee("John", "Family1", 5000, "Java"), FulltimeEmployee("Mike", "Family2", 7000, "Python"),
                 Employee("Sarah", "Family3", 9500, "Devops"), Employee("Thomas", "Family4", 6700, "Cloud Computing")]
    print("Average salary: ", FulltimeEmployee.average_salary(employees))


if __name__ == "__main__":
    main()
