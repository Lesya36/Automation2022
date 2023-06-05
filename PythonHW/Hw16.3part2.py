employee_shift = ["Mike", "Andrew", "Emma", "Kelly", "John", "Brad"]
def replace_employee(employee_shift, old_employee, new_employee, old_employee_index):
    old_employee.index = employee_shift.index(old_employee)
    employee_shift.remove(old_employee)
    employee_shift.insert(old_employee.index, new_employee)
    print(employee_shift)

    replace_employee(employee_shift, "Kelly", "Maria")