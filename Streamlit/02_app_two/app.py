import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
#add the title
st.title('data analysis application')
st.subheader("this is simple data analysis application")
#create a dropdown list to chose the dataset
dataset_options= ['iris','titanic','tips','diamonds']
selected_dataset = st.selectbox('select dataset',dataset_options)
#load the selected data set
if selected_dataset == 'iris':
    df = sns.load_dataset('iris')
elif selected_dataset == 'titanic':
    df = sns.load_dataset('titanic')
elif selected_dataset == 'tips':
    df = sns.load_dataset('tips')
elif selected_dataset == 'diamonds':
    df = sns.load_dataset('diamonds')
#Button to upload custom data set
uploaded_file = st.file_uploader("upload a custom dataset", type=["csv", "xlsx"])   
if uploaded_file is not None:
    #process the uploaded file
    df = pd.read_csv(uploaded_file) #assuming the uploaded file in csv format
st.write(df) #display the dataset
#Display the number of rows and columns from selected dataset
st.write('Number of rows:',df.shape[0])
st.write('Number of columns:',df.shape[1])
#display the column names of selected data with their data type
st.write('Column names and their data types:',df.dtypes)
#print the null values if those are > 0
if df.isnull().sum().sum() > 0:
    st.write('Null values:',df.isnull().sum().sort_values(ascending=False))
else:
    st.write('No null values')
#display the summary statistics of the selected dataset
st.write('Summary statistics:',df.describe())
#Create a pairplot
st.subheader('Pairplot')
#select the colimn to be used as hue in pairplot
hue_column = st.selectbox('select a column to be used as hue',df.columns)
st.pyplot(sns.pairplot(df,hue=hue_column))
#create a heatmap
st.subheader('Heatmap')
#select the columns which are numeric and then create a corr_matrix
numeric_columns = df.select_dtypes(include=[np.number]).columns
corr_matrix = df[numeric_columns].corr()
numeric_columns = df.select_dtypes(include=[np.number]).columns
corr_matrix = df[numeric_columns].corr()
from plotly import graph_objects as go
#convert the seaborn heatmap to plotly heatmap
heatmap_fig = go.Figure(data=go.Heatmap(z=corr_matrix.values, x=corr_matrix.columns, y=corr_matrix.columns,colorscale='Viridis'))
st.plotly_chart(heatmap_fig)