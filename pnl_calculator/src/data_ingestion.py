import os
import sys
sys.path.append('E:\pnl_calculator')
#from src.logger import logging
#from src.exception import CustomException
import pandas as pd
import tabula

from dataclasses import dataclass

file_path=input()

@dataclass
class DataIngestionConfig:
    pdf1_data_path: str=os.path.join('artifacts',"pdf1.csv")


class DataIngestion:
    def __init__(self):
        self.data_ingestion_conf=DataIngestionConfig()

    def initiate_data_ingestion(self):
        try:
            input_pdf = file_path
            output_pdf = DIR_OUTPUT + "convert_pdf_to_csv.csv"
    # Open PDF document
            document = ap.Document(input_pdf)
            save_option = ap.ExcelSaveOptions()
            save_option.format = ap.ExcelSaveOptions.ExcelFormat.CSV

            #df.to_csv(self.data_ingestion_conf.raw_data_path,index=False,header=True)
            #logging.info("Intiated the stock data")
            #logging.info("the data ingestion is completed")
            return(
                self.data_ingestion_conf.pdf1_data_path
            )
        except Exception as e:
            raise Exception(e)


if __name__=="__main__":
    obj=DataIngestion()
    obj.initiate_data_ingestion()

         
