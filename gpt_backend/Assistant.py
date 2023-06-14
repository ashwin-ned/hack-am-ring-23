import os
import openai
#from dotenv import load_dotenv, find_dotenv

# Read local .env file
#load_dotenv(find_dotenv())
openai.api_key = "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"


def get_completion_from_messages(message, model="text-curie-001", temperature=0, max_tokens=500):

    response = openai.ChatCompletion.create(
        model=model,
        messages=message,
        temperature=temperature,
        max_tokens=max_tokens,
    )
    return response.choices[0].message["content"]

class Assistant:
    def __init__(self, sport, user_experience, bmi, workout_intensity):

        self.sport = sport
        self.user_experience = user_experience
        self.bmi = bmi
        self.workout_intensity = workout_intensity
        self.delimiter = "####"
        self.system_message = f" you are a {self.sport} trainer focusing on {self.user_experience} athletes," \
                              f" give training schedule for an athlete with bmi {self.bmi} for {self.workout_intensity} per week"

    def create_prompt_message(self):
        user_message = f" I am a taekwondo professional who stopped training for two years." \
                       f" Give me a workout schedule to get back into shape in a month's time period."
        messages = [
            {'role': 'system',
             'content': self.system_message},
            {'role': 'user',
             'content': f"{self.delimiter}{user_message}{self.delimiter}"},
        ]
        #response = get_completion_from_messages(messages)
        #print(response)