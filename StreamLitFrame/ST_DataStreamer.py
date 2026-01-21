import streamlit as st
import pandas as pd

st.set_page_config(page_title="CSV Explorer", layout="wide")

st.title("📊 CSV Data Explorer")
st.write("Upload a CSV file to explore your data instantly!")

# 1. File Uploader
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Read the file into a DataFrame
    df = pd.read_csv(uploaded_file)

    # 2. Basic Statistics Sidebar
    st.sidebar.header("Quick Stats")
    st.sidebar.write(f"**Total Rows:** {df.shape[0]}")
    st.sidebar.write(f"**Total Columns:** {df.shape[1]}")
    
    # 3. Data Filtering Section
    st.subheader("🔍 Filter Data")
    
    # Let user pick a column to filter by
    all_columns = df.columns.tolist()
    filter_column = st.selectbox("Select a column to filter by:", all_columns)
    
    # Get unique values from that column
    unique_values = df[filter_column].unique()
    selected_value = st.selectbox(f"Select a value from '{filter_column}':", unique_values)
    
    # Filter the dataframe
    filtered_df = df[df[filter_column] == selected_value]
    
    # 4. Display Data
    st.subheader("📄 Data View")
    
    # Use tabs to show filtered vs full data
    tab1, tab2, tab3 = st.tabs(["Filtered Data", "Full Dataset", "Data Summary"])
    
    with tab1:
        st.write(f"Showing results for: **{selected_value}**")
        st.dataframe(filtered_df, use_container_width=True)
        
    with tab2:
        st.dataframe(df, use_container_width=True)
        
    with tab3:
        st.write("Numerical Column Analysis:")
        st.write(df.describe())

else:
    st.info("💡 Please upload a CSV file to get started. Don't have one? Create a quick 'test.csv' with columns like 'Name, Score, Category'!")
    st.image("https://www.streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png", width=200)