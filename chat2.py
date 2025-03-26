import streamlit as st
import pickle

def get_storage_temp():
    return st.text_input("Storage Temperature")

def get_storage_humid():
    return st.text_input("Storage Humidity")

def get_material_type():
    return st.selectbox("Material Type", ["Glass", "HDPE", "PET", "PLA", "Paperboard"])

def get_product_state():
    return st.selectbox("Product State", ["Semisolid", "Solid"])

def get_storage_condition():
    return st.selectbox("Storage Condition", ["Chilled", "Refrigerated"])

def predict_species(te, hu, material, state, condition):
    loaded_model = pickle.load(open('proj.pkl','rb'))
    material_ohe = [1 if material == m else 0 for m in ["Glass", "HDPE", "PET", "PLA", "Paperboard"]]
    state_ohe = [1 if state == s else 0 for s in ["Semisolid", "Solid"]]
    condition_ohe = [1 if condition == c else 0 for c in ["Chilled", "Refrigerated"]]
    new_data = [[float(te), float(hu)] + material_ohe + state_ohe + condition_ohe]
    prediction = loaded_model.predict(new_data)
    st.write("Prediction with new data:", prediction)

if __name__ == "__main__":
    st.title('Shelf Life Prediction for Packaging using MLOps')
    st.image('shelfnew.png')
    storage_temp = get_storage_temp()
    storage_humid = get_storage_humid()
    material_type = get_material_type()
    product_state = get_product_state()
    storage_condition = get_storage_condition()
    
    if st.button("Predict"):
        predict_species(storage_temp, storage_humid, material_type, product_state, storage_condition)
