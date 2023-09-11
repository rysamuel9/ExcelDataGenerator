import pytest
from unittest.mock import patch
from interfaces.dummy_data_generator import DummyDataGenerator
from core.entities import Employee


@pytest.fixture
def generator():
    return DummyDataGenerator(num_rows=10)


@patch('builtins.input', side_effect=['10'])
def test_generate_dummy_data(mock_input, generator):
    generated_data = generator.generate_dummy_data()

    assert len(generated_data) == 10

    for employee in generated_data:
        assert isinstance(employee, Employee)
        assert isinstance(employee.employee_id, int)
        assert isinstance(employee.email, str)
        assert isinstance(employee.name, str)
        assert isinstance(employee.role, str)
        assert isinstance(employee.phone, str)
        assert isinstance(employee.address, str)
        assert isinstance(employee.dob, str)
        assert isinstance(employee.city, str)
        assert isinstance(employee.gender, str)
        assert isinstance(employee.status, str)
        assert isinstance(employee.salary, int)
        assert isinstance(employee.contract_type, str)
        assert isinstance(employee.hr_pic, str)
        assert isinstance(employee.join_date, str)
        assert employee.email.endswith("@gmail.com")
        assert employee.phone.startswith("+628")


@pytest.fixture
def zero_generator():
    return DummyDataGenerator(num_rows=0)


def test_generate_zero_dummy_data(zero_generator):
    generated_data = zero_generator.generate_dummy_data()
    assert len(generated_data) == 0


def test_generate_negative_dummy_data():
    generator = DummyDataGenerator(num_rows=-5)
    generated_data = generator.generate_dummy_data()
    assert len(generated_data) == 0
