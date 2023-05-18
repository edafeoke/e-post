from models.database import Database


class User:
    def __init__(self, db_file):
        self.db = Database(db_file)
        
    def create_user(self, username, password):
        try:
            self.db.insert_user(username, password)
        except Exception as e:
            print(f'Error creating user: {e}')
            
    def authenticate_user(self, username, password):
        user = self.db.get_user(username)
        if user and user[2] == password:
            return True
        else:
            return False
