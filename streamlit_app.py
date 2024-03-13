# Import python packages
import streamlit as st
from snowflake.snowpark.context import get_active_session

# Write directly to the app
st.title(":cup_with_straw:  Streamlit: JOB NAME App :balloon:")
st.write(
    """List Fruit"""
)
from snowflake.snowpark.functions import col

# Read DB
session = get_active_session()
# my_dataframe = session.table("DWH_DEV.TECH_TALEND.TECH_PARAM_JOB").select(col('JOB_NAME'))
my_dataframe = session.table("STREAMLIT_DB.STREAMLIT_SCHEMA.FRUIT_OPTIONS").select(col('FRUIT_NAME'))

st.dataframe(data=my_dataframe, use_container_width=True)

# Multi Selection 
Job_list= st.multiselect('Choose Job :' , my_dataframe)

# Visuel des Listes Choisies sous format tableau // Evite d 'aficher element si aucune selection
if Job_list:
    Job_string=''
  #   st.write(Job_list)
  #   st.text(Job_list)

# Boucle sur Selection des JobName et affichage de la chaine Job_string
    for Job_chosen in Job_list:
     #   Job_string+=Job_chosen
        Job_string+=Job_chosen + ' '

     #    st.write(Job_string)

    # Insert into TABLE(column)
    my_insert_stmt = """ insert into STREAMLIT_DB.STREAMLIT_SCHEMA.orders(ingredients)
            values ('""" + Job_string + """')"""
    # st.write(my_insert_stmt)

    # ADD a SubMit Button
    time_to_insert =st.button('Valider')

    if time_to_insert:
        session.sql(my_insert_stmt).collect()

        st.success('Your Smoothie is ordered!', icon="✅")
        
# Insert Select
#if Job_string:
#        session.sql(my_insert_stmt).collect()
#        st.success('Your Smoothie is ordered!', icon="✅")


    


    
# Store the initial value of widgets in session state

# if "visibility" not in st.session_state:
#     st.session_state.visibility = "visible"
#     st.session_state.disabled = False

# col1, col2 = st.columns(2)
# 
# with col1:
#      st.checkbox("Disable selectbox widget", key="disabled")
#     st.radio(
#         "Set selectbox label visibility 👉",
#         key="visibility",
#         options=["visible", "hidden", "collapsed"],
#     )

# with col2:
#     option = st.selectbox(
#         "How would you like to be contacted?",
#         ("Email", "Home phone", "Mobile phone"),
#         label_visibility=st.session_state.visibility,
#         disabled=st.session_state.disabled,
#     )
#  st.write ('Favorite is :', option)