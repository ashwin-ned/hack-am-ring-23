import os
import openai
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv()) # Read local .env file
openai.api_key  = os.environ["OPEN_API_KEY"]

class Assistant:
    def __init__(self, userData,  model="gpt-3.5-turbo"):

        self.model = model
        self.sport = userData.sport
        self.user_experience = userData.user_experience
        self.weight = userData.weight
        self.height = userData.height
        self.workout_intensity = userData.workout_intensity
        self.delimiter = "####"
        system_msgContent = f" you are a {self.sport} trainer focusing on {self.user_experience} athletes," \
                              f" give training schedule for an athlete with weight {self.weight} and height {self.height} for {self.workout_intensity} per week." \
                              f" Only provide the schedule in JSON format and no extra notes."
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
        return response