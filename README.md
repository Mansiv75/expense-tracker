
# Expense Tracker

A simple command-line application for tracking expenses. This application allows users to add, list, delete, and summarize their expenses. Additionally, users can export their expenses to a CSV file for further analysis.

~ Features

- Add a new expense with a description and amount.
- List all recorded expenses.
- Delete an expense by its ID.
- View a summary of all expenses or expenses for a specific month.
- Export all expenses to a CSV file.

~ Requirements

- Python 3.x

~ Installation

1. Clone the repository:

    ```
    git clone https://github.com/yourusername/expense-tracker.git
    ```

2. Navigate to the project directory:

    ```
    cd expense-tracker
    ```

3. No additional libraries are required beyond Python’s standard library.

~ Usage

* Add a New Expense

To add a new expense, use the following command:

```
python one.py add --description "Description of the expense" --amount Amount
```
```
python one.py add --description "Lunch" --amount 15.50
```

* List All Expenses

To list all recorded expenses, use:

```
python one.py list
```

* Delete an Expense

To delete an expense, use the following command with the expense ID:

```
python one.py delete --id ExpenseID
```
```
python one.py delete --id 1
```

* View Summary

To view the summary of all expenses, use:

```
python one.py summary
```

To view the summary of expenses for a specific month, use:

```
python one.py summary --month MonthNumber
```
```
python one.py summary --month 8
```

* Export Expenses to CSV

To export all expenses to a CSV file, use:

```
python one.py export
```

This will create a file named `expenses.csv` in the current directory.

~ File Storage

- Expenses are stored in a file named `expenses.txt` in JSON format.
- The export functionality creates a `expenses.csv` file with the recorded expenses.

~ Contributing

Feel free to fork the repository and make improvements. Please open an issue or submit a pull request with any changes or enhancements.

