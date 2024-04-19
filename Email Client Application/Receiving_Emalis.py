import imaplib
import email
from plyer import notification

def receive_email(receiver_email, receiver_password):
    imap_server = None

    # Try to open a connection and retrieve the email
    print("\nReceiver Side: Reading latest email...")
    try:
        # Connect to the IMAP server
        imap_server = imaplib.IMAP4_SSL('imap.gmail.com') 
        imap_server.login(receiver_email, receiver_password) # Login to the IMAP server
        
        # Select the mailbox (inbox)
        imap_server.select('INBOX') 
        _, data = imap_server.search(None, 'ALL') # Retrieve all emails from the mailbox
        latest_email_id = data[0].split()[-1] # Get the latest email id
        # Fetch the latest email
        _, email_data = imap_server.fetch(latest_email_id, '(RFC822)') # RFC822: Standard format of text messages
        # Parse the email data
        raw_email = email_data[0][1]
        email_message = email.message_from_bytes(raw_email)
        
        subject = email_message['Subject']
        from_ = email_message['From']

        
        # Send a push notification
        notification_title = "New Email Received"
        notification_text = f"Subject: {subject}\nFrom: {from_}"

        notification.notify(
            title=notification_title,
            message=notification_text,
            app_name="Email Client Application"
        )

        # Print the email body
        for part in email_message.walk(): # Loop over the message parts
            if part.get_content_type() == "text/plain": # Check for the plain text part of the message
                received_message = part.get_payload(decode=True).decode('utf-8')
                print(f"Latest Email Body: {received_message}") # Decode the text and print it
    
    # Raise error if an error occurred
    except Exception as e:
        print("Error:", e)

    # Logout from the email
    finally:
        if imap_server:
            imap_server.logout()

    return received_message