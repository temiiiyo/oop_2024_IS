from user import User

class Application:
    def __init__(self, app_id, user: User, app_type):
        self.app_id = app_id
        self.user = user
        self.app_type = app_type