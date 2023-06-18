from gpt_backend.Logger import Logger
from gpt_backend.Assistant import Assistant
from datetime import datetime
if __name__ == "__main__":


    user_msg = f" I am a taekwondo professional who stopped training for two years." \
               f" Give me a workout schedule to get back into shape in a month's time period."

    Trainer1 = Assistant("taekwondo", "professional", 21, 3)
    response = Trainer1.create_prompt_message(user_msg)

    # Log the Input and Output for study
    time_stamp = datetime.now()
    dt_string = time_stamp.strftime("%d/%m/%Y %H:%M:%S")
    log = Logger(user_msg, [Trainer1.model, Trainer1.sport, Trainer1.user_experience, Trainer1.bmi, Trainer1.workout_intensity], response, dt_string)
    log.log_data()