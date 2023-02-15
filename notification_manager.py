from twilio.rest import Client
import smtplib
TWILIO_SID='AC0739f387a4f6e5b58a31688301672b1f'
TWILIO_AUTH_TOKEN='b415740eca24c92b3c39af5505f5a2ef'
TWILIO_VIRTUAL_NUMBER='+19403704292'
TWILIO_VERIFIED_NUMBER='+16142560712'
MAIL_PROVIDER_SMTP_ADDRESS = "smtp.gmail.com"
MY_EMAIL ='sameeranati@gmail.com'
MY_PASSWORD = 'psjg rozj sjcl pshg'

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    
    
    def send_emails(self,emails,message,link):
        with smtplib.SMTP(MAIL_PROVIDER_SMTP_ADDRESS) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}\n{link}".encode('utf-8')
                )
       