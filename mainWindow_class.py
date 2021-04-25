# -*- coding: utf-8 -*-
################################################################################
# HATCH - Hudson Alpha Tech Challenge
# Emmkay
# 
# Main Window Graphics Class
################################################################################

################################################################################
# Libraries
from sys             import version_info

import pandas as pd
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout
from PyQt5.QtWidgets import QPlainTextEdit
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QFileDialog


################################################################################
# Classes
from load_data_file import load_data
from process_csv_class import process_csv
from surveyWindow_class import SurveyWindow


################################################################################
# MainWindow
class MainWindow(QMainWindow):
    def __init__(self):
        if version_info[0] == 3:
            super().__init__()
        else:
            super(MainWindow,self).__init__()
        # Establish basic window shape
        self.setWindowTitle('Domo Arigato Mr Robato!')
        
        self.setStyleSheet('background-color: rgb(255,180,188);')
        # self.setFont('Sans Serif')
        #self.setFixedSize(QSize(1000,400))
        self.survey_widget = []
        self.survey_data = 0
        self.output = ''
        self.df = pd.DataFrame()
        
        
        self.save_file = QPushButton('Download .csv file')
        self.save_file.setStyleSheet('background-color: white;')
        self.save_file.setToolTip('Download a copy of the survey to fill out here.')
        self.save_file.clicked.connect(self.get_file)
        
        
        
        self.choose_file = QPushButton('Choose .csv file to evaluate multiple patients')
        self.choose_file.setStyleSheet('background-color: white;')
        self.choose_file.setToolTip('If you have already filled out the survey, upload it here.')
        self.choose_file.clicked.connect(self.pick_file)
        
        self.calc = QPushButton('Calculate risk')
        self.calc.setStyleSheet('background-color: white;')
        self.calc.clicked.connect(self.calculate)
        
        self.surv = QPushButton('Take the survey for a single patient')
        self.surv.setStyleSheet('background-color: white;')
        self.surv.setToolTip('If you have not filled out a survey already, you can take it in real time here.')
        self.surv.clicked.connect(self.survey)
        
        self.textbox = QPlainTextEdit()
        self.textbox.setReadOnly(True)
        self.textbox.setStyleSheet('background-color: white;')
        self.display_it('Press \'Download .csv file\' to download the template for the program.\n'
                        'Press \'Choose .csv file\' to evaluate multiple patients\' to select a filled'
                        '-out file for use.\n'
                        'Press \'Calculate risk\' to display the results of the selected file.\n'
                        'Press \'Save to a file\' to save the results of the selected file to in'
                        ' a .txt format.\n'
                        'Press \'Take the survey for a single patient\' in order to get a single'
                        ' person\'s results quickly and easily.')
        
        self.save = QPushButton('Save to a file')
        self.save.setStyleSheet('background-color: white;')
        self.save.setToolTip('Please select a .csv above and use this button to save the results to a .txt file.')
        self.save.clicked.connect(self.saveit)
        
        label1 = QLabel()
        label1.setText('Results')
        
        label2 = QLabel()
        label2.setText(' or ')
        
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.save_file)
        button_layout.addWidget(self.choose_file)
        button_layout.addWidget(self.calc)
        button_layout.addWidget(label2)
        button_layout.addWidget(self.surv)
        
        other_layout = QVBoxLayout()
        other_layout.addLayout(button_layout)
        other_layout.addWidget(label1)
        other_layout.addWidget(self.textbox)
        other_layout.addWidget(self.save)
        
        self.main_widget = QWidget()
        self.main_widget.setLayout(other_layout)
        self.setCentralWidget(self.main_widget)
        
        
        
        
    def pick_file(self, s):
        self.df = load_data()
        self.display_it('Data successfully uploaded.')
    
        
    
    def calculate(self, s):
        #try:
        self.the_class = process_csv(self.df)
        self.output = str(self.the_class.process_it())
        self.display_it(self.output)
        #except:
         #   self.display_it('Error: Please attach a csv file above.')
    
    def display_it(self, string):
        self.textbox.setPlainText(string)
        
    def survey(self, s):
        self.survey_widget = SurveyWindow()
        self.survey_widget.show()
    
    def get_file(self, s):
        mydf = pd.read_csv('template.csv')
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(
            self, "Save File", r"H:\DomoArigato.csv", "CSV Files (*.csv)", options=options
        )
        mydf.to_csv(fileName)
        self.display_it('File successfully downloaded.')
        
    def saveit(self, s):
        if(self.df.empty):
            self.display_it('Please upload a file above.')
        else:
            self.the_class = process_csv(self.df)
            self.output = str(self.the_class.process_it())
            #f = open(self.output, 'rb')
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            fileName, _ = QFileDialog.getSaveFileName(
                self, "Save File", r"H:\results.txt", "TXT Files (*.txt)", options=options
                )
            if fileName:
                with open(fileName, "wb") as f:
                    f.write(bytes(self.output, 'utf-8'))
                self.display_it('File successfully saved.')

        