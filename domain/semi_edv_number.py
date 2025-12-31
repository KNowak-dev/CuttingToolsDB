from pydantic import AfterValidator
from typing import Annotated
import re

class EDVNumberSemiProduct:
    def validate_edv_semi(v: str) -> str:
        if not re.fullmatch(r'57-\d{5}', v):
            raise ValueError("Podałeś zły format EDV półfabrykatu.")
        return v

    EDV_semi_product = Annotated[str, AfterValidator(validate_edv_semi)]
