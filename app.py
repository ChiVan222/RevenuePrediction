import streamlit as st
import sklearn
import pickle
model = pickle.load(open("model.pickle","rb"))
st.balloons()
st.snow()
st.title('Revenue Prediction')
x = st.number_input('Input Temperature' )
if st.button("Predict"):
   y = model.predict(x.reshape(-1,1))
   st.success(y)
