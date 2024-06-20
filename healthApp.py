import streamlit as st
import pandas as pd
import datetime
from PIL import Image
import plotly.express as px
import plotly.graph_objects as go
print("HealthCare Dashboard")
# reading the data from excel file
df = pd.read_csv("healthcare_dataset.csv")


st.set_page_config(layout="wide")
st.markdown('<style>div.block-container{padding-top:1rem;}</style>', unsafe_allow_html=True)

col1, col2 = st.columns([0.1,0.9])
html_title = """
    <style>
    .title-test {
    font-weight:bold;
    padding:5px;
    border-radius:6px;
    }
    </style>
    <br>
    <center><h1 class="title-test">Healthcare Dataset - Dashboard</h1></center>
    <center><h5 class="title-test"><a href='https://www.kaggle.com/datasets/prasad22/healthcare-dataset?resource=download'>Dataset Link</h5></a></center>
    """


df['Date of Admission'] = pd.to_datetime(df['Date of Admission'])
df['Discharge Date'] = pd.to_datetime(df['Discharge Date'])


with col2:
    st.markdown(html_title, unsafe_allow_html=True)

col3, col4, col5 = st.columns([0.1,0.45,0.45])

with col3:
    box_date = str(datetime.datetime.now().strftime("%d %B %Y"))
    st.write(f"Dilanga Abeyrathna:  \n {box_date}")

# with col4:
    # fig = px.bar(df, x = "Retailer", y = "TotalSales", labels={"TotalSales" : "Total Sales {$}"},
    #              title = "Total Sales by Retailer", hover_data=["TotalSales"],
    #              template="gridon",height=500)
    # st.plotly_chart(fig,use_container_width=True)

_, dwn1, view2 = st.columns([0.15,0.40,0.40])

with dwn1:
    age_by_condition = df.groupby('Medical Condition')['Age'].mean().reset_index()

    # Plot using Plotly Express with different color palettes
    fig = px.bar(age_by_condition, x='Medical Condition', y='Age', color='Medical Condition',
                title='Average Age by Medical Condition',
                labels={'Age': 'Average Age', 'Medical Condition': 'Medical Condition'},
                color_discrete_sequence=px.colors.qualitative.Pastel)
    st.plotly_chart(fig,use_container_width=True)

with view2:
    sex_by_condition = df.groupby(['Medical Condition', 'Gender']).size().reset_index(name='Count')

    # Plot using Plotly Express with different color palettes
    fig = px.bar(sex_by_condition, x='Medical Condition', y='Count', color='Gender',
                title='Patient Count by Gender and Medical Condition',
                labels={'Count': 'Patient Count', 'Medical Condition': 'Medical Condition', 'Gender': 'Gender'},
                color_discrete_sequence=px.colors.qualitative.Pastel)
    st.plotly_chart(fig,use_container_width=True)


_, bar1, bar2 = st.columns([0.15,0.45,0.40])
with bar1:
    grouped_df = df.groupby(['Blood Type', 'Medical Condition']).size().reset_index(name='Count')

    # Plot using Plotly Express
    fig = px.bar(grouped_df, x='Blood Type', y='Count', color='Medical Condition', barmode='group',
                title='Patient Count by Blood Type and Medical Condition',
                labels={'Count': 'Patient Count', 'Blood Type': 'Blood Type', 'Medical Condition': 'Medical Condition'})
    st.plotly_chart(fig,use_container_width=True)

with bar2:
    grouped_df = df.groupby(['Blood Type', 'Gender']).size().reset_index(name='Count')

    # Plot using Plotly Express
    fig = px.bar(grouped_df, x='Blood Type', y='Count', color='Gender', barmode='group',
                title='Patient Count by Blood Type and Gender',
                labels={'Count': 'Patient Count', 'Blood Type': 'Blood Type', 'Gender': 'Gender'})
    st.plotly_chart(fig,use_container_width=True)


_, view1, view2 = st.columns([0.15,0.40,0.40])

with view2:
    expander = st.expander("Data Description 1")
    data1 = df.describe()    
    expander.write(data1)
    

with view1:
    expander = st.expander("Data Description 2")
    data2 = df.describe(include= "object").T
    expander.write(data2)

_,view3, view4 = st.columns([0.15,0.40,0.40])
with view3:
    monthly_admissions = df['Date of Admission'].dt.month.value_counts().sort_index()

    # Create a DataFrame
    monthly_admissions_df = pd.DataFrame({'Month': monthly_admissions.index, 'Admissions': monthly_admissions.values})

    fig = px.line(monthly_admissions_df, x='Month', y='Admissions', title='Monthly Admissions Trend')
    fig.update_xaxes(title='Month')
    fig.update_yaxes(title='Number of Admissions')
    st.plotly_chart(fig,use_container_width=True)

with view4:
    grouped_df = df.groupby(['Blood Type', 'Gender']).size().reset_index(name='Count')

    # Plot using Plotly Express
    fig = px.bar(grouped_df, x='Blood Type', y='Count', color='Gender', barmode='group',
                title='Patient Count by Blood Type and Gender',
                labels={'Count': 'Patient Count', 'Blood Type': 'Blood Type', 'Gender': 'Gender'})
    st.plotly_chart(fig,use_container_width=True)



_,view5 = st.columns([0.15,0.80])

with view5:
    dsch = df.groupby(['Hospital'])['Name'].count().reset_index()
    dsch.columns = ['hospital', 'count']
    fig = px.bar(
        dsch, 
        x='hospital', 
        y="count", 
        barmode='group',
        orientation='v', 
        title='Cases per hospital distribution'
    )
    st.plotly_chart(fig,use_container_width=True)

    st.write(df.head())