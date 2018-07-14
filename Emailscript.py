import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import getpass

PASSWORD = getpass.getpass("EMAIL Account password is:")
SERVER = smtplib.SMTP("smtp.gmail.com","587")
SERVER.starttls()
SERVER.login("premkumar.v@vvdntech.com", PASSWORD)

MESSAGE = MIMEMultipart()

SENDER = "premkumar.v@vvdntech.com"
RECEIVER = "premkumar.v@vvdntech.com"
MESSAGE["From"] = SENDER
MESSAGE["To"] = RECEIVER
MESSAGE["Subject"] = "Python Email"

SIGNATURE = """-- 
Thanks & Regards,
Premkumar.V
VVDN Technologies Pvt. Ltd.
Cell : +91-9042742637 | Skype : prem.varadharajan"""

MESSAGE.attach(MIMEText("Hi Team, \r\n \r\nPlease find the test report below. \r\n \n\n %s" %SIGNATURE , "plain"))

filename = "test1.txt"
f = file(filename)
attachment = MIMEText(f.read())
attachment.add_header('Content-Disposition', 'attachment', filename=filename)
MESSAGE.attach(attachment)

TEXT = MESSAGE.as_string()

try:

	SERVER.sendmail(SENDER, RECEIVER, TEXT)
        print "Email is send to receipent successfully"

except:
 	print "This script failed to send the Email"

SERVER.quit()
