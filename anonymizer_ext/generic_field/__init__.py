from langchain_experimental.data_anonymizer import PresidioAnonymizer
from presidio_analyzer import Pattern, PatternRecognizer
from faker.providers import BaseProvider
from faker import Faker
from presidio_anonymizer.entities import OperatorConfig
from typing import List, Callable

from abc import ABC, abstractmethod

class FakeDataGenerator(ABC):

    @abstractmethod
    def generate(self) -> str:
        pass

def init_anonymize_generic_field_lambda(anonymizer: PresidioAnonymizer, entity: str, patterns: List[Pattern], fake_data_generator_fn: Callable[[], str]):
    fake = Faker()
    class DynamicProvider(BaseProvider):
        def generate_data(self):
            return fake_data_generator_fn()

    fake.add_provider(DynamicProvider)

    def fn(_=None):
        return fake.generate_data()
    
    anonymizer.add_operators({
            entity: OperatorConfig(
                "custom", {"lambda": fn}
            )
        })

    recognizer = PatternRecognizer(
        supported_entity=entity, patterns=patterns
    )
    anonymizer.add_recognizer(recognizer)
    pass

def init_anonymize_generic_field(anonymizer: PresidioAnonymizer, entity: str, patterns: List[Pattern], generator: FakeDataGenerator):
    fake = Faker()
    class DynamicProvider(BaseProvider):
        def generate_data(self):
            return generator.generate()

    fake.add_provider(DynamicProvider)

    def fn(_=None):
        return fake.generate_data()
    
    anonymizer.add_operators({
            entity: OperatorConfig(
                "custom", {"lambda": fn}
            )
        })

    recognizer = PatternRecognizer(
        supported_entity=entity, patterns=patterns
    )
    anonymizer.add_recognizer(recognizer)
    pass


__all__ = [
    "FakeDataGenerator",
    "init_anonymize_generic_field_lambda",
    "init_anonymize_generic_field"
]