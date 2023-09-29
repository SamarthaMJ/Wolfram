import streamlit as st
import requests

# Set your Wolfram Alpha API key here
WOLFRAM_ALPHA_API_KEY = "ERT5E3-4HPGR2XXH8"

st.title("Wolfram Alpha Question Answerer")

# Create a text input for the user to enter their question
question = st.text_input("Enter your question:")

# Create a button to submit the question
if st.button("Get Answer"):
    if question:
        # Define the Wolfram Alpha API URL
        api_url = "http://api.wolframalpha.com/v2/query"

        # Define parameters for the API request
        params = {
            "input": question,
            "format": "plaintext",
            "output": "JSON",
            "appid": WOLFRAM_ALPHA_API_KEY,
        }

        try:
            # Send the API request
            response = requests.get(api_url, params=params)
            data = response.json()

            # Extract and display the answer
            pods = data.get("queryresult", {}).get("pods", [])
            for pod in pods:
                if pod["title"] == "Result":
                    answer = pod["subpods"][0]["plaintext"]
                    st.write(f"Answer: {answer}")
                    break
            else:
                st.write("No answer found.")

        except Exception as e:
            st.error(f"Error: {str(e)}")

    else:
        st.warning("Please enter a question.")
