import streamlit as st
import pandas as pd
import os 
from io import BytesIO

st.set_page_config(page_title="Data Sweeper", layout="wide", page_icon="📝")
st.title("Data Sweeper")
st.write("Transform your file between CSV and Excel formats with built-in data cleaning tools and visualization")

uploaded_file = st.file_uploader("Upload a file", type=["csv", "xlsx"], accept_multiple_files=True)

if uploaded_file:
    for file in uploaded_file:
        file_ext = os.path.splitext(file.name)[-1].lower()
        
        if file_ext==".csv":
            df = pd.read_csv(file)
        elif file_ext==".xlsx":
            df = pd.read_excel(file)
        else: st.error("Unsupported file format:{file_ext}")
        continue
    #Display info about file
    st.write(f"File Name:{file.name}")
    st.write(f"File Size:{file.size/1024}")
    
    #Show 5 rows of dataframe
    st.write("Preview the head of the dataframe")
    st.dataframe(df.head())
    
    #Data Cleaning
    st.subheader("Data Cleaning Options")
    if st.checkbox(f"Clean data for {file.name}"):
        col1, col2 = st.columns(2)
        with col1:
            if st.button(f"Remove Duplicates from {file.name}"):
                df.drop_duplicates(inplace=True)
                st.write("Duplicates removed")
                
        with col2:
            if st.button(f"Fill missing values in {file.name}"):
                numeric_cols = df.select_dtypes(include=["number"]).columns
                df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
                st.write("Missing values filled")
                
        #Choose specific colums to keep or convert
        st.subheader("Choose columms to keep or convert")
        columns =st.multiselect(f"Choose columns for {file.name}", df.columns, default=df.columns)
        df = df[columns]
        
        #Data Visualization
        st.subheader("📊Data Visualization")
        if st.checkbox(f"Show Visualization for {file.name}"):
            st.write("Choose a plot type")
            plot_type = st.selectbox("Plot Type", ["Line", "Bar", "Histogram", "Boxplot"])
            if plot_type=="Line":
                axis = st.selectbox("X-axis", df.columns, index=0)
                columns = st.multiselect("Y-axis", df.columns.drop(axis))  # This avoids selecting axis column again
                if columns:  # Only plot if user selected Y-axis columns
                    st.line_chart(df.set_index(axis)[columns])
                else:
                    st.warning("Please select at least one column for Y-axis.")
            elif plot_type=="Bar":
                st.bar_chart(df.select_dtypes(include="number"))
            # elif plot_type=="Histogram":    
            #     st.write(df.select_dtypes(include="number"))
            # elif plot_type=="Boxplot":
            #     st.write(df.select_dtypes(include="number"))
                
        #Convert the file to CSV or Excel
        st.subheader(f"Conversion Options")
        conversion_type = st.radio(f"Convert {file.name} to:", ["CSV", "Excel"], key=file.name)
        if st.button(f"Convert {file.name}"):
            buffer = BytesIO()
            if conversion_type=="CSV":
                df.to_csv(buffer, index=False)
                file_name = file.name.replace(file_ext, ".csv")
                mime_type = "text/cv"    
            
            elif conversion_type=="Excel":
                df.to_excel(buffer, index=False)
                file_name = file.name.replace(file_ext, ".xlsx")
                mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            buffer.seek(0)
            
            #Download the file
            st.download_button(
                label=f"⬇Download {file.name} as {conversion_type}",
                data=buffer,
                file_name=file_name,
                mime=mime_type
            )
st.success("🏆 All files processed!")
            
            
                
                
                
                
        
