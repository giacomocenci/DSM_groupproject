import streamlit as st
import pandas as pd
import pickle
 
 
st.write("""
# Prediction Monitor
Hello *world!*
""")

def score_model(supplier, quantity) -> float:
    # Load Model 
    model = pickle.load(open('./gbm_500.pkl', 'rb'))
    
    # Define the possible suppliers
    suppliers = ['Aromatico', 'Beans Inc.', 'Fair Trade AG', 'Farmers of Brazil', 'Handelskontor Hamburg']
    
    # Create a dictionary for the DataFrame
    data = {
        "quantity_ordered": [quantity],
    }
    
    # Add supplier one-hot encoding to the dictionary
    for s in suppliers:
        data[f'd_{s}'] = [1 if s == supplier else 0]
    
    # Create the DataFrame
    test_data = pd.DataFrame(data)
    
    prediction = model.predict(test_data)[0]    
    
    return prediction
        
                    
                    
    

# All suppliers
suppliers = ['Aromatico', 'Beans Inc.', 'Fair Trade AG', 'Farmers of Brazil', 'Handelskontor Hamburg']

# Create input fields
# Create input fields
supplier = st.selectbox("Select supplier name", suppliers)
quantity = st.number_input("Enter quantity", min_value=0)


# Add a button to call the function
if st.button("Calculate Score"):
    if supplier and quantity:
        score = score_model(supplier, quantity)
        st.write(f"Predicted days late: {score}")
    else:
        st.write("Please enter both supplier name and quantity.")


