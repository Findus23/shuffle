import smtplib
from email.mime.text import MIMEText

from config import sender

s = smtplib.SMTP('localhost')


def notify(name: str, email: str, chosen_person: str) -> None:
    to = f"{name} <{email}>"

    msg = MIMEText(f"Hello {name},\n\nThe chosen person is {chosen_person}.")
    msg['Subject'] = f"Result of shuffle for {name}"
    msg['From'] = sender
    msg['To'] = to
    print(msg.as_string())
    s.sendmail(sender, [to], msg.as_string())
