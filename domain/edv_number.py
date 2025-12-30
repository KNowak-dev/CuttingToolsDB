from pydantic import BaseModel, validator
import re

class EDVNumber(BaseModel):
    nr_edv: str
        
    @validator('nr_edv')
    def validate_edv_number(cls, nr_edv):
        pattern = r"[5]{1}[1]{1}-\d{5}"
        match = re.fullmatch(pattern, nr_edv)
        
        if not match:
            raise ValueError("Podałeś zły format EDV.")
        return nr_edv
    
