import streamlit as st
import numpy as np
import sklearn 
import pandas as pd
import joblib

# Load the model from the pickle file
model = joblib.load('Football_Manager_rf1.joblib')

st.set_page_config(
     page_title='Football Manager 2024 Progression Predictor',
     layout="wide",
)
st.title('Will my defensive player progress?')

col1, col2, col3, col4 = st.columns(4) #devide the page in four columns

with col1: # allows to display content in the first column
    st.header('Technique', divider='red')
    Cen = st.number_input('Centres', value=10, min_value=0,max_value=20, step=1) # asks the user to enter a player stat
    Ctr = st.number_input('Contrôle', value=10, min_value=0,max_value=20, step=1)
    Cor = st.number_input('Corners', value=10,  min_value=0,max_value=20, step=1)
    CF = st.number_input('Coups francs', value=10,  min_value=0,max_value=20, step=1)
    Drb = st.number_input('Dribbles', value=10,  min_value=0,max_value=20, step=1)
    Fin = st.number_input('Finition', value=10, min_value=0,max_value=20, step=1)
    Head = st.number_input('Jeu de tête', value=10, min_value=0,max_value=20, step=1)
    Mar = st.number_input('Marquage', value=10, min_value=0,max_value=20, step=1)
    Pas = st.number_input('Passes', value=10, min_value=0,max_value=20, step=1)
    Pen = st.number_input('Penalty', value=10, min_value=0,max_value=20, step=1)
    Tcl = st.number_input('Tacles', value=10, min_value=0,max_value=20, step=1)
    Tec = st.number_input('Technique', value=10, min_value=0,max_value=20, step=1)
    Tir = st.number_input('Tirs de loin', value=10, min_value=0,max_value=20, step=1)
    T_lg = st.number_input('Touches longues', value=10, min_value=0,max_value=20, step=1)

with col2:# allows to display content in the second column
    st.header('Mental', divider='red')
    Agr = st.number_input('Agressivité', value=10, min_value=0,max_value=20, step=1)
    Ant = st.number_input('Anticipation', value=10, min_value=0,max_value=20, step=1)
    Apl = st.number_input('Appels de balle', value=10, min_value=0,max_value=20, step=1)
    Ctn = st.number_input('Concentration', value=10, min_value=0,max_value=20, step=1)
    Crg = st.number_input('Courage', value=10, min_value=0,max_value=20, step=1)
    Dec = st.number_input('Décisions', value=10, min_value=0,max_value=20, step=1)
    Det = st.number_input('Détermination', value=10, min_value=0,max_value=20, step=1)
    Ins = st.number_input('Inspiration', value=10, min_value=0,max_value=20, step=1)
    Col = st.number_input('Jeu collectif', value=10, min_value=0,max_value=20, step=1)
    Ldr = st.number_input('Leadership', value=10, min_value=0,max_value=20, step=1)
    Pla = st.number_input('Placement', value=10, min_value=0,max_value=20, step=1)
    Sgf = st.number_input('Sang-froid', value=10, min_value=0,max_value=20, step=1)
    Vis = st.number_input('Vision du jeu', value=10, min_value=0,max_value=20, step=1)
    Vol = st.number_input('Volume de jeu', value=10, min_value=0,max_value=20, step=1)

with col3: # allows to display content in the third column
    st.header('Physique', divider='red')
    Acc = st.number_input('Accélération', value=10, min_value=0,max_value=20, step=1)
    Agi = st.number_input('Agilité', value=10, min_value=0,max_value=20, step=1)
    Jump = st.number_input('Détente verticale', value=10, min_value=0,max_value=20, step=1)
    End = st.number_input('Endurance', value=10, min_value=0,max_value=20, step=1)
    Equ = st.number_input('Équilibre', value=10, min_value=0,max_value=20, step=1)
    Pui = st.number_input('Puissance', value=10, min_value=0,max_value=20, step=1)
    Phy = st.number_input('Qualités phys. nat.', value=10, min_value=0,max_value=20, step=1)
    Vit = st.number_input('Vitesse', value=10, min_value=0,max_value=20, step=1)

with col4: # allows to display content in the 4th column
    st.header('Age', divider='red')
    Age = st.number_input('Age', value=15, min_value=15,max_value=45, step=1)

input_dict = {
    'Age': Age,
    'Cor': Cor,
    'Cen': Cen,
    'Drb': Drb,
    'Apl': Apl,
    'Agr': Agr,
    'Fin': Fin,
    'Ctn': Ctn,
    'Ctr': Ctr,
    'Det': Det,
    'Ins': Ins,
    'Col': Col,
    'Dec': Dec,
    'Equ': Equ,
    'CF': CF,
    'Acc': Acc,
    'Pui': Pui,
    'Pla': Pla,
    'Phy': Phy,
    'Vol': Vol,
    'Vit': Vit,
    'Agi': Agi,
    'Jump': Jump,
    'Sgf': Sgf,
    'End': End,
    'Crg': Crg,
    'Ldr': Ldr,
    'Vis': Vis,
    'Ant': Ant,
    'Head': Head,
    'Tir': Tir,
    'T_Lg': T_lg,
    'Mar': Mar,
    'Pas': Pas,
    'Pen': Pen,
    'Tcl': Tcl,
    'Tec': Tec
}
with col4:# allows to display content in the 4th column
    if st.button('Predict'): #Runs the data through the model to make a prediction when the user clicks on the button 
        inputs = pd.DataFrame(input_dict, index=[0])
        def_stats = ['Head', 'Mar', 'Tcl', 'Agr', 'Ant', 'Ctn', 'Crg', 'Dec', 'Pla', 'Sgf', 'Jump', 'Pui', 'Vit']
        inputs['best_def'] = inputs[def_stats].mean(axis=1)
        prediction = model.predict(inputs)
        if prediction==0:
            st.write('The player should progress')
        elif prediction==1:
            st.write('The player should regress')
        elif prediction==2:
            st.write('The player should remain at the same level')