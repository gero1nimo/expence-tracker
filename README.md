### Expense Manager
#### Overview
A lightweight expense tracker for recording and reporting personal expenses. Designed for local use with a simple cvs file to track and minimal dependencies. The application will automatically create an expenses.csv file if there is not one in directory. Every time the application runs, the program will automatically get the previous expenses from csv file and will automatically save every expense creation or update or delete. 

### Project Link 
https://roadmap.sh/projects/expense-tracker

#### Key Features
- Add, edit, and delete expenses
- Categorization and tagging
- Monthly and category-wise summaries
- CSV import/export
- Simple CLI and minimal GUI (if included)

#### Requirements
- Python 3.8+
- pip

#### Installation
1. Clone the repo:
    git clone <repo-url>
2. Create and activate a virtual environment:
    python -m venv venv
    - Windows: venv\Scripts\activate
    - macOS/Linux: source venv/bin/activate


#### Commands
| Command | Parameters | Description |
|---------|-----------|-------------|
| `--add` | `CATEGORY AMOUNT` | Add a new expense |
| `--list` | -NO-PARAMETERS | List expenses |
| `--summary` | -NO-PARAMETERS | Show all expense summary  |
| `--summary-by-month` | `MONTH NUM` | Show expense summary by month |
| `--delete` | `EXPENSE_ID` | Delete an expense by ID |
| `--update` | `EXPENSE_ID [OPTIONS]` | Edit an existing expense |

#### Running
- Start the application:
  python main.py [--command PARAMETERS]

#### Usage Examples
```bash
python main.py --add "Groceries" 50.00 
python main.py --list --month 2024-01
python main.py --summary 

python main.py --export expenses.csv
python main.py --import expenses.csv
```



