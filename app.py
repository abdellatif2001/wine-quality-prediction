import pandas as pd
import streamlit as st
import pickle 

st.title('More wine More happiness')
st.write('## quality of your wine')
st.write('### enter the infos')

type_wine = ['Red','White']
color = st.radio('color of the wine',type_wine)

fx = st.text_input('Fixed acidity')
va = st.text_input('Volatile acidity')
ca = st.text_input('Citric acid')
rs = st.text_input('Residual sugar')
ch = st.text_input('Chlorides')
fsd = st.text_input('Free sulfur dioxide')
tsd = st.text_input('Total sulfur dioxide')
de = st.text_input('Density')
ph = st.text_input('PH')
su = st.text_input('Sulphates')
al = st.text_input('Alcohol')

ok = st.button("rating")

if color == 'Red':
    model = pickle.load(open('winequality_red_model.sav', 'rb'))
elif color == 'White':
    model = pickle.load(open('winequality_white_model.sav', 'rb'))


if ok:
    x = [fx,va,ca,rs,ch,fsd,tsd,de,ph,su,al]
    r = model.predict([x])
    st.write('rating is',r[0])
