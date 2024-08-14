## Usage

```python
from langchain_experimental.data_anonymizer import PresidioAnonymizer
from anonymizer_ext import *

anonymizer = PresidioAnonymizer()
sg_phone_number_init(anonymizer)

data = anonymizer.anonymize(
    "My name is Slim Shady, call me at +65 96667440 or email me at real.slim.shady@gmail.com"
)

print(data)
```