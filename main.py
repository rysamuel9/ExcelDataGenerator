from interfaces.dummy_data_generator import DummyDataGenerator
import openpyxl
import os
from datetime import datetime

if __name__ == "__main__":
    num_rows = 20
    generator = DummyDataGenerator(num_rows=num_rows)
    generated_data = generator.generate_dummy_data()

    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = "PROFILE"

    headers = [
        "EmployeeID*",
        "Email*",
        "Name*",
        "Role",
        "Phone*",
        "CurrentAddress",
        "DateBirth*",
        "City",
        "Gender*",
        "Status*",
        "ExpectedSalary",
        "ContractType",
        "HRPIC",
        "JoinDate"
    ]
    sheet.append(headers)

    for employee in generated_data:
        employee_data = [
            employee.employee_id, employee.email, employee.name, employee.role,
            employee.phone, employee.address, employee.dob, employee.city,
            employee.gender, employee.status, employee.salary, employee.contract_type,
            employee.hr_pic, employee.join_date
        ]
        sheet.append(employee_data)

    target_directory = os.path.join(os.getcwd(), 'generated_excel')

    os.makedirs(target_directory, exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

    file_name = f"dummy_data_{timestamp}.xlsx"

    file_path = os.path.join(target_directory, file_name)
    workbook.save(file_path)
    print(
        f"Dummy data for {num_rows} employees generated and saved to {file_name}.")
