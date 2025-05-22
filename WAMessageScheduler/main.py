# step-1 install required libraries
from twilio.rest import Client
from datetime import datetime,timedelta
import time

# step-2 Twilio Credentials
account_sid = "AC6073bf0a30ae527cdfa5cfb56ccf44e3"
auth_token = "1819feb9fdd58ae0dcc8ef3336fc1894"

client = Client(account_sid, auth_token)

# step-3 define send message function
def send_whatsapp_message(recipient_number,message_body):
    try:
        client.messages.create(
            from_='whatsapp:+14155238886',
            body=message_body,
            to=f"whatsapp:{recipient_number}"
        )
        print(f'Message sent successfully! Message {recipient_number}')
    except Exception as e:
        print(f"An error occured {e}")

#  step-4 user input
name = input("Enter the recipient name : ")
recipient_number = input("Enter the recipient number with country code (e.g, +917020903497) : ")
message_body = input(f"Enter the message you want to send to {name} : ")

# step-5 parse date time and calculate delay
date_str = input("Enter the date to send the message (YYYY-MM-DD) : ")
time_str = input("Enter the time to send the message (HH-MM in 24hr format) : ")

# datetime
schedule_datetime = datetime.strptime(f"{date_str} {time_str}","%Y-%m-%d %H:%M")  #strp = string pass time
current_datetime = datetime.now()

# calculate delay
time_difference = schedule_datetime - current_datetime
delay_seconds = time_difference.total_seconds()

if delay_seconds <= 0:
    print("Oops! The selected time has already passed.Please choose a future date and time to continue.")
else:
    print(f"Message scheduled to be sent to {name} at {schedule_datetime}.")

    # wait until the scheduled time
    time.sleep(delay_seconds)

    # send the message
    send_whatsapp_message(recipient_number,message_body)