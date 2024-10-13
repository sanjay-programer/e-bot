import streamlit as st
from helper import user_chat

# Page configuration
st.set_page_config(page_title="SAN-BOT", layout="wide")

# Header
st.title("SAN-BOT: Your Product Assistant")

# Main content layout
query = st.text_input("Ask your question:")

if query:
    # Spinner for better UX
    with st.spinner("Fetching response..."):
        output = user_chat(query)

    # Displaying the result
    st.write("## Results:")
    st.write(output)

# Footer
st.write("---")
st.write("Powered by **SAN-BOT**")
