import streamlit as st
import pandas as pd
import plotly.express as px

#reading the csv file and adding in a manufacturer's column
df = pd.read_csv('vehicles_us.csv')
df['manufacturer'] = df['model'].apply(lambda x: x.split()[0])

#Making a luxury and non-luxury df for later use
luxury = ['acura', 'bmw', 'buick', 'cadillac', 'chrysler', 'mercedes-benz', ]
df_lux = df[df['manufacturer'].isin(luxury)]

non_luxury = ['chevrolet', 'dodge', 'ford', 'gmc', 'honda', 'hyundai', 'jeep', 'kia', 'nissan', 'ram', 'subaru', 'toyota', 'volkswagen']
df_non_lux = df[df['manufacturer'].isin(non_luxury)]

#First  show the different manufacturers and types of vehicles that are in the dataset. 
st.header('Vehicle types by manufacturer')
fig = px.histogram(df, x='manufacturer', color='type')
st.write(fig)

#This chart will allow the user to compare the price and milage on the car. 
st.header('A comparison of price vs milage and condition of the vehicle')
fig6 = px.scatter(df_lux, x='odometer', y='price', color='condition', title='Price vs. Odometer by Vehicle Condtion')
fig7 = px.scatter(df_non_lux, x='odometer', y='price', color='condition', title='Price vs. Odometer by Vehicle Condtion')
#adding a checkbox option that will make change the displayed chart based on whether or not the vehicles are in the luxury or non-luxury dfs
check_lux = st.checkbox('View Luxury Cars Only', value=True)
if check_lux:
    st.write('Only luxury cars displayed')
    st.write(fig6)
else:
    st.write('Non-luxury cars displayed')
    st.write(fig7)

#one more scatter plot to show a comparison of price vs year
st.header('A comparison of price vs year of the vehicle')
fig4 = px.scatter(df, x='model_year', y='price', color='type')
st.write(fig4)