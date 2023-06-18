from gpt_backend.logger import Logger
from gpt_backend.Assistant import Assistant
from gpt_backend.data_model import *
from datetime import datetime
from fastapi import FastAPI
from modules.database_manager import *
import logging
import json

app = FastAPI()

user_msg = " " 
# f" I am a taekwondo professional who stopped training for two years." \
#            f" Give me a workout schedule to get back into shape in a month's time period." \

# user_data = {"age":25, "weight": 70, "height":186, "sport":"taekwondo", "user_experience": "professional", "workout_intensity": 3, "time_period": 1}
# user = UserDataModel(**user_data)

@app.get("/",operation_id="getState",description="Index page",name="get intro page",tags=["intro"])
def index():
    return{"Info":"Welcome to Training Bot"}


@app.post("/first_request",operation_id="firstRequest",tags=["request"])
async def first_req(user:UserDataModel):
    try:
        Trainer1 = Assistant(user)
        response = Trainer1.create_prompt_message(user_msg)
        # Log the Input and Output for study
        time_stamp = datetime.now()
        dt_string = time_stamp.strftime("%d/%m/%Y %H:%M:%S")
        log = Logger(user_msg, [Trainer1.model, Trainer1.sport, Trainer1.user_experience, Trainer1.weight, Trainer1.height, Trainer1.workout_intensity], response, dt_string)
        log.log_data()
        data = json.loads(response)
        write_to_file("response_data.json",data)
        return data
    except Exception as e:
        print(f"Error is {e}")
        return {"Error":e} 

@app.post("/tracking_info")
def tracking(input_data:TrackingInput):
    try:
        data = read_file("response_data.json")
        for training in data["training_schedule"].values():
            if training["warm_up"]==input_data.task:
                training["tracking_data"]=input_data.dict()
        
        write_to_file("response_data.json",data)
    except Exception as e:
        print(f"Error : {e}")
        return {"Error":e}

            
    
    