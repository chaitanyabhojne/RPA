from HDFC import HDFCOperations

class BankOperations:
    def __init__(self, bank_name, transaction_type, no_of_days):
        self.bank_name = bank_name
        self.transaction_type = transaction_type
        self.no_of_days = no_of_days
        self.debit_subject = "You have done a UPI txn. Check details!"
        self.credit_subject = "View: Account update for your HDFC Bank A/c"

    def get_bank_transaction_details(self):
        hdfc_ops = HDFCOperations()
        if self.bank_name == "HDFC":
            if self.transaction_type == 'debited':
                return hdfc_ops.get_HDFC_details(self.transaction_type, self.no_of_days, self.debit_subject)
            if self.transaction_type == 'credited':
                return hdfc_ops.get_HDFC_details(self.transaction_type, self.no_of_days, self.credit_subject)
        else:
            print(f"Bank '{self.bank_name}' is not supported.")
            return []