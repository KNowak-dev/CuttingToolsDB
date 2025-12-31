from pydantic import AfterValidator
from typing import Annotated
import re

class EDVNumber:
    def validate_edv(v: str) -> str:
        if not re.fullmatch(r"51-\d{5}", v):
            raise ValueError("Podałeś zły format EDV.")
        return v

    EDV = Annotated[str, AfterValidator(validate_edv)]
    