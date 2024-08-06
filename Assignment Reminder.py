#Assignment Reminder
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(subject, body, to):
    from_email = "your_email@example.com"
    from_password = "your_password"

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, from_password)
    text = msg.as_string()
    server.sendmail(from_email, to, text)
    server.quit()

def assignment_reminder():
    print("Welcome to the Assignment Reminder!")
    email = input("Enter student's email: ")
    assignment = input("Enter assignment name: ")
    due_date = input("Enter due date (YYYY-MM-DD): ")

    subject = f"Reminder: {assignment} due on {due_date}"
    body = f"Dear student,\n\nThis is a reminder that your assignment '{assignment}' is due on {due_date}.\n\nBest regards,\nYour Teacher"
    
    send_email(subject, body, email)
    print("Reminder sent successfully.")

if __name__ == "__main__":
    assignment_reminder()
