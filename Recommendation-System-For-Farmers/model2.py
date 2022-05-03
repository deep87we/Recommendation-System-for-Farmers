import streamlit as st
import pickle 
import numpy as np

def load_model(modelfile):
	loaded_model = pickle.load(open(modelfile, 'rb'))
	return loaded_model
def show_model2():
     # title
    html_temp = """
    <div>
    <h1 style="color:MEDIUMSEAGREEN;text-align:left;"> Fertilzer Recommendation  🌱 </h1>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    col1,col2  = st.columns([2,2])
    
    with col1: 
        with st.expander(" ℹ️ Information", expanded=True):
            st.write("""
            Fertilizer recommendation is one of the most important aspects of precision agriculture. Fertilzers recommendation are based on a number of factors. Precision agriculture seeks to define these criteria on a site-by-site basis in order to address crop selection issues. While the "site-specific" methodology has improved performance, there is still a need to monitor the systems' outcomes.Precision agriculture systems aren't all created equal. 
            However, in agriculture, it is critical that the recommendations made are correct and precise, as errors can result in significant material and capital loss.
            """)
        '''
        ## How does it work ❓ 
        Complete all the parameters and the machine learning model will predict the most suitable Fertilser to add in a particular farm based on various parameters
        '''


    with col2:
        st.subheader(" Find out the most suitable Fertilzer to add in your farm to increase the Productivity👨‍🌾")
        temp = st.number_input("Temperature",0.0,100000.0)
        humidity = st.number_input("Humidity in %", 0.0,100000.0)
        moisture = st.number_input("Moisture",0.0,100000.0)
        Soils=["Black","Clayey","Loamy","Red","Sandy"]
        Soil=st.selectbox("Soil_Type",Soils)
        if Soil=="Black":
            soil=0
        elif Soil=="Clayey":
            soil=1
        elif Soil=="Loamy":
            soil=2
        elif Soil=="Red":
            soil=3
        elif Soil=="Sandy":
            soil=4
        Crops=["Barley"	,"Cotton"	,"Ground Nuts"	,"Maize","Millets","Oil seeds","Paddy","Pulses","Sugarcane"	,"Tobacco","Wheat"]
        Crop=st.selectbox("Crop_Type",Crops)
        if Crop=="Barley":
            crop=0
        elif Crop=="Cotton":
            crop=1
        elif Crop=="Ground Nuts":
            crop=2
        elif Crop=="Maize":
            crop=3
        elif Crop=="Millets":
            crop=4
        elif Crop=="Oil seeds":
            crop=5
        elif Crop=="Paddy":
            crop=6
        elif Crop=="Pulses":
            crop=7
        elif Crop=="Sugarcane":
            crop=8
        elif Crop=="Tobacco":
            crop=9
        elif Crop=="Wheat":
            crop=10

        N = st.number_input("Nitrogen", 1,10000)
        K = st.number_input("Potassium", 1,10000)
        P = st.number_input("Phosporus", 1,10000)
         
        

        feature_list = [temp,humidity,moisture,soil,crop,N,P, K]
        single_pred = np.array(feature_list).reshape(1,-1)
        
        if st.button('Predict'):

            loaded_model = load_model('model-3.pkl')
            prediction = loaded_model.predict(single_pred)
            col1.write('''
		    ## Results 🔍 
		    ''')
            if prediction.item()==6:
                ans="Urea"
            elif prediction.item()==5:
                ans="DAP"
            elif prediction.item()==4:
                ans="28-28"
            elif prediction.item()==3:
                ans="20-20"
            elif prediction.item()==2:
                ans="17-17-17"
            elif prediction.item()==1:
                ans="14-35-14"
            elif prediction.item()==0:
                ans="10-26-26"
            col1.success(f"{ans} Fertilizer is recommended by the A.I for your farm.")
      #code for html ☘️ 🌾 🌳 👨‍🌾  🍃

    st.warning("Note: This ML application is for educational/demo purposes only and cannot be relied upon. Check the source code [here](https://github.com/deep87we/Recommendation-System-for-Farmers)")
    hide_menu_style = """
    <style>
    #MainMenu {visibility: hidden;}
    </style>
    """

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)
