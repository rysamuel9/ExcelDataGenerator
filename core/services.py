import random
from faker import Faker
from core.entities import Employee


class DummyDataGeneratorService:
    def __init__(self):
        self.fake = Faker('id_ID')

    def generate_random_date(self):
        day = random.randint(1, 28)
        month = random.randint(1, 12)
        year = random.randint(1980, 2000)
        return f"{day:02d}-{month:02d}-{year}"
    
    def generate_random_phone(self):
        prefix = "+628"
        digits = random.randint(8, 10)
        random_number = ''.join(str(random.randint(0, 9)) for _ in range(digits))
        return f"{prefix}{random_number}"

    def generate_dummy_employee(self):
        employee_id = self.fake.unique.random_int(min=10000, max=99999, step=1)
        email = self.fake.unique.email(domain="gmail.com")
        name = self.fake.name()
        role = self.fake.job()
        phone = self.generate_random_phone()
        address = self.fake.address()
        dob = self.generate_random_date()
        city = self.fake.city()
        gender = random.choice(["Male", "Female"])
        status = random.choice(["Single", "Married"])
        salary = random.randint(4_000_000, 20_000_000)
        contract_type = random.choice(["Permanent", "Contract"])
        hr_pic = "rony.tamba@rapidtech.id"
        join_date = self.generate_random_date()

        return Employee(
            employee_id, email, name, role, phone, address, dob, city, gender, status,
            salary, contract_type, hr_pic, join_date
        )
