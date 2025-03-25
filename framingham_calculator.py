#!/usr/bin/python3

'''
     FRAMINGHAM 10-YEAR RISK SCORES FOR CARDIAC EVENT

    BASED ON:   D’agostino RB, Vasan RS, Pencina MJ, Wolf PA, Cobain M, Massaro 
                JM, Kannel WB. General cardiovascular risk profile for use in 
                primary care. Circulation. 2008 Feb 12;117:743-53. PMID:18212285.
    SEE ALSO:   https://www.framinghamheartstudy.org/fhs-risk-functions/cardiovascular-disease-10-year-risk/

    VERS: 25MAR2025
'''

import pandas as pd
import numpy as np
import argparse

class FramScore:
    def __init__(self, age, sex, sbp, hypten, smoke, diab, bmi, type_score='10-year risk'):
        self.age_var = np.log(age)
        self.sex_var = sex
        self.hypten_var = hypten
        self.smoke_var = smoke
        self.diab_var = diab
        self.bmi = bmi
        self.sbp = sbp
        self.type_score = type_score

        if sex == 0:
            coef_dict = FramScore.coef_m
            self.power_var = 0.88431
            self.exp_var = 23.9388
        else:
            coef_dict = FramScore.coef_f
            self.power_var = 0.94833
            self.exp_var = 26.0145
        
        if type_score == 'all':
            risk_score = self.run_score(bmi, sbp, hypten, coef_dict, 'risk')
            opt_score = self.run_score(bmi, sbp, hypten, coef_dict, 'optimal')
            normal_score = self.run_score(bmi, sbp, hypten, coef_dict, 'normal')
            heart_score = self.run_score(bmi, sbp, hypten, coef_dict, 'heart age')
        else:
            returned_score = self.run_score(bmi, sbp, hypten, coef_dict, type_score)
    
    coef_m = {
        "age": 3.11296, 
        "sbp_utx": 1.85508,
        "sbp_tx": 1.92672,
        "smoke": 0.70953,
        "bmi": 0.79277,
        "diab": 0.5316
    }

    coef_f = {
        "age": 2.72107,
        "sbp_utx": 2.81291,
        "sbp_tx": 2.88267,
        "smoke": 0.61868,
        "bmi": 0.51125,
        "diab": 0.77763,
    }  

    def get_variable(self, var_name):
        return getattr(self, var_name, 0)

    def run_score(self, bmi, sbp, hypten_var, coef_dict, type_score):
        print(f'Calculating Framingham risk score for {type_score}...')
        if type_score == 'optimal':
            self.sbp_utx_var = 4.700480366
            self.bmi_var = 3.091042453
            for key in ["sbp_tx", "smoke", "diab"]:
                coef_dict.pop(key, None)
        elif type_score == 'normal':
            self.sbp_utx_var = 4.828313737
            self.bmi_var = 3.113515309
            for key in ["sbp_tx", "smoke", "diab"]:
                coef_dict.pop(key, None)
        else:
            self.bmi_var = np.log(self.bmi)
            self.sbp_utx_var = np.log(self.sbp) if hypten_var == 0 else None
            self.sbp_tx_var = np.log(self.sbp) if hypten_var == 1 else None

        beta_score = self.calc_beta(coef_dict)
        risk_score = self.calc_risk_score(beta_score)

        if type_score == 'heart age':
            returned_score = self.calc_heart_age(coef_dict, beta_score, risk_score)
        else:
            returned_score = risk_score
        
        print(f'{type_score}: {returned_score}')
        print()
        return returned_score


    def calc_beta(self, coef_dict):
        beta_sum = 0
        for key, item in coef_dict.items():
            if self.hypten_var == 1 and key == 'sbp_utx':
                continue
            elif self.hypten_var == 0 and key == 'sbp_tx':
                continue
            else:
                pass
            
            var_name = f"{key}_var"
            var = self.get_variable(var_name)
            # print(f'Var: {var_name}, {var}')
            beta_term = item * var
            beta_sum += beta_term

        # print(f'Beta: {beta_sum}')   
        return beta_sum
    
    def calc_risk_score(self, beta_score):

        risk_score = 1 - (self.power_var ** (np.exp(beta_score - self.exp_var)))
        return round(risk_score,3)
    
    def calc_heart_age(self, coef_dict, beta_score, risk_score):

        age_coef = coef_dict['age']

        beta_score_adj = beta_score - (age_coef * self.age_var)
        consti_num = np.exp(-(beta_score_adj - self.exp_var) / age_coef)
        consti_denom = (-np.log(self.power_var)) ** (1 / age_coef)
        consti = consti_num / consti_denom
        expo = 1 / age_coef
        term = (-np.log(1 - risk_score)) ** expo
        heart_age = term * consti

        return heart_age

if __name__ =='__main_':

    parser = argparse.ArgumentParser(description="Description: Calculates 10-year \
                                 risk for cardiac event.")
    parser.add_argument("sex", type=int, help="Sex of patient. 0: male, 1: female")
    parser.add_argument("age", type=int, help="Age of patient in whole years")
    parser.add_argument("sbp", type=int, help="Systolic blood pressure in mmHg")
    parser.add_argument("hypten", type=int, help="Patient hypertension status: 0 untreated, 1 treated")
    parser.add_argument("smoke", type=int, help="Patient smoking status, 0 not smoking, 1 currently smoking")
    parser.add_argument("diab", type=int, help="Patient diabetes status, 0 no diabetes, 1 diabetes")
    parser.add_argument("bmi", type=float, help="BMI of patient in kg/m2. \
                        See options: --weight, --height, --metric")
    parser.add_argument("weight", type=float, required=False, help="Patient \
                        weight for BMI. Pass --metric 0 if in pounds")
    parser.add_argument("height", type=float, required=False, help="Patient \
                        height for BMI. Pass --metric 0 if in inches")
    parser.add_argument("metric", type=int, required=False, help="Units for \
                        BMI calculation: 0 lb:inches, 1 kg:m^2")

    args = parser.parse_args()  
    sex = args.sex 
    age = args.age
    sbp = args.sbp
    hypten = args.hypten
    smoke = args.smoke
    diab = args.diab
    if args.height and args.weight:
        if args.metric == 1:
            bmi = args.weight / args.height
        else:
            # imperial -- metric conversion

            print()
    else:
        bmi = args.bmi

    fram_obj = FramScore(age, sex, sbp, hypten, smoke, diab, bmi)

