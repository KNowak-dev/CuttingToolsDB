from pydantic import BaseModel, validator
import re

class EDV_semi_finished_product(BaseModel):
    nr_edv_semi_finished_product: str

    @validator('nr_edv_semi_finished_product')
    def validate_edv_number(cls, nr_edv_semi_finished_product):
        pattern = r"[5]{1}[7]{1}-\d{5}"
        match = re.fullmatch(pattern, nr_edv_semi_finished_product)
    
        if not match:
            raise ValueError("Podałeś zły format EDV półfabrykatu.")
        return nr_edv_semi_finished_product
    