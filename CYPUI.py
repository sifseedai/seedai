import streamlit as st
import requests

# Define the Streamlit app
def main():
    st.title('Crop Yield Prediction')

    # Add input fields for user to enter data
    st.sidebar.header('Enter Data:')
    N = st.sidebar.number_input('Nitrogen (N)', min_value=0)
    P = st.sidebar.number_input('Phosphorus (P)', min_value=0)
    K = st.sidebar.number_input('Potassium (K)', min_value=0)
    temperature = st.sidebar.number_input('Temperature', min_value=0.0)
    humidity = st.sidebar.number_input('Humidity', min_value=0.0)
    ph = st.sidebar.number_input('pH', min_value=0.0)
    rainfall = st.sidebar.number_input('Rainfall', min_value=0.0)

    # When the user clicks the 'Predict' button, perform prediction
    if st.sidebar.button('Predict'):
        # Send HTTP request to FastAPI server
        response = requests.post("http://localhost:8000/predict",
                                params={"N": N, "P": P, "K": K,
                                        "temperature": temperature,
                                        "humidity": humidity, "ph": ph,
                                        "rainfall": rainfall})
        if response.status_code == 200:
            predicted_yield = response.json()["prediction"]
            st.write(f'Predicted Crop Yield: {predicted_yield}')
        else:
            st.error("Failed to get prediction from server.")

if __name__ == '__main__':
    main()
