import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
import re
import logging

# Setup logging
logging.basicConfig(filename='email_reminder.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def send_email(subject, body, to):
    from_email = os.getenv("EMAIL_USER")
    from_password = os.getenv("EMAIL_PASS")

    if not from_email or not from_password:
        raise ValueError("Email credentials are not set. Please set EMAIL_USER and EMAIL_PASS environment variables.")

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'html'))

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(from_email, from_password)
            server.sendmail(from_email, to, msg.as_string())
        logging.info(f"Reminder sent successfully to {to}")
    except Exception as e:
        logging.error(f"Failed to send email to {to}: {e}")
        raise

def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None

def assignment_reminder():
    print("Welcome to the Assignment Reminder!")
    
    email = input("Enter student's email: ").strip()
    if not is_valid_email(email):
        print("Invalid email address. Exiting.")
        return

    assignment = input("Enter assignment name: ").strip()
    due_date = input("Enter due date (YYYY-MM-DD): ").strip()

    subject = f"Reminder: {assignment} due on {due_date}"
    body = (f"<html><body><p>Dear student,</p>"
            f"<p>This is a reminder that your assignment '{assignment}' is due on {due_date}.</p>"
            f"<p>Best regards,<br>Your Teacher</p></body></html>")

    try:
        send_email(subject, body, email)
        print("Reminder sent successfully.")
    except Exception as e:
        print(f"Error sending email: {e}")

if __name__ == "__main__":
    assignment_reminder()
