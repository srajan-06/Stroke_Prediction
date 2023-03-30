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



        g1 = {"Male":1,"Female":0,"Other":3}
        m1 = {"Yes":1,"No":0}
        w1 = {"children":0,"Never_worked":1,"Private":2,"Govt_job":3,"Self-employed":4}
        r1 = {"Urban":0,"Rural":1}
        s1 = {"never smoked":0,"Unknown":1,"formerly smoked":2,"smokes":3}

        temp[0] = g1[temp[0]]
        temp[4] = m1[temp[4]]
        temp[5] = w1[temp[5]]
        temp[6] = r1[temp[6]]
        temp[9] = s1[temp[9]]

        import pandas as pd
        import numpy as np

        temp[1] = int(temp[1])
        temp[2] = int(temp[2])
        temp[3] = int(temp[3])
        temp[7] = float(temp[7])
        temp[8] = float(temp[8])

        print(temp)
        y_pred = model.predict([temp])

        if y_pred[0] == 1:
            y_pred  = 'POSITIVE'
        else:
            y_pred = 'NEGATIVE'
        return render(request,'explore/explore_result.html', {'result' : y_pred})
