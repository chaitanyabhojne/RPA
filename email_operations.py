import imaplib
import email
import json
from datetime import datetime, timedelta

class EmailOperations:
    
    def __init__(self, bank_name=None, transaction_type=None, no_of_days=None, subject_keyword=None):
        self.bank_name = bank_name
        self.transaction_type = transaction_type
        self.no_of_days = no_of_days
        self.subject_keyword = subject_keyword
    
    # This method reads email credentials from a JSON file named 'cred.json' and returns them as a dictionary
    def read_credentials(self):
        with open('cred.json', 'r') as file:
            credentials = json.load(file)
        return credentials

    # This method extracts the email body, handling both plain text and HTML formats
    def get_email_body(self, msg):
        if msg.is_multipart():
            for part in msg.walk():
                content_type = part.get_content_type()
                content_disposition = str(part.get("Content-Disposition"))

                if content_type == "text/plain" and "attachment" not in content_disposition:
                    return part.get_payload(decode=True).decode(
                        part.get_content_charset() or "utf-8",
                        errors="replace"
                    )

            for part in msg.walk():
                content_type = part.get_content_type()
                content_disposition = str(part.get("Content-Disposition"))

                if content_type == "text/html" and "attachment" not in content_disposition:
                    return part.get_payload(decode=True).decode(
                        part.get_content_charset() or "utf-8",
                        errors="replace"
                    )
        else:
            return msg.get_payload(decode=True).decode(
                msg.get_content_charset() or "utf-8",
                errors="replace"
            )

        return ""

    def fetch_emails(self):
        print("Fetching emails...")
        cred = self.read_credentials()
        mail = imaplib.IMAP4_SSL('imap.gmail.com')
        mail.login(cred['email_address'], cred['app_password'])
        mail.select('inbox')
        
        SUBJECT_KEYWORD = self.subject_keyword
        SINCE_DATE = (datetime.now() - timedelta(days=self.no_of_days)).strftime("%d-%b-%Y")

        result, data = mail.search(None, f'(SINCE "{SINCE_DATE}" SUBJECT "{SUBJECT_KEYWORD}")')
        
        if result != "OK":
            raise RuntimeError("Search failed")

        email_ids = data[0].split()

        email_body = []

        for email_id in email_ids:
            status, msg_data = mail.fetch(email_id, '(RFC822)')
            
            if status != "OK":
                print(f"Failed to fetch email with ID {email_id}")
                continue
            
            raw_email = msg_data[0][1]
            email_message = email.message_from_bytes(raw_email)
            
            email_body.append(self.get_email_body(email_message))

        mail.logout()
        print(f"Email Fetched.")
        return email_body