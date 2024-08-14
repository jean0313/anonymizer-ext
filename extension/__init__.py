from .phone_number import *

from langchain_experimental.data_anonymizer import PresidioAnonymizer
from presidio_anonymizer.entities import OperatorConfig

def sg_phone_number_init(anonymizer: PresidioAnonymizer):
    anonymizer.add_recognizer(SgPhoneNumberRecognizer())

    operator = SGPhoneNumberOperator()
    anonymizer.add_operators({
            "SG_PHONE_NUMBER": OperatorConfig(
                "custom", {"lambda": operator.fake_sg_phone_number}
            )
        })
    pass

__all__ = ["sg_phone_number_init"]