import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(sender_email, sender_password, recipient_email, subject, body):
    smtp_server = None
    
    # Try to open a connection and send the email
    print("\nSender Side: Sending Email...")
    try:
        # Connect to the SMTP server
        smtp_server = smtplib.SMTP('smtp.gmail.com', 587) # 587: The default port number to open connection using starttls
        smtp_server.starttls()
        smtp_server.login(sender_email, sender_password) # Login to the SMTP server

        # Create a multipart message
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = recipient_email
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain')) # Add body to the email (plain text)

        # Send the email
        smtp_server.send_message(message)
        print("Email sent successfully!")

    # Raise error if an error occurred
    except Exception as e: 
        print("Error:", e)

    # Close the connection
    finally:
        if smtp_server:
            smtp_server.quit() 