import streamlit as st
import pandas as pd
import plotly.express as px

# Define data URL
DATA_URL = 'https://raw.githubusercontent.com/randalnabout/streamlit/main/2019.csv'

# Load the data from the URL
data = pd.read_csv(DATA_URL)

def main():
    st.title("World Happiness Report")

    # Add your Streamlit content here
    fig5 = px.scatter_geo(data,
                         locations="Country or region",
                         locationmode="country names",
                         color="Score",
                         hover_name="Country or region",
                         size="GDP per capita",
                         projection="natural earth",
                         title="World Happiness Report")

    fig5.update_geos(showcoastlines=True, coastlinecolor="Black", showland=True, landcolor="white", showocean=True, oceancolor="lightblue")

    fig5.update_layout(geo=dict(showframe=False, showcoastlines=False))

    st.plotly_chart(fig5)

    st.title("Happiness Score vs. GDP per Capita (All Countries)")

    fig6 = px.scatter(data_frame=data, x="GDP per capita", y="Score", animation_frame="Overall rank",
                     size="Score", color="Country or region", hover_name="Country or region",
                     title="Happiness Score vs. GDP per Capita (All Countries)")

    fig6.update_layout(xaxis=dict(range=[1.2, 1.6]), yaxis=dict(range=[2, 8]))

    st.plotly_chart(fig6)

if __name__ == "__main__":
    main()
