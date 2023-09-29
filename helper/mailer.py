import os
import smtplib
import re

class EMailException(Exception):
    """
    Email Exception gets thrown when an email could not be sent.
    """

class Mailer:
    
    def __init__(self) -> bool:
        self.from_address = os.environ.get("FROM_ADDRESS")
        self.to_address = os.environ.get("TO_ADDRESS")
        self.password = os.environ.get("PASSWORD")

    def send_mail(self, name: str, email: str, message: str) -> None:
        
        message = f"From: {self.from_address}\r\nTo: {self.to_address}\r\nSubject: Message from website\r\n\r\nName: {name}\nE-Mail: {email}\nMessage: {message}"

        smtp_obj = smtplib.SMTP("smtp.mail.me.com", 587)
        smtp_obj.starttls()
        smtp_obj.login(self.from_address, self.password)

        try:
            send_status = smtp_obj.sendmail(from_addr=self.from_address, to_addrs=self.to_address, msg=message)
            if send_status != {}:
                raise EMailException("There was an error sending the email")

        except Exception:
            return False

        finally:
            smtp_obj.quit()
            return True

    
    def check_validity(email: str) -> bool:
        pattern = r"^\S+@\S+\.\S+$"

        if re.match(pattern, email):
            return True

        return False
