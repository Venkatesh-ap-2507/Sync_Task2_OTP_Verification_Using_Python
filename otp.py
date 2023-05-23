import tkinter as tk
import smtplib
import random


otp = str(random.randint(200000,999999))

smtp_server = "smtp.gmail.com"
port = 587  # For starttls
sender_email = "venkateshpensalwar561@gmail.com"
password = "dqulnfwhvbdlghmx"
receiver_email = ""

def send_email():
    global otp, receiver_email

    receiver_email = email_entry.get()
    message = f"Subject: OTP Verification\n\n OTP is {otp}"
    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

def verify_otp():
    user_input = otp_entry.get()
    if user_input == otp:
        result_label.config(text="OTP verified")
    else:
        result_label.config(text="OTP Not verified")

root = tk.Tk()
root.geometry("300x200")

email_label = tk.Label(root, text="Enter your email:")
email_label.pack()

email_entry = tk.Entry(root)
email_entry.pack()

send_button = tk.Button(root, text="Send OTP", command=send_email)
send_button.pack()

otp_label = tk.Label(root, text="Enter OTP:")
otp_label.pack()

otp_entry = tk.Entry(root)
otp_entry.pack()

verify_button = tk.Button(root, text="Verify OTP", command=verify_otp)
verify_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()