# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 23:58:02 2021

@author: Zaid
"""

import fitz  # this is pymupdf
import spacy 
import pandas as pd
import streamlit as st


def main():
    st.title("Medical Terms Entity Extraction App")
    
    menu = ["DocumentFiles","About"]
    choice = st.sidebar.selectbox('Menu', menu)
    
    
    
    if choice=="DocumentFiles":
        st.subheader("Upload Document Files")
        docx_file = st.file_uploader("Upload Document",type=['pdf','txt'])
        
        menu1 = ['DRUG','DOSAGE','DURATION','ROUTE','STRENGTH','FORM','FREQUENCY']
        choice1 = st.selectbox("Select Entity", menu1)
        
        st.write("Note: If it shows empty then your document not contain that releted entity.")
                    
                    
        if st.button("Process"):
            if docx_file is not None:
                    with fitz.open(stream=docx_file.read(),filetype='pdf') as doc:
                        text = ""
                        for page in doc:
                            text += page.getText()
                            
                    nlp = spacy.load("en_core_med7_lg")
                    doc = nlp(text)
                    
                
                    
                    if choice1 == 'DOSAGE':
                        data = {'DOSAGE': [ent.text for ent in doc.ents if ent.label_== 'DOSAGE']}
                    elif choice1 == 'DRUG': 
                        data = {'Drugs Names': [ent.text for ent in doc.ents if ent.label_== 'DRUG']}
                    elif choice1 == 'DURATION':
                        data = {'DURATION Names': [ent.text for ent in doc.ents if ent.label_== 'DURATION']}
                    elif choice1 == 'ROUTE':
                        data = {'ROUTE': [ent.text for ent in doc.ents if ent.label_== 'ROUTE']}
                    elif choice1 == 'STRENGTH':
                        data = {'STRENGTH': [ent.text for ent in doc.ents if ent.label_== 'STRENGTH']}
                    elif choice1 == 'FORM':
                        data = {'FORM': [ent.text for ent in doc.ents if ent.label_== 'FORM']}
                    elif choice1 == 'FREQUENCY':
                        data = {'FREQUENCY': [ent.text for ent in doc.ents if ent.label_== 'FREQUENCY']}
                  
                    else:
                        st.write("Entity is not defined")
                    df = pd.DataFrame(data)
                    df = df.drop_duplicates()
                    st.write(df)
                    
                    #download csv
                    df = df.to_csv()
                    st.download_button("Download", data=df,file_name='drug.csv',mime='text/csv')
    
    else:
        st.subheader("About")
        st.write("Medical Terms Entity Extraction")
        st.write("The increasing number of biomedical articles and resources, searching for and extracting valuable information has become challenging.")
        st.write("Researchers consider multiple information sources and transform unstructured text data into refined knowledge to facilitate research productivity. However, manual annotation and feature generation by biomedical experts are inefficient because they involve a complex process and require expensive and time-consuming labour. Therefore, efficient and accurate natural language processing (NLP) techniques are becoming increasingly important for use in computational data analysis, and advanced text mining techniques are necessary to automatically analyse the biomedical literature and extract useful information from texts.")
        st.write("Our project is about Information Extraction (IE), which is one of the important tasks in text analysis and Natural Language Processing (NLP). It involves extracting meaningful pieces of knowledge related to clinical subjects like drug names, drug compositions, diseases, etc.  from Medical Journals as unstructured data and unstructured data is computationally opaque.")
        st.write("We are building this custom tool which helps to minimize time commitments from domain experts and the manual efforts on researching content.")
        st.write("Created by: Zaid Habib")


if __name__=='__main__':
    main()