from gpt_backend.logger import Logger
from gpt_backend.Assistant import Assistant
from datetime import datetime
from fastapi import FastAPI
import json


app = FastAPI()

user_msg = f" I am a taekwondo professional who stopped training for two years." \
           f" Give me a workout schedule to get back into shape in a month's time period." \
           f" in a JSON format."



@app.get("/",operation_id="getState",description="Index page",name="get intro page",tags=["intro"])
def index():
    return{"Info":"Welcome to Training Bot"}


@app.post("/first_request",operation_id="firstRequest",tags=["request"])
async def first_req():
    Trainer1 = Assistant("taekwondo", "professional", 21, 3)
    response = Trainer1.create_prompt_message(user_msg)
    # Log the Input and Output for study
    time_stamp = datetime.now()
    dt_string = time_stamp.strftime("%d/%m/%Y %H:%M:%S")
    log = Logger(user_msg, [Trainer1.model, Trainer1.sport, Trainer1.user_experience, Trainer1.bmi, Trainer1.workout_intensity], response, dt_string)
    log.log_data()
    data = json.loads(response)
    return data
