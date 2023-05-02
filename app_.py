# -*- coding: utf-8 -*-
"""
Created on Tue May  2 16:34:44 2023

@author: HP
"""

from flask import Flask,render_template,request
import pickle

app = Flask(__name__)
model = pickle.load(open('chronic_kidney_model.pkl','rb'))

@app.route('/')
def home():
    return '<center><h1> Chronic Kidney Disorder Prediction!</h1></center>'

@app.route('/predict',methods=['GET','POST'])
def predict():
    
    if request.method=='POST':
        
        input_features = [float(x) for x in request.form.values()]
        age= input_features[0]
        blood_pressure = input_features[1]
        specific_gravity= input_features[2]
        albumin= input_features[3]
        sugar= input_features[4]
        red_blood_cells= input_features[5]
        pus_cell= input_features[6]
        pus_cell_clumps= input_features[7]
        bacteria = input_features[8]
        blood_glucose_random= input_features[9]
        blood_urea = input_features[10]
        serum_creatinine= input_features[11]
        sodium= input_features[12]
        potassium= input_features[13]
        haemoglobin= input_features[14]
        packed_cell_volume= input_features[15] 
        white_blood_cell_count = input_features[16] 
        red_blood_cell_count = input_features[17]
        hypertension= input_features[18] 
        diabetes_mellitus= input_features[19]
        coronary_artery_disease= input_features[20] 
        appetite=input_features[21] 
        peda_edema= input_features[22]
        aanemia = input_features[23]
        
        value = [age, blood_pressure, specific_gravity, albumin, sugar,
                 red_blood_cells, pus_cell, pus_cell_clumps, bacteria,
                 blood_glucose_random, blood_urea, serum_creatinine, sodium,
                 potassium, haemoglobin, packed_cell_volume,
                 white_blood_cell_count, red_blood_cell_count, hypertension,
                 diabetes_mellitus, coronary_artery_disease, appetite,
                 peda_edema, aanemia]
        
        predictions_=model.predict(value)
        
        return render_template('index_chronic_kd.html', predictions_text ='Status of Disorder {}'.format(predictions_))
    
    return render_template('index_chronic_kd.html')

if __name__ =='__main__':
    app.run()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        