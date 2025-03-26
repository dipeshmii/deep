import streamlit as st
import pickle
import numpy as np

def get_storage_temp():
    return st.text_input("Storage Temperature")

def get_storage_humid():
    return st.text_input("Storage Humidity")

def get_material_type():
    return st.radio("Material Type", ["Glass", "HDPE", "PET", "PLA", "Paperboard", "Aluminium"])

def get_product_state():
    return st.radio("Product State", ["Solid", "Semisolid", "Liquid"])

def get_storage_condition():
    return st.radio("Storage Condition", ["Chilled", "Refrigerated", "Ambient"])

def predict_shelf_life(temp, humid, material, state, condition):
    loaded_model = pickle.load(open('proj.pkl', 'rb'))
    
    # One-hot encoding for categorical inputs
    material_types = ["Glass", "HDPE", "PET", "PLA", "Paperboard", "Aluminium"]
    product_states = ["Solid", "Semisolid", "Liquid"]
    storage_conditions = ["Chilled", "Refrigerated", "Ambient"]
    
    material_ohe = [1 if material == m else 0 for m in material_types]
    state_ohe = [1 if state == s else 0 for s in product_states]
    condition_ohe = [1 if condition == c else 0 for c in storage_conditions]
    
    # Prepare input for prediction
    new_data = [[float(temp), float(humid)] + material_ohe + state_ohe + condition_ohe]
    prediction = loaded_model.predict(new_data)
    st.write("Predicted Shelf Life:", prediction[0])

if __name__ == "__main__":
    st.title('Shelf Life Prediction using Decision Tree')
    st.image('penguin.png')  # Update this image if needed
    
    storage_temp = get_storage_temp()
    storage_humid = get_storage_humid()
    material_type = get_material_type()
    product_state = get_product_state()
    storage_condition = get_storage_condition()
    
    if st.button("Predict"):
        predict_shelf_life(storage_temp, storage_humid, material_type, product_state, storage_condition)
