import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from flask import jsonify


from app.models import EmailRequest
import os

email = os.getenv("email_smtp")
password_smtp = os.getenv("password_smtp")
apitoken_smtp = os.getenv("apitoken_smtp")


def send_email_logic(email_request: EmailRequest):
    try:
        msg = MIMEMultipart()
        msg["From"] = email
        msg["To"] = email_request.receiver_email
        msg["Subject"] = email_request.subject
        msg.attach(MIMEText(email_request.body, "plain"))
        server = smtplib.SMTP("smtp.mailersend.net", 587)
        server.starttls()
        server.login(email, password_smtp)
        server.sendmail(email, email_request.receiver_email, msg.as_string())
        server.quit()
        return jsonify({"message": "Email sent successfully"}), 201
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"message": "Email was not sent"}), 500
