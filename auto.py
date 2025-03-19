import smtplib

# Gmail login credentials
EMAIL = "your_email@gmail.com"
PASSWORD = "your_app_password"  # Use the generated App Password

# Set up SMTP server
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()  # Secure connection
server.login(EMAIL, PASSWORD)  # Log in to Gmail

# Email details
to_email = "receiver_email@gmail.com"
subject = "Test Email"
body = "Hello! This is a test email sent from Python. 📩"

# Format email message
message = f"Subject: {subject}\n\n{body}"

# Send email
server.sendmail(EMAIL, to_email, message)
print("Email sent successfully!")

# Close connection
server.quit()
