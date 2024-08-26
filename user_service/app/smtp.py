import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from flask import jsonify


from models import EmailRequest

email = "MS_8LdMsC@trial-0p7kx4xee3eg9yjr.mlsender.net"
password = "vlqrsLaTUDNlU5xU"
apitoken = "mlsn.9b1c08785bb41b1e603ea5d8f6a1d008fabcb1ff86367d9a76c2ac839f1b4088"


def send_email_logic(email_request: EmailRequest):
    try:
        msg = MIMEMultipart()
        msg["From"] = email
        msg["To"] = email_request.receiver_email
        msg["Subject"] = email_request.subject
        msg.attach(MIMEText(email_request.body, "plain"))
        server = smtplib.SMTP("smtp.mailersend.net", 587)
        server.starttls()
        server.login(email, password)
        server.sendmail(email, email_request.receiver_email, msg.as_string())
        server.quit()
        return jsonify({"message": "Email sent successfully"}), 201
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"message": "Email was not sent"}), 500
