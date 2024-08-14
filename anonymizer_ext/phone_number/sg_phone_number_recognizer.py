from typing import List, Optional

from presidio_analyzer import Pattern, PatternRecognizer

class SgPhoneNumberRecognizer(PatternRecognizer):
    """
    Recognize Sg phone numbers using regex.

    :param patterns: List of patterns to be used by this recognizer
    :param context: List of context words to increase confidence in detection
    :param supported_language: Language this recognizer supports
    :param supported_entity: The entity this recognizer can detect
    """

    PATTERNS = [
        Pattern(
            "SG Phone Number",
            r"(\+65\s?|\b65\s?)?[3689]\d{7}\b",
            0.5,
        ),
    ]

    CONTEXT = ["phone", "number", "telephone", "cell", "cellphone", "mobile", "call"]

    def __init__(
        self,
        patterns: Optional[List[Pattern]] = None,
        context: Optional[List[str]] = None,
        supported_language: str = "en",
        supported_entity: str = "SG_PHONE_NUMBER",
    ):
        patterns = patterns if patterns else self.PATTERNS
        context = context if context else self.CONTEXT
        super().__init__(
            supported_entity=supported_entity,
            patterns=patterns,
            context=context,
            supported_language=supported_language,
        )
