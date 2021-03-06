from .template import *


class Plain(BotFunc):
    """Not a command: just keeps logs and usage_data"""
    def __init__(self, db):
        super().__init__(db)
    
    def create_handler(self):
        h = MessageHandler(Filters.text, callback=self.add_to_log)
        return h

    def add_to_log(self, update: Update, context: CallbackContext) -> None:
        super().log_activity(
            read = True,
            send = False,
            execute = False
        )
