from abc import ABC, abstractmethod
from datetime import datetime

class Expense(ABC):
    def __init__(self, amount, date=None):
        self.amount = amount
        self.date = date if date else datetime.now().strftime("%Y-%m-%d")
    @abstractmethod
    def to_dict(self):
        pass
class ExpenseFactory:
    @staticmethod
    def create_expense(category, amount, date=None):
        expense_classes = {'Food': FoodExpense, 'Transport': TransportExpense, 'Activity': ActivityExpense, 'Health': HealthExpense}
        return expense_classes[category](amount, date)
class FoodExpense(Expense):
    def to_dict(self):
        return {'amount': self.amount, 'category': 'Food', 'date': self.date}
class TransportExpense(Expense):
    def to_dict(self):
        return {'amount': self.amount, 'category': 'Transport', 'date': self.date}
class ActivityExpense(Expense):
    def to_dict(self):
        return {'amount': self.amount, 'category': 'Activity', 'date': self.date}
class HealthExpense(Expense):
    def to_dict(self):
        return {'amount': self.amount, 'category': 'Health', 'date': self.date}
