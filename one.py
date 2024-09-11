import argparse
import os
import json
from datetime import datetime
import csv

def main():
    #object is created
    parser = argparse.ArgumentParser(description='Expense Tracker')

    #subparsers are commands that are to be defined

    subparsers = parser.add_subparsers(dest="command", required=True)

    #create a parser for the 'add' command
    add_parser = subparsers.add_parser('add', help='Add a new expense')
    add_parser.add_argument('--description', required=True, help='Description of the expense')
    add_parser.add_argument('--amount', required=True, type=float, help='Amount of the expense')

    #create a parser for the 'list' command
    list_parser = subparsers.add_parser('list', help='List all expenses')

    #create a parser for the 'delete' command
    delete_parser = subparsers.add_parser('delete', help='Delete an expense')
    delete_parser.add_argument('--id', required=True, type=int, help='ID of the expense to delete')

    # Create a parser for the 'summary' command
    summary_parser = subparsers.add_parser('summary', help='Show a summary of expenses')
    summary_parser.add_argument('--month', type=int, help='Month (1-12) to filter expenses by')

    # Create a parser for the 'export' command
    export_parser = subparsers.add_parser('export', help='Export expenses to a CSV file')



    args=parser.parse_args()
    print(args)
    if args.command == 'add':
        add_expense(args.description, args.amount)
    elif args.command == 'list':
        list_expenses()
    elif args.command == 'delete':
        delete_expense(args.id)
    elif args.command == 'summary':
        if(args.month):
            show_summary(month=int(args.month))
        else:
            show_summary()
    elif args.command == 'export':
        export_to_csv()                        

def add_expense(description, amount):
    #create a format for the expense
    if amount<=0:
        print("Amount should be greater than zero.")
        return
    expense={
        
        'id':get_next_id(),
        'date':datetime.now().strftime('%Y-%m-%d'),
        'description':description,
        'amount':amount
    }

    #check if file already exists and load it or create an empty list and 
    if os.path.exists('expenses.txt'):
        with open('expenses.txt', 'r') as file:
            expenses = json.load(file)
    else:
        expenses=[]

    expenses.append(expense)

    #update the file
    with open('expenses.txt', 'w') as file:
        json.dump(expenses, file, indent=4)
    print(f"Expense added successfully(ID:{expense['id']})")

#helper function to get the next id
def get_next_id():
    if os.path.exists('expenses.txt'):
        with open('expenses.txt', 'r') as file: 
            expenses = json.load(file)
            if (expenses):
                return expenses[-1]['id']+1
    return 1                             

def list_expenses():
    if os.path.exists('expenses.txt'):
        with open('expenses.txt', 'r') as file:
            expenses=json.load(file)

            #print header
            print(f"{'ID': <5}{'Date': <10}{'Description':<15}{'Amount':<7}")
            print('-'*37)

            #print each expense
            for expense in expenses:
                print(f"{expense['id']:<5} {expense['date']:<10} {expense['description']:<15} ${expense['amount']:<7.2f}")

    else:
        print("No expenses found.")  
def delete_expense(expense_id):
    if os.path.exists('expenses.txt'):
        with open('expenses.txt', 'r') as file:
            expenses = json.load(file)

            #filter out the expense with the given id
            updated_expenses =[expense for expense in expenses if expense['id']!=expense_id]

            if len(updated_expenses)<len(expenses):
                with open('expenses.txt','w') as file:
                    json.dump(updated_expenses, file, indent=4)
                    print("Expense deleted successfully.")
            else:
                print("Expense ID not found.")

    else:
        print("No expenses found.")                    
def show_summary(month=None):
    if os.path.exists('expenses.txt'):
        with open('expenses.txt', 'r') as file:
            expenses = json.load(file)
        total=0
        if month:
            for expense in expenses:
                expense_month=int(expense['date'].split('-')[1])
                if expense_month==month:
                    total+=expense['amount']
            print(f'Total expenses for month {month}=${total:.2f}')
        else:
            for expense in expenses:
                total+=expense['amount']
            print(f'Total expenses={total:.2f}')

    else:
        print("No expenses found.")
def export_to_csv():
    if os.path.exists('expenses.txt'):
        with open('expenses.txt','r') as file:
            expenses=json.load(file)
        with open('expenses.csv','w', newline='') as csvfile:
            fieldnames=['ID', 'Date','Description','Amount']
            writer=csv.DictWriter(csvfile,fieldnames=fieldnames)
            writer.writeheader()#write the header


            #write each expense as a row in the CSV file
            for expense in expenses:
                writer.writerow({
                    'ID': expense['id'],
                    'Date': expense['date'],
                    'Description': expense['description'],
                    'Amount': expense['amount']
                })  
        print('Expenses exported to "expenses.csv" successfully ')
    else:
        print("No expenses found to export.")                  
                           
                

if __name__ == '__main__':
    main()