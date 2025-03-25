import streamlit as st
import pickle



def get_storage_temp():
    storage_temp = st.text_input("Storage Temperature")
    return storage_temp

def get_storage_humid():
    storage_humid = st.text_input("Storage Humidity")
    return storage_humid

def get_material_type_Glass():
    material_type_Glass = st.text_input("material_type_Glass")
    return material_type_Glass

def get_material_type_HDPE():
    material_type_HDPE = st.text_input("material_type_HDPE")
    return material_type_HDPE

def get_material_type_PET():
    material_type_PET = st.text_input("material_type_PET")
    return material_type_PET

def get_material_type_PLA():
    material_type_PLA	 = st.text_input("material_type_PLA")
    return material_type_PLA

def get_material_type_Paperboard():
    material_type_Paperboard = st.text_input("material_type_Paperboard")
    return material_type_Paperboard

def get_product_state_Semisolid():
    product_state_Semisolid = st.text_input("product_state_Semisolid")
    return product_state_Semisolid

def get_product_state_Solid():
    product_state_Solid = st.text_input("product_state_Solid")
    return product_state_Solid

def get_storage_cond_Chilled():
    storage_cond_Chilled = st.text_input("storage_cond_Chilled")
    return storage_cond_Chilled

def get_storage_cond_Refrigerated():
    storage_cond_Refrigerated = st.text_input("storage_cond_Refrigerated")
    return storage_cond_Refrigerated

def predict_species(te,hu,gl,hd,pe,pl,pp,ss,so,ch,re):
    loaded_model = pickle.load(open('proj.pkl','rb'))
    new_data = [[float(te),float(hu),float(gl),float(hd),float(pe),float(pl),float(pp),float(ss),float(so),float(ch),float(re)]]
    prediction = loaded_model.predict(new_data)
    st.write("Prediction with new data: ")
    st.write(prediction)
    



if __name__ == "__main__":
    st.title('Penguin Species prediction with Decision Tree model 2025')
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
    predict_species(storage_temp,storage_humid,material_type_Glass,material_type_HDPE,material_type_PET,material_type_PLA,material_type_Paperboard,product_state_Semisolid,product_state_Solid,storage_cond_Chilled,storage_cond_Refrigerated)
    
