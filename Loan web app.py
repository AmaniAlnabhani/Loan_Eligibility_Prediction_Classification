# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 14:21:18 2024

@author: Amani
"""


import numpy as np
import pickle
import streamlit as st
#loding the sved model
#rb mean read binary
loaded_model=pickle.load(open('C:/Users/Amani/OneDrive/Documents/machine Learning/Loan/trained_model.sav','rb'))

def loan_prediction(input_data):

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)


    prediction = loaded_model.predict(input_data_reshaped)
    print( prediction)

    if (prediction[0] == 0):
      return 'Sorry your Loan Rejected😔 '
    else:
      return 'congratulations your Loan Accepted🎉'

    
def main():
    
    #given title
    st.title('Loan prediction web app')
    #gitting input data from user
    
    Gender=st.text_input('gender')
    Married=st.text_input('married')
    Dependents=st.text_input('Dependents')
    Education=st.text_input('Education')
    Self_Employed=st.text_input('self employed')
    ApplicantIncome=st.text_input('Enter your Income')
    CoapplicantIncome=st.text_input('Enter your CoapplicantIncome')
    LoanAmount=st.text_input('Enter your Loan Amount')
    Loan_Amount_Term=st.text_input('Enter your Loan_Amount_Term')
    Credit_History=st.text_input('Credit history')
    Property_Area=st.text_input('property')


    
    #cod for prediction
    loan=''
    # create a button for prediction
    if st.button('Loan State Result'):
        loan=loan_prediction([Gender,Married,Dependents,Education,
                                   Self_Employed,ApplicantIncome,CoapplicantIncome,LoanAmount,
                                   Loan_Amount_Term,Credit_History,Property_Area])
    st.success(loan)
    
    
if __name__ == '__main__' :
     main()