from datetime import datetime
from typing import List, Optional 
from pydantic import (
    BaseModel,
    ValidationError,
    validator,
    PositiveInt,
    StrictBool
)

def get_error(json_input):

    class Control_error(BaseModel):
    
        area: PositiveInt
        property_type: str
        rooms_number: PositiveInt
        zip_code: int
        Locality: str
        Elevator: bool
        land_area: PositiveInt
        garden: StrictBool
        garden_area: PositiveInt
        equipped_kitchen: StrictBool
        full_address: str
        swimming_pool: StrictBool
        furnished: StrictBool
        open_fire: StrictBool
        terrace: bool
        terrace_area: PositiveInt
        facades_number: PositiveInt
        building_state: str

        @validator("property_type", allow_reuse=True)
        def property_type_check(cls, v):
            valid_option = ["APARTMENT", "HOUSE"]
            if v not in valid_option:
                raise ValueError(
                    f'This are the valid options : {valid_option}'
                )
            return v
        
        @validator("Locality", allow_reuse=True)
        def Locality_check(cls, v):
            Locality_option = ["Brussels", "Flanders", "Wallonia"]
            if v not in Locality_option :
                raise ValueError(
                    f'This are the valid options : {Locality_option }'
                )
            return v
        
        @validator("building_state", allow_reuse=True)
        def building_state_check(cls, v):
            building_state_option = ["NEW", "GOOD", "TO RENOVATE", 
                                        "JUST RENOVATED", "TO REBUILD"]

            if v not in building_state_option :
                raise ValueError(
                    f'This are the valid options : {building_state_option}'
                )
            return v

    try:
        error = Control_error(**json_input)
        return "No errors found"
    except ValidationError as e:
        return e.json()