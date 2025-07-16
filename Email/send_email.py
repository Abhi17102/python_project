import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Title
st.title("📧 Gmail Email Sender")

# User input fields
receiver_email = st.text_input("Recipient Email")
subject = st.text_input("Subject")
body = st.text_area("Message")

# Gmail credentials (NOTE: Use environment variables or secrets in production)
sender_email = "your_senderid@gmail.com"
app_password = "your_gmail_app_pasword"  # Use 16-digit Gmail App Password

# Send email when button is clicked
if st.button("Send Email"):
    if not receiver_email or not subject or not body:
        st.warning("⚠️ Please fill in all fields.")
    else:
        try:
            # Compose the email
            message = MIMEMultipart()
            message["From"] = sender_email
            message["To"] = receiver_email
            message["Subject"] = subject
            message.attach(MIMEText(body, "plain"))

            # Send the email
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(sender_email, app_password)
            server.sendmail(sender_email, receiver_email, message.as_string())
            server.quit()

            st.success("✅ Email sent successfully!")

        except Exception as e:
            st.error(f"❌ Failed to send email: {e}")
