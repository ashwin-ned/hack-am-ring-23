

class Logger:

    def __init__(self, user_msg, assistant_msg, response, timestamp):
        self.user_msg = user_msg
        self.assistant_msg = str(assistant_msg)
        self.response = str(response)
        self.timestamp = timestamp


    def log_data(self):

        with open('log.txt', 'a') as f:
            f.write(self.timestamp)
            f.write('\n')
            f.write(self.user_msg)
            f.write('\n')
            f.write(self.assistant_msg)
            f.write('\n')
            f.write(self.response)
            f.write('\n')
            f.write('\n')
            f.write('\n')

        f.close()