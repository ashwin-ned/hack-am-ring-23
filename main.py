
from gpt_backend.Assistant import Assistant

if __name__ == "__main__":

    user_msg = f" I am a taekwondo professional who stopped training for two years." \
               f" Give me a workout schedule to get back into shape in a month's time period."

    Trainer1 = Assistant("taekwondo", "professional", 21, 3)
    Trainer1.create_prompt_message(user_msg)
