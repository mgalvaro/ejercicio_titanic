import streamlit as st
import pickle as pkl
import pandas as pd

# función para cargar el modelo y el encoding
def load_model(file_modelo, file_encoding):

    with open(file_modelo, 'rb') as model_file:
        modelo = pkl.load(model_file)

    with open(file_encoding, 'rb') as encoding_file:
        encoding = pkl.load(encoding_file)

    return modelo, encoding

def preprocesado(sex, age, pclass, fare, embarked):   # poner las columnas
     
    df = pd.DataFrame(columns=['Sex', 'Age', 'Pclass', 'Fare', 'Embarked_C', 'Embarked_Q', 'Embarked_S', 'Embarked_nan'])

    if sex == "male":
        df.iloc[0]['Sex'] = 1
    else:
        df.iloc[0]['Sex'] = 0

    df.iloc[0]['Age'] = age
    df.iloc[0]['Pclass'] = pclass
    df.iloc[0]['Fare'] = fare

    if embarked == "C":
        df.iloc[0]['Embarked_C'] = 1
        df.iloc[0]['Embarked_Q'] = 0
        df.iloc[0]['Embarked_S'] = 0
        df.iloc[0]['Embarked_nan'] = 0
    elif embarked == "Q":
        df.iloc[0]['Embarked_C'] = 0
        df.iloc[0]['Embarked_Q'] = 1
        df.iloc[0]['Embarked_S'] = 0
        df.iloc[0]['Embarked_nan'] = 0
    elif embarked == "S":
        df.iloc[0]['Embarked_C'] = 0
        df.iloc[0]['Embarked_Q'] = 0
        df.iloc[0]['Embarked_S'] = 1
        df.iloc[0]['Embarked_nan'] = 0
    else:
        df.iloc[0]['Embarked_C'] = 0
        df.iloc[0]['Embarked_Q'] = 0
        df.iloc[0]['Embarked_S'] = 0
        df.iloc[0]['Embarked_nan'] = 1

    return df
    

def main():
    
    st.markdown('Predicción Titanic')

    sex = st.radio(label = "Choose sex",
                   options = ('Male', 'Female'),
                   index = None,
                   disabled = False,
                   horizontal = True,
                   )
    
    age = st.slider(label = "Choose age",
                    min_value = 0.,
                    max_value = 100.,
                    value = 50.,
                    step = 1.)
    
    pclass = st.radio(label = "Choose class",
                   options = (1, 2, 3),
                   index = None,
                   disabled = False,
                   horizontal = True,
                   )
    
    fare = st.slider(label = "Choose fare",
                    min_value = 0.,
                    max_value = 10000.,
                    value = 50.,
                    step = 1.)
    
    embarked = st.radio(label = "Choose embarked",
                   options = ('C', 'Q', 'S'),
                   index = None,
                   disabled = False,
                   horizontal = True,
                   )
    
    df = preprocesado(sex, age, pclass, fare, embarked)

    st.dataframe(df)

if __name__ == "__main__":
    main()