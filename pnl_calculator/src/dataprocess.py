#step -1
import pandas as pd
import aspose.pdf as ap 
import os
import sys
#sys.path.append('E:\pnl_calculator')
#from src.logger import logging
DIR_OUTPUT='E:\pnl_calculator\pnl_calculator\output'
def dataingestion(file_path):
    input_pdf = file_path
    #logging.info("Data ingestion has been starte")
    output_pdf = "E:\pnl_calculator\pnl_calculator\output\convert_pdf_to_csv.csv"
    # Open PDF document
    document = ap.Document(input_pdf)

    save_option = ap.ExcelSaveOptions()
    save_option.format = ap.ExcelSaveOptions.ExcelFormat.CSV

    # Save the file
    document.save(output_pdf, save_option)

print("Enter the file path like E:\pnl_calculator\pnl_calculator\input\Investments-1.pdf")
PDF_File_Path=input()
dataingestion(PDF_File_Path)

