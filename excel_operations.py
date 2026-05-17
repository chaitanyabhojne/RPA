from openpyxl import workbook
from datetime import datetime
from logging import getLogger

logger = getLogger(__name__)

class ExcelOperations:
    
    def __init__(self, bank_name, transaction_type):
        self.bank_name = bank_name
        self.transaction_type = transaction_type
        self.file_name = f"{bank_name}_{self.transaction_type}_transaction_details_{datetime.now().strftime('%Y-%m-%d')}.xlsx"

    def create_excel_file(self):
        print("Creating Excel file...")
        wb = workbook.Workbook()
        ws = wb.active
        ws.title = f"{self.transaction_type.capitalize()} Transactions"
        ws.append(["Amount", "Transaction Type", "From", "Date"])

        return wb

    def save_transaction_details_to_excel(self, wb, transaction_details):
        ws = wb.active
        print(f"Saving transaction details to Excel file...")
        for detail in transaction_details:
            ws.append(
                [
                    detail.get("Amount", ""),
                    detail.get("TransactionType", ""),
                    detail.get("From", ""),
                    detail.get("Date", "")
                ]
        )
        wb.save(f"{'output/'}{self.file_name}")
        print(f"Saved transaction details to Excel file successfully.")