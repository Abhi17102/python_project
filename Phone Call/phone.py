import streamlit as st
from twilio.rest import Client

# Streamlit page config
st.set_page_config(page_title="📞 Twilio Voice Caller", page_icon="📞", layout="centered")

# App title and description
st.title("📞 Twilio Voice Caller")
st.markdown(
    """
    Make real-time voice calls using [Twilio](https://www.twilio.com/) API.  
    > 🔐 Enter your Twilio credentials and the message to be spoken during the call.
    ---
    """
)

# Voice Call Form
st.subheader("📞 Make a Call")

with st.form("call_form"):
    call_sid = st.text_input("🔑 Twilio SID", type="password")
    call_token = st.text_input("🔐 Twilio Auth Token", type="password")
    call_from = st.text_input("📞 Twilio Phone Number (with +country code)")
    call_to = st.text_input("📲 Recipient Phone Number (with +country code)")
    call_msg = st.text_area("🗣️ Message to Speak", value="Hello! This is a Python-Twilio call. Have a great day!")

    call_submit = st.form_submit_button("📞 Make Call")

    if call_submit:
        if all([call_sid, call_token, call_from, call_to, call_msg]):
            try:
                client = Client(call_sid, call_token)
                twiml = f'<Response><Say>{call_msg}</Say></Response>'
                call = client.calls.create(
                    to=call_to,
                    from_=call_from,
                    twiml=twiml
                )
                st.success(f"✅ Call initiated successfully!\nCall SID: `{call.sid}`")
            except Exception as e:
                st.error(f"❌ Failed to make the call:\n`{e}`")
        else:
            st.warning("⚠️ Please fill in all fields before making the call.")
