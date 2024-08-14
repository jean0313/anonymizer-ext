from faker import Faker
from faker.providers import BaseProvider
import random

class SgPhoneNumberProvider(BaseProvider):
    def singapore_phone_number(self):
        first_digit = random.choice([3, 6, 8, 9])
        remaining_digits = ''.join(random.choices('0123456789', k=7))
        return f"{first_digit}{remaining_digits}"
    
    def singapore_international_phone_number(self):
        return f"+65 {self.singapore_phone_number()}"
    
class SgPhoneNumberOperator:
    def __init__(self) -> None:
        self.fake = Faker()
        self.fake.add_provider(SgPhoneNumberProvider)
        pass

    def fake_sg_phone_number(self, _=None):
        return self.fake.singapore_international_phone_number()


