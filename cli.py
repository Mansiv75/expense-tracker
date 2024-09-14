import argparse
from expense_manager import add_expense, list_expenses, delete_expense, show_summary, export_to_csv

def main():
    parser = argparse.ArgumentParser(description='Expense Tracker CLI')

    subparsers = parser.add_subparsers(dest="command", required=True)

    # 'add' command
    add_parser = subparsers.add_parser('add', help='Add a new expense')
    add_parser.add_argument('--description', required=True, help='Description of the expense')
    add_parser.add_argument('--amount', required=True, type=float, help='Amount of the expense')

    # 'list' command
    list_parser = subparsers.add_parser('list', help='List all expenses')

    # 'delete' command
    delete_parser = subparsers.add_parser('delete', help='Delete an expense')
    delete_parser.add_argument('--id', required=True, type=int, help='ID of the expense to delete')

    # 'summary' command
    summary_parser = subparsers.add_parser('summary', help='Show a summary of expenses')
    summary_parser.add_argument('--month', type=int, help='Month (1-12) to filter expenses by')

    # 'export' command
    export_parser = subparsers.add_parser('export', help='Export expenses to a CSV file')

    args = parser.parse_args()

    if args.command == 'add':
        expense_id = add_expense(args.description, args.amount)
        print(f"Expense added successfully (ID: {expense_id})")
    elif args.command == 'list':
        expenses = list_expenses()
        for expense in expenses:
            print(f"{expense['id']:<5} {expense['date']:<10} {expense['description']:<15} ${expense['amount']:<7.2f}")
    elif args.command == 'delete':
        if delete_expense(args.id):
            print("Expense deleted successfully.")
        else:
            print("Expense ID not found.")
    elif args.command == 'summary':
        total = show_summary(args.month)
        if args.month:
            print(f'Total expenses for month {args.month} = ${total:.2f}')
        else:
            print(f'Total expenses = ${total:.2f}')
    elif args.command == 'export':
        export_to_csv()
        print('Expenses exported to "expenses.csv" successfully')

if __name__ == '__main__':
    main()
