from email_operations import EmailOperations
from bs4 import BeautifulSoup

class HDFCOperations:
    def __init__(self):
        self.bank_name = "HDFC"
    
    # This method fetches debit transaction details from HDFC bank emails based on the specified transaction type, number of days, and subject keyword
    def get_HDFC_details(self, transaction_type, no_of_days, subject_keyword):
        email_ops = EmailOperations(self.bank_name, transaction_type, no_of_days, subject_keyword)
        email_body = email_ops.fetch_emails()
        transaction_details = []
        for email in email_body:
            alert_details = self.get_data_by_class(email, "td esd-text")
            if transaction_type == 'debited':
                transaction_details.append(self.extract_debited_transaction_details(alert_details))
            if transaction_type == 'credited':
                transaction_details.append(self.extract_credited_transaction_details(alert_details))
        return transaction_details

    # This method extracts data by class from the email body using BeautifulSoup
    def get_data_by_class(self, email_body, class_name):
        soup = BeautifulSoup(email_body, "html.parser")
        elements = soup.find_all(class_=class_name)
        return [element.get_text(strip=True) for element in elements]
    
    # This method extracts transaction details such as amount, transaction type, sender/receiver, and date from the alert details
    def extract_debited_transaction_details(self, alert_details):
        details = {}
        for detail in alert_details:
            if "Rs." in detail:
                details["Amount"] = detail.split("Rs.")[1].split(' ')[0].strip()
            if "debited" in detail:
                details["TransactionType"] = 'Debited'
            if "towards" in detail:
                details["From"] = detail.split("towards")[1].split(' on')[0].strip()
            if "on" in detail:
                details["Date"] = detail.split(" on ")[1].split('.')[0].strip()
                
        return details
    # This method extracts credited transaction details such as amount, transaction type, sender/receiver, and date from the alert details
    def extract_credited_transaction_details(self, alert_details):
        details = {}
        for detail in alert_details:
            if "Rs." in detail:
                details["Amount"] = detail.split("Rs.")[1].split(' ')[0].strip()
            if "credited" in detail:
                details["TransactionType"] = 'Credited'
            if "from" in detail:
                details["From"] = detail.split(" Sender: ")[1].split('c.')[0].strip()
            if "Date" in detail:
                details["Date"] = detail.split(" Date: ")[1].split('b.')[0].strip()
                
        return details