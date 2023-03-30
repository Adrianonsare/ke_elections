import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

st.title("Streamlit Test")


uploaded_file = st.file_uploader("Upload File")

try:
    # @st.cache_data
    def uploadfile(x):
        if uploaded_file is not None:

            df=pd.read_excel(x)

            return df

    df=uploadfile(uploaded_file)
    st.write(df)

    # st.sidebar.title("Select County")
    # option_select=st.sidebar.radio("County Select Options",("All","Select"))

    # if option_select == "All":
    #     data_select=df
    #     st.dataframe(data_select)
    #     group=data_select.groupby('variable')['CountOFVotes'].sum().reset_index()
    #     fig=px.bar(group,x='variable',y='CountOfVotes')
    #     st.plotly_chart(fig,use_container_width=True)
    # else:
    #     variable=df['variable'].unique()
    #     var_select=st.sidebar.selectbox("Select County",variable)
    #     data_select=df[df['variable']==var_select]
    #     st.dataframe(data_select)
    #     fig=px.bar(data_select,x='County',y='CountOfVotes')
    #     st.plotly_chart(fig,use_container_width=True)
      
except:
    st.warning("You Have Not Uploaded A File")




