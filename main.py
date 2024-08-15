from langchain_experimental.data_anonymizer import PresidioAnonymizer
from anonymizer_ext import *
import random
from presidio_analyzer import Pattern

anonymizer = PresidioAnonymizer()

init_anonymize_generic_field_lambda(
    anonymizer, 
    "SG_PHONE_NUMBER", 
    [Pattern("SG Phone Number", r"(\+65\s?|\b65\s?)?[3689]\d{7}\b", 0.5)], 
    lambda: f"+65 {random.choice([3, 6, 8, 9])}{''.join(random.choices('0123456789', k=7))}"
)


class ComplexFieldGenerator(FakeDataGenerator):
    def generate(self) -> str:
        return f"xxxx{''.join(random.choices('0123456789', k=10))}"

init_anonymize_generic_field(
    anonymizer,
    "COMPLEX_FIELD",
    patterns=[Pattern("Complex Field", r"\bxxxx\d{10}", 0.5)], 
    generator=ComplexFieldGenerator()
)

data = anonymizer.anonymize(
    "My name is Slim Shady, call me at +65 96667440 or email me at real.slim.shady@gmail.com, Complex Field xxxx2345678901 , phone is +65 96667440 "
)

print(data)