
from .sg_phone_number_recognizer import SgPhoneNumberRecognizer
from .sg_phone_number_operator import SgPhoneNumberOperator

from typing import List, Optional
from presidio_analyzer import Pattern
from langchain_experimental.data_anonymizer import PresidioAnonymizer
from presidio_anonymizer.entities import OperatorConfig

def init_anonymizer_sg_phone_number(anonymizer: PresidioAnonymizer, recognizer_patterns: Optional[List[Pattern]] = None):
    anonymizer.add_recognizer(SgPhoneNumberRecognizer(recognizer_patterns))

    operator = SgPhoneNumberOperator()
    anonymizer.add_operators({
            "SG_PHONE_NUMBER": OperatorConfig(
                "custom", {"lambda": operator.fake_sg_phone_number}
            )
        })
    pass


__all__= [
    "SgPhoneNumberRecognizer",
    "SgPhoneNumberOperator",
    "init_anonymizer_sg_phone_number",
]
