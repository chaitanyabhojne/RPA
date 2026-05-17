from excel_operations import ExcelOperations
from bank_operations import BankOperations

BANK_NAME = "HDFC"
TRANSACTION_TYPE = ["debited", "credited"]
NO_OF_DAYS = 7

if __name__ == "__main__":
    print("Script started.")
    
    for transaction_type in TRANSACTION_TYPE:
        print(f"Processing {transaction_type} transactions for {BANK_NAME} bank...")
        bank_ops = BankOperations(BANK_NAME, transaction_type, NO_OF_DAYS)
        transaction_details = bank_ops.get_bank_transaction_details()

        if transaction_details:
            excel_ops = ExcelOperations(BANK_NAME, transaction_type)
            excel_file = excel_ops.create_excel_file()
            excel_ops.save_transaction_details_to_excel(excel_file, transaction_details)
        else:
            print("No transaction details found in the emails.")
        print("Script finished.")
    