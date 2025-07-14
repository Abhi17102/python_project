# app.py

import streamlit as st

# Page Configuration
st.set_page_config(page_title="📡 All-in-One Communication Hub", layout="wide")

# Sidebar Menu
st.sidebar.title("📋 Communication Tools")
menu = st.sidebar.radio("Choose a Utility", [
    "📧 Gmail Email Sender",
    "📸 Instagram Photo Uploader",
    "📞 Twilio Voice Caller",
    "📩 Twilio SMS Sender",
    "💬 WhatsApp Group Message"
])

# ==============================
# 1. Gmail Email Sender Section
# ==============================
if menu == "📧 Gmail Email Sender":
    import smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart

    st.title("📧 Gmail Email Sender")
    st.markdown("Send emails using Gmail and App Password")

    receiver_email = st.text_input("Recipient Email")
    subject = st.text_input("Subject")
    body = st.text_area("Message")

    sender_email = st.text_input("Sender Gmail Address", value="dhabhaiabhi10a@gmail.com")
    app_password = st.text_input("Gmail App Password", type="password")

    if st.button("Send Email"):
        if not receiver_email or not subject or not body or not app_password:
            st.warning("⚠️ Please fill in all fields.")
        else:
            try:
                message = MIMEMultipart()
                message["From"] = sender_email
                message["To"] = receiver_email
                message["Subject"] = subject
                message.attach(MIMEText(body, "plain"))

                server = smtplib.SMTP("smtp.gmail.com", 587)
                server.starttls()
                server.login(sender_email, app_password)
                server.sendmail(sender_email, receiver_email, message.as_string())
                server.quit()

                st.success("✅ Email sent successfully!")
            except Exception as e:
                st.error(f"❌ Failed to send email: {e}")

# ==============================
# 2. Instagram Photo Uploader
# ==============================
elif menu == "📸 Instagram Photo Uploader":
    from instagrapi import Client

    st.title("📸 Instagram Photo Uploader")
    username = st.text_input("Instagram Username")
    password = st.text_input("Instagram Password", type="password")
    photo_path = st.text_input("Path to Image (e.g., E:/Fable.jpg)")
    caption = st.text_area("Caption", value="Posted via Python 🐍")

    if st.button("Upload to Instagram"):
        try:
            cl = Client()
            cl.login(username, password)
            cl.photo_upload(photo_path, caption)
            st.success("✅ Photo uploaded successfully!")
        except Exception as e:
            st.error(f"❌ Upload failed: {e}")

# ==============================
# 3. Twilio Voice Caller
# ==============================
elif menu == "📞 Twilio Voice Caller":
    from twilio.rest import Client

    st.title("📞 Twilio Voice Caller")
    sid = st.text_input("Twilio SID", type="password")
    token = st.text_input("Twilio Auth Token", type="password")
    caller = st.text_input("Twilio Phone Number (with +country code)")
    recipient = st.text_input("Recipient Phone Number (with +country code)")
    message = st.text_area("Message to Speak", value="Hello! This is a Python-Twilio call.")

    if st.button("📞 Make Call"):
        if all([sid, token, caller, recipient, message]):
            try:
                client = Client(sid, token)
                twiml = f"<Response><Say>{message}</Say></Response>"
                call = client.calls.create(to=recipient, from_=caller, twiml=twiml)
                st.success(f"✅ Call initiated successfully!\nCall SID: `{call.sid}`")
            except Exception as e:
                st.error(f"❌ Failed to make the call:\n`{e}`")
        else:
            st.warning("⚠️ Please fill in all fields.")

# ==============================
# 4. Twilio SMS Sender
# ==============================
elif menu == "📩 Twilio SMS Sender":
    from twilio.rest import Client

    st.title("📩 Twilio SMS Sender")
    sid = st.text_input("Twilio SID", type="password")
    token = st.text_input("Twilio Auth Token", type="password")
    twilio_num = st.text_input("Twilio Phone Number (with +country code)")
    recipient = st.text_input("Recipient Phone Number (with +country code)")
    sms_msg = st.text_area("Message", value="Hello from Python, I am PLK!")

    if st.button("🚀 Send SMS"):
        if all([sid, token, twilio_num, recipient, sms_msg]):
            try:
                client = Client(sid, token)
                message = client.messages.create(
                    body=sms_msg,
                    from_=twilio_num,
                    to=recipient
                )
                st.success(f"✅ SMS sent successfully!\nMessage SID: `{message.sid}`")
            except Exception as e:
                st.error(f"❌ SMS failed:\n`{e}`")
        else:
            st.warning("⚠️ Fill all fields before sending.")

# ==============================
# 5. WhatsApp Group Message
# ==============================
elif menu == "💬 WhatsApp Group Message":
    import pywhatkit

    st.title("💬 WhatsApp Group Message Sender")
    group_id = st.text_input("Group ID (Example: 'LW frzi team')")
    msg = st.text_area("Message to Send", value="Hello everyone!")
    hour = st.number_input("Hour (24hr format)", min_value=0, max_value=23, value=10)
    minute = st.number_input("Minute", min_value=0, max_value=59, value=30)

    if st.button("Send WhatsApp Group Message"):
        try:
            pywhatkit.sendwhatmsg_to_group_instantly(group_id, msg, wait_time=10, tab_close=True)
            st.success("✅ Message sent to WhatsApp group!")
        except Exception as e:
            st.error(f"❌ Failed to send WhatsApp message:\n{e}")
