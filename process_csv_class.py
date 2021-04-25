# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 19:11:57 2021

@author: emoody
"""
import pandas as pd

class process_csv():
    def __init__(self, file):
        self.df = file.transpose()
        #self.df.transpose()
        self.output = ''
        self.yesses = {'Y', 'y', 'Yes', 'yes','True', 'true', 'Yea', 'yea'}
        self.nos = {'n', 'N', 'No', 'no', 'False', 'false', 'Nope', 'nope'}
        
    def setFlag(self, s):
        self.output += '- ' + s + '\n'
        
        
    def process_it(self):
        risk_eval = ''
        r = 0
        
        for x in range(len(self.df.columns)):
            s = pd.Series(self.df[x].values)
            risk_eval +='====== Results for: ' + s[0] + '======\n'
            # 0: name, 1: age menopause started, 2: CHRT, 3: EHRT,
            # 4: DES, 5: mDES, 6: breast tissue, 7: birth of firstborn,
            # 8: family history
            
            
            # BRCA1
            if(s[1] in self.yesses):
                self.setFlag('An inherited alteration on BRCA1 makes risk of development'
                             ' 72% by age 80.')
                r+=120
                
            # BRCA2
            if(s[2] in self.yesses):
                self.setFlag('An inherited alteration on BRCA2 makes risk of development'
                    ' 69% by age 80.')
                r+=110
                
            # age
            try:
                age = int(s[3])
                if(age >= 40 and age < 50):
                    self.setFlag('1 in 68 women have a risk of developing breast cancer '
                                 'between the ages of 40 to 50.')
                    r+=40
                elif(age >= 50 and age < 60):
                    self.setFlag('1 in 42 women have a risk of developing breast cancer '
                                 'between the ages of 50 to 60.')
                    r+=50
                elif(age >= 60 and age < 70):
                    self.setFlag('1 in 28 women have a risk of developing breast cancer '
                                 'between the ages of 60 to 70.')
                    r+=60
                elif(age >= 70):
                    self.setFlag('1 in 26 women have a risk of developing breast cancer '
                                 'at 70+ years old.')
                    r+=63
            except:
                pass
                                
            # menstruation
            try:
                mens = int(s[4])
                if(mens < 12):
                    self.setFlag('Longer or higher exposure to reproductive hormones, '
                                 'like estrogen and progesterone, increase risk of '
                                 'cancer. 80% of all breast cancers grow according'
                                 ' to estrogen supply.')
                    r+=30
            except:
                pass
            # menopause
            try:
                meno = int(s[5])
                if(meno>55):
                    self.setFlag('Longer or higher exposure to reproductive hormones, '
                                 'like estrogen and progesterone, increase risk of '
                                 'cancer. 80% of all breast cancers grow according'
                                 ' to estrogen supply.')
                    r+=30
            except:
                pass
            
            # CHRT
            if(s[6] in self.yesses):
                self.setFlag('Combination Hormone Replacement Therapy will increase'
                             ' the risk of breast cancer by 75% even if it was only'
                             ' used for a short time.')
                r+=90
           
            # EHRT
            if(s[7] in self.yesses):
                self.setFlag('Estrogen-only combination hormone replacement therapy'
                             ' increases risk of breast cancer if used for 10 or more'
                             ' years.')
                r+=15
                
            # DES
            if(s[8] in self.yesses):
                self.setFlag('Taking DES gives you a 20-30% increased chance of getting'
                             ' breast cancer.')
                r+=45
                
            # mDES
            if(s[9] in self.yesses):
                self.setFlag('Your mother taking DES gives you a 20-30% increased '
                             'chance of getting breast cancer.')
                r+=40
                
            # breast tissue
            try:
                bage = int(s[10])
                if(bage < 51):
                    self.setFlag('Dense breast tissue is a huge risk factor for breast '
                                 'cancer in 39% of premenopausal women.')
                    r+=45
                elif(bage >=51):
                    self.setFlag('Dense breast tissue is a huge risk factor for breast '
                                 'cancer in 26% of postmenopausal women.')
                    r+=40
            except:
                pass
            
            # Childen age
            try:
                cage = int(s[11])
                if(cage>35):
                    self.setFlag('Women who have their first child after 35 are 40% more'
                                 ' likely to develop breast cancer than if the first child'
                                 ' was born before the mother was 20.')
                    r+=50
            except:
                self.setFlag('Women who never have children have a higher risk of '
                             'breast cancer than women who have their children '
                             'before 34, but a slightly lower chance of developing'
                             ' cancer than those who have a child after 35.')
                r+=45
                
            # Cancer history
            
            
            
            # Ethnicity
            white = {'white', 'White', 'Caucasian', 'caucasian', 'European', 'Western European', 'European-descent'}
            black = {'black', 'Black', 'African', 'african', 'African-American', 'African American'}
            asian = {'Asian', 'asian', 'Pacific Islander', 'pacific islander', 'pacific', 'Pacific'}
            hisp = {'Hispanic', 'hispanic', 'Latina', 'latina', 'Latino', 'latino', 'Latinx', 'latinx'}
            
            if(s[12] in white):
                self.setFlag('12.2 per 100,000 white women have ovarian cancer.')
                r+=15
            elif(s[12] in hisp):
                self.setFlag('10.6 per 100,000 hispanic women have ovarian '
                             'cancer.')
                r+=12
            if(s[12] in asian):
                self.setFlag('9.5 per 100,000 Asian/Pacific Islander women have '
                             'ovarian cancer.')
                r+=10
            if(s[12] in black):
                self.setFlag('9.4 per 100,000 black women have ovarian cancer.')
                r+=9.5
                
            cancers = ['breast', 'breast cancer', 'prostate', 'prostate cancer', 'ovarian', 'ovarian cancer']
            try:
                l = s[13].split(', ')
                for item in l:
                    if item in cancers:
                        r+=20
                        self.setFlag('Having an immediate relative with a cancer increases'
                                     ' chances of getting a similar cancer dramatically.')
            except:
                if s[13] in cancers:
                    r+=20
                    self.setFlag('Having an immediate relative with a cancer increases'
                                 ' chances of getting a similar cancer dramatically.')
            
            
            risk_eval += 'RISK LEVEL: '
            if(r < 100):
                risk_eval += 'LOW\nDetails:\n'
            elif(r < 220):
                risk_eval += 'MEDIUM\nDetails:\n'
            else:
                risk_eval += 'HIGH\nDetails:\n'
            risk_eval += self.output
            self.output = ''
            r = 0
            
        
        
        
        return risk_eval
        