import streamlit as st

def page2():
    st.title("Page 2")
    st.write("Welcome to Page 2 of the Streamlit app!")
    st.write("Here you can add more content specific to this page.")
    
    # Example of adding a simple input and button
    user_input = st.text_input("Enter some text:")
    if st.button("Submit"):
        st.write(f"You entered: {user_input}")

if __name__ == "__main__":
    page2()