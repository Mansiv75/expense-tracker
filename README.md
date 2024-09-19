#Expense Tracker

This repository contains two implementations of an Expense Tracker:
1. CLI (Command-Line Interface) Application for managing expenses via terminal commands.
2. API (Application Programming Interface) for managing expenses programmatically, including user authentication with JWT.

## Table of Contents
-Introduction
-CLI Application
  -Features
  -Usage
-API Application
  -Features
  -Endpoints
  -Usage
-Installation
-Testing-Screenshots/Video Demosts
-Contributing
-License
---

## Introduction
The Expense Tracker allows users to:
- Add, list, delete, and summarize expenses.
- Authenticate using JWT (for API).
- Manage expenses via CLI or HTTP requests.

## CLI Application

### CLI Features
- Add Expense: Add a new expense with a date, description, and amount.
- List Expenses: Display all expenses.
- Delete Expense: Remove an expense by its ID.
- Summarize Expenses: Get a total expense for a specific month or overall.
- Export Expenses: Export data to CSV format.

### CLI Usage
To use the CLI app:
1. Run the `expense-manager.py` to start managing expenses:
    ```
    python expense-manager.py --help
    ```
2. Example commands:
    - Add an expense:
      ```
      python expense-manager.py add --description "Groceries" --amount 50
      ```
    - List all expenses:
      ```
      python expense-manager.py list
      ```
    - Delete an expense:
      ```
      python expense-manager.py delete --id 1
      ```

## API Application

### API Features
- User Signup & Login: Authenticate via JWT tokens.
- Add Expense: Create a new expense linked to a user.
- List Expenses: Retrieve all expenses of an authenticated user.
- Delete Expense: Remove an expense by ID.
- Summary: Show the total expenses for a specific month or overall.

### API Endpoints
| Endpoint           | Method  | Description                                |
|--------------------|---------|--------------------------------------------|
| `/api/users`       | POST    | Register a new user                        |
| `/api/login`       | POST    | Log in and receive a JWT token             |
| `/api/expenses`    | POST    | Add a new expense (JWT required)           |
| `/api/expenses`    | GET     | List all expenses (JWT required)           |
| `/api/expenses/<id>` | DELETE | Delete an expense by ID (JWT required)     |
| `/api/summary`     | GET     | Show total expenses for a specific month   |

### API Usage
1. Signup: 
    ```
    POST /api/users
    {
      "username": "john_doe",
      "password": "secret_password"
    }
    ```

2. Login:
    ```
    POST /api/login
    {
      "username": "john_doe",
      "password": "secret_password"
    }
    ```

3. Add Expense:
    ```
    POST /api/expenses
    {
      "description": "Lunch",
      "amount": 15.00
    }
    ```

4. List Expenses:
    ```
    GET /api/expenses
    ```

5. Delete Expense:
    ```
    DELETE /api/expenses/1
    ```

6. Summary:
    ```
    GET /api/summary?month=9
    ```

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/YourUsername/expense-tracker.git
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up the database:
   - For API:
     ```
     python -m flask create-db
     ```

## Testing
You can manually test the API using tools like Postman or cURL.

### CLI Testing
Run the following commands to test the CLI application:
- Add expenses, list them, delete, or get summaries through `expense-manager.py`.

### API Testing
Use Postman to:
- Signup new users.
- Log in to retrieve the JWT token.
- Perform the expense management operations.

---

