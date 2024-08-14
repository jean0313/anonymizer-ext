## Usage

```python
from langchain_experimental.data_anonymizer import PresidioAnonymizer
from anonymizer_ext import *
from presidio_analyzer import Pattern

anonymizer = PresidioAnonymizer()
init_anonymizer_sg_phone_number(anonymizer, [Pattern("SG Phone Number", r"(\+65\s?|\b65\s?)?[3689]\d{7}\b", 0.5)])
init_anonymizer_uob_cif(anonymizer)


data = anonymizer.anonymize(
    "My name is Slim Shady, call me at +65 96667440 or email me at real.slim.shady@gmail.com, CIF is 0000000001244567890"
)

print(data)
```