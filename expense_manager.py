import os
import json
import csv
from datetime import datetime

def get_next_id():
    if os.path.exists('expenses.txt'):
        with open('expenses.txt', 'r') as file:
            expenses = json.load(file)
            if expenses:
                return expenses[-1]['id'] + 1
    return 1

def add_expense(description, amount):
    if amount <= 0:
        raise ValueError("Amount should be greater than zero.")
    
    expense = {
        'id': get_next_id(),
        'date': datetime.now().strftime('%Y-%m-%d'),
        'description': description,
        'amount': amount
    }

    if os.path.exists('expenses.txt'):
        with open('expenses.txt', 'r') as file:
            expenses = json.load(file)
    else:
        expenses = []

    expenses.append(expense)

    with open('expenses.txt', 'w') as file:
        json.dump(expenses, file, indent=4)

    return expense['id']

def list_expenses():
    if os.path.exists('expenses.txt'):
        with open('expenses.txt', 'r') as file:
            expenses = json.load(file)
        return expenses
    else:
        return []

def delete_expense(expense_id):
    if os.path.exists('expenses.txt'):
        with open('expenses.txt', 'r') as file:
            expenses = json.load(file)

        updated_expenses = [expense for expense in expenses if expense['id'] != expense_id]

        if len(updated_expenses) < len(expenses):
            with open('expenses.txt', 'w') as file:
                json.dump(updated_expenses, file, indent=4)
            return True
        else:
            return False
    else:
        return False

def show_summary(month=None):
    expenses = list_expenses()
    total = 0
    if month:
        for expense in expenses:
            expense_month = int(expense['date'].split('-')[1])
            if expense_month == month:
                total += expense['amount']
    else:
        for expense in expenses:
            total += expense['amount']
    return total

def export_to_csv():
    expenses = list_expenses()
    with open('expenses.csv', 'w', newline='') as csvfile:
        fieldnames = ['ID', 'Date', 'Description', 'Amount']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for expense in expenses:
            writer.writerow({
                'ID': expense['id'],
                'Date': expense['date'],
                'Description': expense['description'],
                'Amount': expense['amount']
            })
