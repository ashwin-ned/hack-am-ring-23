import os
import openai
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv()) # Read local .env file
openai.api_key  = os.environ["OPEN_API_KEY"]

class Assistant:
    def __init__(self, sport, user_experience, bmi, workout_intensity,  model="gpt-3.5-turbo"):

        self.model = model
        self.sport = sport
        self.user_experience = user_experience
        self.bmi = bmi
        self.workout_intensity = workout_intensity
        self.delimiter = "####"
        system_msgContent = f" you are a {self.sport} trainer focusing on {self.user_experience} athletes," \
                              f" give training schedule for an athlete with bmi {self.bmi} for {self.workout_intensity} per week"
        self.system_message = {'role': 'system', 'content': system_msgContent}


    def get_completion_from_messages(self, message, temperature=0, max_tokens=500):
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=message,
            temperature=temperature,
            max_tokens=max_tokens,
        )
        return response.choices[0].message["content"]


    def create_prompt_message(self, user_msg):
        user_message = {'role': 'user', 'content': user_msg}
        messages = [user_message, self.system_message]
        response = self.get_completion_from_messages(messages)
        print(response)
        return response