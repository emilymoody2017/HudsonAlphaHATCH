# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 18:53:52 2021

@author: emoody
"""
from PyQt5.QtWidgets import QFileDialog
UIGetFile = QFileDialog.getOpenFileName
import pandas as pd

def load_data():
    file = UIGetFile(caption='Please load a .csv file.')[0] 
    # print(file)
    df = pd.read_csv(file)
    #print(df)
    return df

