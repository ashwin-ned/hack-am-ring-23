from pydantic import BaseModel
from typing import Optional

class UserDataModel(BaseModel):
    age                 : int
    weight              : int
    height              : int
    sport               : str
    user_experience     : str
    workout_intensity   : int
    time_period         : int
    user_prompt         : Optional[str]


class TrackingInput(BaseModel):
    set                 :  Optional[int]
    rep                 :  Optional[int]
    task                :  Optional[str] 
    check               :  Optional[bool]