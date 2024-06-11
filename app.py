import streamlit as st
import pandas as pd
import openpyxl

def main():
    st.title("Excel File Uploader")

    uploaded_file = st.file_uploader("Choose an Excel file", type="xlsx")
    
    if uploaded_file is not None:
        try:
            # Read the file into a DataFrame
            df = pd.read_excel(uploaded_file)
            
            st.write("File successfully uploaded!")
            st.write("Here is a preview of the file content:")
            
            # Display the DataFrame
            st.dataframe(df)
        except Exception as e:
            st.error(f"Error loading file: {e}")

if __name__ == "__main__":
    main()
