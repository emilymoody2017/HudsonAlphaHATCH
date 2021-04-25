# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 14:12:55 2021

@author: emoody
"""
from sys             import version_info

from PyQt5.QtWidgets import QFrame
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout
from PyQt5.QtWidgets import QPlainTextEdit
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QComboBox, QDialogButtonBox


class SurveyWindow(QFrame):
    def __init__(self):
        if version_info[0] == 3:
            super().__init__()
        else:
            super(SurveyWindow,self).__init__()
        # Establish basic window shape
        self.setWindowTitle('Survey')
        
        self.setStyleSheet('background-color: rgb(255,180,188);')
        self.output = ""
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        
        
        # Alteration on BRCA1
        in1label = QLabel()
        in1label.setText('Do you have an inherited alteration on the BRCA1 '
                         'gene?')
        self.inherit1ComboBox = QComboBox()
        self.inherit1ComboBox.setStyleSheet('background-color: white;')
        self.inherit1ComboBox.addItems(['', 'Yes', 'No', 'I don\'t know'])
        brca1layout = QHBoxLayout()
        brca1layout.addWidget(in1label)
        brca1layout.addWidget(self.inherit1ComboBox)
        self.layout.addLayout(brca1layout)
        # self.layout.addSpace(15)
        
        # Alteration on BRCA2
        in2label = QLabel()
        in2label.setText('Do you have an inherited alteration on the BRCA2 '
                         'gene?')
        self.inherit2ComboBox = QComboBox()
        self.inherit2ComboBox.setStyleSheet('background-color: white;')
        self.inherit2ComboBox.addItems(['', 'Yes', 'No', 'I don\'t know'])
        brca2layout = QHBoxLayout()
        brca2layout.addWidget(in2label)
        brca2layout.addWidget(self.inherit2ComboBox)
        self.layout.addLayout(brca2layout)
        
        # Ethnicity 
        ethlabel = QLabel()
        ethlabel.setText('What is your ethnicity?')
        self.ethComboBox = QComboBox()
        self.ethComboBox.setStyleSheet('background-color: white;')
        self.ethComboBox.addItems(['', 'White', 'Hispanic', 
                                   'Asian/Pacific Islander', 'Black', 'Other'])
        ethlayout = QHBoxLayout()
        ethlayout.addWidget(ethlabel)
        ethlayout.addWidget(self.ethComboBox)
        self.layout.addLayout(ethlayout)
        
        # Age
        agelabel = QLabel()
        agelabel.setText('What range best represents your age?')
        self.ageComboBox = QComboBox()
        self.ageComboBox.setStyleSheet('background-color: white;')
        self.ageComboBox.addItems(['', '18 or younger', '19-29', '30-39', 
                                   '40-50', '51-60', '61-70', '70+'])
        agelayout = QHBoxLayout()
        agelayout.addWidget(agelabel)
        agelayout.addWidget(self.ageComboBox)
        self.layout.addLayout(agelayout)
        
        # Menstruation
        menslabel = QLabel()
        menslabel.setText('Did you start menstruation before 12 years old?')
        self.mensComboBox = QComboBox()
        self.mensComboBox.setStyleSheet('background-color: white;')
        self.mensComboBox.addItems(['', 'Yes', 'No', 'Does not apply to me'])
        menslayout = QHBoxLayout()
        menslayout.addWidget(menslabel)
        menslayout.addWidget(self.mensComboBox)
        self.layout.addLayout(menslayout)
        
        # Menopause
        menolabel = QLabel()
        menolabel.setText('Did you begin menopause after age 55?')
        self.menoComboBox = QComboBox()
        self.menoComboBox.setStyleSheet('background-color: white;')
        self.menoComboBox.addItems(['', 'Yes', 'No', 'Does not apply to me'])
        menolayout = QHBoxLayout()
        menolayout.addWidget(menolabel)
        menolayout.addWidget(self.menoComboBox)
        self.layout.addLayout(menolayout)
        
        # HRT
        chrtlabel = QLabel()
        chrtlabel.setText('Have you taken combination hormone replacement '
                          'therapy, even for a short time?')
        self.chrtComboBox = QComboBox()
        self.chrtComboBox.setStyleSheet('background-color: white;')
        self.chrtComboBox.addItems(['', 'Yes', 'No'])
        chrtlayout = QHBoxLayout()
        chrtlayout.addWidget(chrtlabel)
        chrtlayout.addWidget(self.chrtComboBox)
        self.layout.addLayout(chrtlayout)
        
        # EHRT
        ehrtlabel = QLabel()
        ehrtlabel.setText('Have you taken estrogen hormone replacement therapy'
                          ' for 10 or more years?')
        self.ehrtComboBox = QComboBox()
        self.ehrtComboBox.setStyleSheet('background-color: white;')
        self.ehrtComboBox.addItems(['', 'Yes', 'No'])
        ehrtlayout = QHBoxLayout()
        ehrtlayout.addWidget(ehrtlabel)
        ehrtlayout.addWidget(self.ehrtComboBox)
        self.layout.addLayout(ehrtlayout)
        
        
        # des
        deslabel = QLabel()
        deslabel.setText('Have you taken diethylstillbestrol (DES)?')
        self.desComboBox = QComboBox()
        self.desComboBox.setStyleSheet('background-color: white;')
        self.desComboBox.addItems(['', 'Yes', 'No', 'I don\'t know'])
        deslayout = QHBoxLayout()
        deslayout.addWidget(deslabel)
        deslayout.addWidget(self.desComboBox)
        self.layout.addLayout(deslayout)
        
        
        # mothers des
        mdeslabel = QLabel()
        mdeslabel.setText('Has your mother taken diethylstillbestrol (DES) '
                          'between 1940-1971?')
        self.mdesComboBox = QComboBox()
        self.mdesComboBox.setStyleSheet('background-color: white;')
        self.mdesComboBox.addItems(['', 'Yes', 'No', 'I don\'t know'])
        mdeslayout = QHBoxLayout()
        mdeslayout.addWidget(mdeslabel)
        mdeslayout.addWidget(self.mdesComboBox)
        self.layout.addLayout(mdeslayout)
        
        # dense tissue
        pretlabel = QLabel()
        pretlabel.setText('Do you have dense breast tissue, and at what age?')
        self.pretComboBox = QComboBox()
        self.pretComboBox.setStyleSheet('background-color: white;')
        self.pretComboBox.addItems(['', 'Premenopausal', 'Postmenopausal', 
                                    'No', 'I don\'t know'])
        pretlayout = QHBoxLayout()
        pretlayout.addWidget(pretlabel)
        pretlayout.addWidget(self.pretComboBox)
        self.layout.addLayout(pretlayout)
        
        
        # Children
        chilabel = QLabel()
        chilabel.setText('When did you give birth to your first child?')
        self.chiComboBox = QComboBox()
        self.chiComboBox.setStyleSheet('background-color: white;')
        self.chiComboBox.addItems(['', 'before 20', '21-34', 'After 35', 
                                   'Never had children'])
        chilayout = QHBoxLayout()
        chilayout.addWidget(chilabel)
        chilayout.addWidget(self.chiComboBox)
        self.layout.addLayout(chilayout)
        
        canlabel = QLabel()
        canlabel.setText('How many of your close relatives have had breast, ovarian, '
                         'or prostate cancer?')
        self.canComboBox = QComboBox()
        self.canComboBox.setStyleSheet('background-color: white;')
        self.canComboBox.addItems(['', '0', '1', '2', '3', 
                                   '4 or more'])
        canlayout = QHBoxLayout()
        canlayout.addWidget(canlabel)
        canlayout.addWidget(self.canComboBox)
        self.layout.addLayout(canlayout)
        
        
        
        
        
        # End
        self.buttonBox = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.buttonBox.setStyleSheet('background-color: white;')
        self.buttonBox.accepted.connect(self.submit_it)
        self.buttonBox.rejected.connect(self.reject)
        self.layout.addWidget(self.buttonBox)
        
        
 
    def setFlag(self, s):
        self.output += '- ' + s + '\n'      
 
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
        
    def submit_it(self):
        r = 0
        if(self.inherit1ComboBox.currentText()=='Yes'):
            self.setFlag('An inherited alteration on BRCA1 makes risk of '
                         'development'
                         ' 72% by age 80.')
            r+=120
        if(self.inherit2ComboBox.currentText()=='Yes'):
            self.setFlag('An inherited alteration on BRCA2 makes risk of '
                         'development 69% by age 80.')
            r+=110
        if(self.ethComboBox.currentText()=='White'):
            self.setFlag('12.2 per 100,000 white women have ovarian cancer.')
            r+=15
        if(self.ethComboBox.currentText()=='Hispanic'):
            self.setFlag('10.6 per 100,000 hispanic women have ovarian '
                         'cancer.')
            r+=12
        if(self.ethComboBox.currentText()=='Asian/Pacific Islander'):
            self.setFlag('9.5 per 100,000 Asian/Pacific Islander women have '
                         'ovarian cancer.')
            r+=10
        if(self.ethComboBox.currentText()=='Black'):
            self.setFlag('9.4 per 100,000 black women have ovarian cancer.')
            r+=9.5
        if(self.ageComboBox.currentText()=='40-50'):
            self.setFlag('1 in 68 women have a risk of developing breast '
                         'cancer between the ages of 40 to 50.')
            r+=40
        elif(self.ageComboBox.currentText()=='51-60'):
            self.setFlag('1 in 42 women have a risk of developing breast cancer '
                         'between the ages of 50 to 60.')
            r+=50
        elif(self.ageComboBox.currentText()=='61-70'):
            self.setFlag('1 in 28 women have a risk of developing breast cancer '
                         'between the ages of 60 to 70.')
            r+=60
        elif(self.ageComboBox.currentText()=='70+'):
            self.setFlag('1 in 26 women have a risk of developing breast cancer '
                         'at 70+ years old.')
            r+=63
        if(self.mensComboBox.currentText()=='Yes'):
            self.setFlag('Longer or higher exposure to reproductive hormones, '
                         'like estrogen and progesterone, increase risk of '
                         'cancer. 80% of all breast cancers grow according'
                         ' to estrogen supply.')
            r+=30
        if(self.menoComboBox.currentText()=='Yes'):
            self.setFlag('Longer or higher exposure to reproductive hormones, '
                         'like estrogen and progesterone, increase risk of '
                         'cancer. 80% of all breast cancers grow according'
                         ' to estrogen supply.')
            r+=30
        if(self.chrtComboBox.currentText()=='Yes'):
            self.setFlag('Combination Hormone Replacement Therapy will increase'
                         ' the risk of breast cancer by 75% even if it was only'
                         ' used for a short time.')
            r+=90
        if(self.ehrtComboBox.currentText()=='Yes'):
            self.setFlag('Estrogen-only combination hormone replacement therapy'
                         ' increases risk of breast cancer if used for 10 or more'
                         ' years.')
            r+=15
        if(self.desComboBox.currentText()=='Yes'):
            self.setFlag('Taking DES gives you a 20-30% increased chance of getting'
                         ' breast cancer.')
            r+=45
        if(self.mdesComboBox.currentText()=='Yes'):
            self.setFlag('Your mother taking DES gives you a 20-30% increased '
                         'chance of getting breast cancer.')
            r+=40
        if(self.pretComboBox.currentText()=='Premenopausal'):
            self.setFlag('Dense breast tissue is a huge risk factor for breast '
                         'cancer in 39% of premenopausal women.')
            r+=45
        elif(self.pretComboBox.currentText()=='Postmenopausal'):
            self.setFlag('Dense breast tissue is a huge risk factor for breast '
                         'cancer in 26% of postmenopausal women.')
            r+=40
        if(self.chiComboBox.currentText()=='After 35'):
            self.setFlag('Women who have their first child after 35 are 40% more'
                         ' likely to develop breast cancer than if the first child'
                         ' was born before the mother was 20.')
            r+=50
        elif(self.chiComboBox.currentText()=='Never had children'):
            self.setFlag('Women who never have children have a higher risk of '
                         'breast cancer than women who have their children '
                         'before 34, but a slightly lower chance of developing'
                         ' cancer than those who have a child after 35.')
            r+=45
        if(self.canComboBox.currentText()=='1'):
            self.setFlag('Having an immediate relative with a cancer increases'
                         ' chances of getting a similar cancer dramatically.')
            r+=10
        elif(self.canComboBox.currentText()=='2'):
            self.setFlag('Having an immediate relative with a cancer increases'
                         ' chances of getting a similar cancer dramatically.')
            r+=20
        elif(self.canComboBox.currentText()=='3'):
            self.setFlag('Having an immediate relative with a cancer increases'
                         ' chances of getting a similar cancer dramatically.')
            r+=30
        elif(self.canComboBox.currentText()=='4 or more'):
            self.setFlag('Having an immediate relative with a cancer increases'
                         ' chances of getting a similar cancer dramatically.')
            r+=40
        
        print(r)
        
        self.setFlag('Please consult your doctor for more accurate results on'
                     ' cancer and your risk.')
        # print(self.output)
        self.textbox = QPlainTextEdit()
        if(r < 100):
            self.textbox.setPlainText('RISK LEVEL: LOW\nDetails:\n' + self.output)
        elif(r < 220):
            self.textbox.setPlainText('RISK LEVEL: MEDIUM\nDetails:\n' + self.output)
        else:
            self.textbox.setPlainText('RISK LEVEL: HIGH\nDetails:\n' + self.output)
        self.textbox.setWindowTitle('Results')
        self.textbox.resize(750,750)
        self.textbox.show()
        self.output = ""
        
    def reject(self):
        self.close()
        
        
        