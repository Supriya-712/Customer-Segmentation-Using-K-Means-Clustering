import streamlit as st
import pandas as pd
import numpy as np
import pickle

pickle_in = open ("reg.pkl", "rb")
reg = pickle.load (pickle_in)

def predict_cluster (ai, ss):
    prediction = reg.predict ([[ai, ss]])
    return (prediction)

def main ():
    st.title (" \n Customer Segmentation Based On Their Annual Income And Spending Score \n ")

    st.subheader (" \n Annual Income (k$) \n ")
    ai = st.number_input (" \n Enter the Annual Income (k$) : \n ")
    st.write (" \n Annual Income (k$) : ", ai)

    st.subheader (" \n Spending Score (1-100) \n ")
    ss = st.slider (" \n Enter the Spending Score (1-100) : \n ")
    st.write (" \n Spending Score : ", ss)
    res = ""
    if st.button ("Predict Cluster"):
        res = predict_cluster (ai, ss)
    st.success ("Predicted Cluster is : {} ".format(res))

    

if __name__ == "__main__":
    main ()
