from core.entities import Employee
from core.services import DummyDataGeneratorService
from core.repositories import EmployeeRepository


class GenerateDummyDataUseCase:
    def __init__(self, num_rows=20):
        self.num_rows = num_rows
        self.generator_service = DummyDataGeneratorService()
        self.employee_repo = EmployeeRepository()

    def execute(self):
        for _ in range(self.num_rows):
            employee = self.generator_service.generate_dummy_employee()
            self.employee_repo.add_employee(employee)

    def get_generated_data(self):
        return self.employee_repo.get_all_employees()