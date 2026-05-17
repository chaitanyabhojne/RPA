# HDFC Email Transaction RPA

This small RPA project fetches recent HDFC bank transaction alert emails from a Gmail account, extracts debit/credit details, and saves them to an Excel file in the `output/` folder.

**Prerequisites**
- **Python**: 3.8 or newer
- **Packages**: install the HTML parsing and Excel libraries:

```
pip install beautifulsoup4 openpyxl
```

**Setup**
- **Credentials**: update [cred.json](cred.json) with your Gmail address and an app-specific password (the code reads `email_address` and `app_password`). Ensure IMAP is enabled for the Gmail account.

**Usage**
- Run the script:

```
python main.py
```

- The script processes both `debited` and `credited` alerts (configurable in `main.py`) for the last N days and writes an Excel file to the `output/` directory.

**Files**
- **main.py**: entry point that coordinates bank processing and Excel export ([main.py](main.py)).
- **bank_operations.py**: high-level bank orchestration for supported banks ([bank_operations.py](bank_operations.py)).
- **HDFC.py**: HDFC-specific parsing logic using BeautifulSoup ([HDFC.py](HDFC.py)).
- **email_operations.py**: IMAP email fetcher that reads `cred.json` and returns message bodies ([email_operations.py](email_operations.py)).
- **excel_operations.py**: creates and saves Excel workbooks using `openpyxl` ([excel_operations.py](excel_operations.py)).
- **cred.json**: JSON file holding email credentials (not checked into remote repos; keep it secret) ([cred.json](cred.json)).
- **output/**: destination folder for generated Excel files.

**Notes & Tips**
- Use a Gmail app password (not your main password) and enable IMAP in Gmail settings.
- The parsing logic assumes HDFC email templates; results may vary if the email format changes.
- If you want to add support for other banks, implement a new operations class and call it from `bank_operations.py`.

If you want, I can also add a `requirements.txt`, improve error handling, or add unit tests next.

