from application.use_cases import GenerateDummyDataUseCase


class DummyDataGenerator:
    def __init__(self, num_rows=20):
        self.num_rows = num_rows

    def generate_dummy_data(self):
        use_case = GenerateDummyDataUseCase(num_rows=self.num_rows)
        use_case.execute()
        return use_case.get_generated_data()