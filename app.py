import streamlit as st
import pandas as pd
from whatsapp_sender import init_driver, login_to_whatsapp, send_whatsapp_message, close_driver

st.title("WhatsApp Message Sender")

st.markdown("""
1. Upload a CSV file with `name` and `mobile_number` columns.
2. Enter the message you want to send.
3. Click the "Send Messages" button to send the message to all contacts.
""")

uploaded_file = st.file_uploader("Upload CSV", type=["csv"])
message = st.text_area("Enter your message", "Hello, this is a test message!")

if uploaded_file is not None and message:
    df = pd.read_csv(uploaded_file)
    
    if 'name' in df.columns and 'mobile_number' in df.columns:
        st.dataframe(df)
        
        if st.button("Send Messages"):
            driver = init_driver()
            login_to_whatsapp(driver)
            
            for index, row in df.iterrows():
                contact = str(row['mobile_number'])
                try:
                    send_whatsapp_message(driver, contact, message)
                    st.success(f"Message sent to {row['name']} ({contact})")
                except Exception as e:
                    st.error(f"Failed to send message to {row['name']} ({contact}). Error: {e}")
            
            close_driver(driver)
    else:
        st.error("CSV file must contain 'name' and 'mobile_number' columns.")
