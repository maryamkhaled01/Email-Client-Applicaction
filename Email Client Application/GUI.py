import Receiving_Emalis as re
import Sending_Emails as se
import tkinter as tk

def send_email():
    sender_email = sender_email_entry.get()
    sender_password = sender_password_entry.get()
    recipient_email = recipient_email_entry.get()
    subject = subject_entry.get()
    body = body_entry.get('1.0', 'end-1c')
    
    se.send_email(sender_email, sender_password, recipient_email, subject, body)

def receive_email():
    recipient_email = recipient_email_entry.get()
    recipient_password = recipient_password_entry.get()
    
    received_message = re.receive_email(recipient_email, recipient_password)
    received_email_text.delete('1.0', tk.END)  # Clear previous text
    received_email_text.insert(tk.END, received_message)

# Create the main window
window = tk.Tk()
window.title("Email Client Application")
window.geometry("400x550")  # Set window size to 600x400 pixels
window.configure(bg="lightblue") # Set background color

# Create labels and entry widgets for sender email and password
sender_email_label = tk.Label(window, text="Sender Email:", background="lightblue")
sender_email_label.grid(row=0, column=0, sticky="w")
sender_email_entry = tk.Entry(window)
sender_email_entry.grid(row=0, column=1, pady=5, sticky="ew")

sender_password_label = tk.Label(window, text="Sender Password:", background="lightblue")
sender_password_label.grid(row=1, column=0, sticky="w")
sender_password_entry = tk.Entry(window, show="*")
sender_password_entry.grid(row=1, column=1, pady=5, sticky="ew")

# Create labels and entry widgets for recipient email and password
recipient_email_label = tk.Label(window, text="Recipient Email:", background="lightblue")
recipient_email_label.grid(row=2, column=0, sticky="w")
recipient_email_entry = tk.Entry(window)
recipient_email_entry.grid(row=2, column=1, pady=5, sticky="ew")

recipient_password_label = tk.Label(window, text="Recipient Password:", background="lightblue")
recipient_password_label.grid(row=3, column=0, sticky="w")
recipient_password_entry = tk.Entry(window, show="*")
recipient_password_entry.grid(row=3, column=1, pady=5, sticky="ew")

# Create labels and entry widgets for email subject
subject_label = tk.Label(window, text="Subject:", background="lightblue")
subject_label.grid(row=4, column=0, sticky="w")
subject_entry = tk.Entry(window)
subject_entry.grid(row=4, column=1, pady=5, sticky="ew")

# Create labels and entry widgets for email body
body_label = tk.Label(window, text="Body:", background="lightblue")
body_label.grid(row=5, column=0, sticky="w")
body_entry = tk.Text(window, height=8, width=30)
body_entry.grid(row=5, column=1, pady=5, sticky="ew")

# Create buttons to send and receive emails
send_button = tk.Button(window, text="Send Email", command=send_email, background="light sky blue")
send_button.grid(row=6, column=1, pady=5, sticky="ew")

receive_button = tk.Button(window, text="Receive Email", command=receive_email, background="light sky blue", )
receive_button.grid(row=7, column=1, pady=5, sticky="ew")

# Create a text widget to display received email
received_email_text_label = tk.Label(window, text="Received Email:", background="lightblue")
received_email_text_label.grid(row=8, column=0, sticky="w")
received_email_text = tk.Text(window, height=8, width=30)
received_email_text.grid(row=8, column=1, pady=5, sticky="ew")

# Start the GUI event loop
window.mainloop()