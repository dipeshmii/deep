import streamlit as st
import pickle

def get_storage_temp():
    return st.text_input("Storage Temperature")

def get_storage_humid():
    return st.text_input("Storage Humidity")

def get_material_type_Glass():
    return 1 if st.radio("Material Type", ["Glass", "Other"], index=1) == "Glass" else 0

def get_material_type_HDPE():
    return 1 if st.radio("Material Type", ["HDPE", "Other"], index=1) == "HDPE" else 0

def get_material_type_PET():
    return 1 if st.radio("Material Type", ["PET", "Other"], index=1) == "PET" else 0

def get_material_type_PLA():
    return 1 if st.radio("Material Type", ["PLA", "Other"], index=1) == "PLA" else 0

def get_material_type_Paperboard():
    return 1 if st.radio("Material Type", ["Paperboard", "Other"], index=1) == "Paperboard" else 0

def get_product_state_Semisolid():
    return 1 if st.radio("Product State", ["Semisolid", "Other"], index=1) == "Semisolid" else 0

def get_product_state_Solid():
    return 1 if st.radio("Product State", ["Solid", "Other"], index=1) == "Solid" else 0

def get_storage_cond_Chilled():
    return 1 if st.radio("Storage Condition", ["Chilled", "Other"], index=1) == "Chilled" else 0

def get_storage_cond_Refrigerated():
    return 1 if st.radio("Storage Condition", ["Refrigerated", "Other"], index=1) == "Refrigerated" else 0

def predict_species(te, hu, gl, hd, pe, pl, pp, ss, so, ch, re):
    loaded_model = pickle.load(open('proj.pkl', 'rb'))
    new_data = [[float(te), float(hu), float(gl), float(hd), float(pe), float(pl), float(pp), float(ss), float(so), float(ch), float(re)]]
    prediction = loaded_model.predict(new_data)
    st.write("Prediction with new data:")
    st.write(prediction)

if __name__ == "__main__":
    st.title('Penguin Species Prediction with Decision Tree Model 2025')
    st.image('penguin.png')
    
    storage_temp = get_storage_temp()
    storage_humid = get_storage_humid()
    material_type_Glass = get_material_type_Glass()
    material_type_HDPE = get_material_type_HDPE()
    material_type_PET = get_material_type_PET()
    material_type_PLA = get_material_type_PLA()
    material_type_Paperboard = get_material_type_Paperboard()
    product_state_Semisolid = get_product_state_Semisolid()
    product_state_Solid = get_product_state_Solid()
    storage_cond_Chilled = get_storage_cond_Chilled()
    storage_cond_Refrigerated = get_storage_cond_Refrigerated()

    if st.button("Predict"):
        predict_species(storage_temp, storage_humid, material_type_Glass, material_type_HDPE, material_type_PET, material_type_PLA, material_type_Paperboard, product_state_Semisolid, product_state_Solid, storage_cond_Chilled, storage_cond_Refrigerated)
