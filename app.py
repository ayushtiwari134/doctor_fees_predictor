import numpy as np
import pickle
import streamlit as st

# Load the pickled model
pipe = pickle.load(open('pipe.pkl', 'rb'))

def pred_fees(data):
    array = np.array(data).reshape(1, -1)
    prediction = pipe.predict(array)
    return prediction[0]

# data = [14,94,'Ayurveda',' Bangalore',1]
# output = pred_fees(data)
# print(output)

def main():
    st.title("Doctor's Consultation Fees Prediction")
    exp = st.number_input("Experience (in years)", min_value=0, max_value=66, value=0, step=1)
    rating = st.number_input("Rating (out of 100)", min_value=0, max_value=100, value=0, step=1)
    profile = st.selectbox("Profile", ['Ayurveda', 'Dentist', 'Dermatologists', 'ENT Specialist', 'General Medicine', 'Homeopath'])
    city = st.selectbox("City", [' Bangalore', ' Chennai', ' Delhi', ' Hyderabad', ' Mumbai', ' Others'])
    qual = st.number_input("No. of Qualifications", min_value=0, max_value=10, value=0, step=1)

    if st.button("Predict Fees"):
        data = [exp, rating, profile, city, qual]
        output = pred_fees(data)
        st.success("The predicted fees is Rs. {}".format(round(output)))

if __name__ == '__main__':
    main()