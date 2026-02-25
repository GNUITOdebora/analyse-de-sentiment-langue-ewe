import re
import pickle
import nltk
import streamlit as st
st.title("sentiment Analyse de commentaire EWE")
vect=pickle.load(open("vectorizer.pickle","rb"))
model=pickle.load(open("best_modelNLP.pickle","rb"))
text=st.text_input("Leave your comment (Ŋlɔ Wò Nyawo Ði)")

tmp = re.sub(r'\d+', ' ', str(text) )# Supprime les nombres
tmp=re.sub(r'\s+',' ',tmp)# Supprime les espaces multiples
tmp=tmp.lower() #Convertit en minuscules
tmp = re.sub(r'[^\w\s]', '', tmp) # Élimine la ponctuation

X=vect.transform([tmp]).toarray()
pred=model.predict(X)
if st.button("predict"):
  st.success(pred)