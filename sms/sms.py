import streamlit as st
from twilio.rest import Client

st.set_page_config(page_title="📩 SMS Sender", page_icon="📱", layout="centered")

# Title and Description
st.title("📱 Twilio SMS Sender")
st.markdown(
    """
    Easily send SMS messages using Twilio API.  
    > 🔐 *Enter your credentials securely below.*
    """
)

# SMS Form
st.subheader("📩 Send SMS")

with st.form("sms_form"):
    twilio_sid = st.text_input("🔑 Twilio SID", type="password")
    twilio_token = st.text_input("🔐 Twilio Auth Token", type="password")
    twilio_number = st.text_input("📞 Twilio Phone Number (with +country code)")
    recipient_number = st.text_input("📲 Recipient Phone Number (with +country code)")
    sms_body = st.text_area("✉️ Message Text", value="Hello from Python, I am PLK!")
    
    sms_submit = st.form_submit_button("🚀 Send SMS")

    if sms_submit:
        if all([twilio_sid, twilio_token, twilio_number, recipient_number, sms_body]):
            try:
                client = Client(twilio_sid, twilio_token)
                message = client.messages.create(
                    body=sms_body,
                    from_=twilio_number,
                    to=recipient_number
                )
                st.success(f"✅ SMS sent successfully!\nMessage SID: `{message.sid}`")
            except Exception as e:
                st.error(f"❌ SMS sending failed:\n`{e}`")
        else:
            st.warning("⚠️ Please fill in all the fields before submitting.")
