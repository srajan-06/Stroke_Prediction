from django.shortcuts import render

from joblib import load
model = load('./savedModels/model.joblib')

from django.urls import reverse_lazy


from django.contrib.auth import get_user_model
User = get_user_model()

def Predictor(request):
    return render(request,'explore/explore_ipop.html')
    success_url = reverse_lazy('explore:pred')

def formInfo(request):

    if request.method == 'POST':
        temp = []
        temp.append(request.POST.get('gender'))
        temp.append(request.POST.get('age'))
        temp.append(request.POST.get('hypertension'))
        temp.append(request.POST.get('heart_disease'))
        temp.append(request.POST.get('ever_married'))
        temp.append(request.POST.get('work_type'))
        temp.append(request.POST.get('Residence_type'))
        temp.append(request.POST.get('avg_glucose_level'))
        temp.append(request.POST.get('bmi'))
        temp.append(request.POST.get('smoking_status'))



        g1 = {"Male":1,"Female":0,"Other":2}


        temp[0] = g1[temp[0]]

        import pandas as pd
        import numpy as np
        print(temp)

        temp[1] = int(temp[1])
        temp[2] = int(temp[2])
        temp[3] = int(temp[3])
        temp[4] = int(temp[4])
        temp[5] = int(temp[5])
        temp[6] = int(temp[6])
        temp[7] = float(temp[7])
        temp[8] = float(temp[8])
        temp[9] = int(temp[9])

        print(temp)
        y_pred = model.predict([temp])

        if y_pred[0] == 1:
            y_pred  = 'POSITIVE'
        else:
            y_pred = 'NEGATIVE'
        return render(request,'explore/explore_result.html', {'result' : y_pred})
