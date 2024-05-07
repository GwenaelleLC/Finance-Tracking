from FileManager import*
from datetime import datetime
from glob import glob

class User:
    all_users = {}

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.expenses = []
        self.load_expenses()
        User.all_users[username] = self

    @classmethod
    def load_all_users(cls):
        user_files = glob('*_info.json')
        for user_file in user_files:
            user_info = FileManager.read_data(user_file)
            if user_info:
                cls(user_info['username'], user_info['password'])

    @classmethod
    def create_account(cls, username, password):
        file_name = f"{username}_info.json"
        if os.path.exists(file_name):
            print("Account already exists.")
            return None
        FileManager.write_data(file_name, {"username": username, "password": password})
        FileManager.write_data(f"{username}_expenses.json", [])
        return cls(username, password)

    @classmethod
    def login(cls, username, password):
        user_data = FileManager.read_data(f"{username}_info.json")
        if user_data and user_data["password"] == password:
            return cls(username, password)
        return None

    def add_expense(self, amount, category, date=None):
        date = datetime.now().strftime("%Y-%m-%d")  # La date est automatiquement réglée à aujourd'hui
        self.expenses.append({"amount": amount, "category": category, "date": date})
        FileManager.write_data(f"{self.username}_expenses.json", self.expenses)

    def load_expenses(self):
        expenses_data = FileManager.read_data(f"{self.username}_expenses.json")
        if expenses_data:
            self.expenses = expenses_data

    def remove_expense(self, index):
        if 0 <= index < len(self.expenses):
            del self.expenses[index]
            FileManager.write_data(f"{self.username}_expenses.json", self.expenses)
            return True
        return False

    def get_expense_history(self):
        return self.expenses