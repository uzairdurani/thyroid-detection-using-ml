from django import forms, http
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import newForm
from django.template.defaulttags import register
import pickle
from sklearn.preprocessing import StandardScaler, LabelEncoder, MinMaxScaler


def home(request):
    form = newForm()
    return render(request, 'home.html', {'form': form})


reg_model = pickle.load(open('Logistic Regression.pickle', 'rb'))
svm_model = pickle.load(open('Support Vector Machine.pickle', 'rb'))
rf_model = pickle.load(open('Random Forest.pickle', 'rb'))
scaler = pickle.load(open('scalermodel.pickle', 'rb'))


def predict(request):
    global reg_model
    if request.method == 'POST':
        form = newForm(request.POST)
        if form.is_valid():
            AGE = form.cleaned_data['AGE']
            TSH = form.cleaned_data['TSH']
            T3 = form.cleaned_data['T3']
            TT4 = form.cleaned_data['TT4']
            T4U = form.cleaned_data['T4U']
            FTI = form.cleaned_data['FTI']

            SURGERY = int(form.cleaned_data['SURGERY'])

            SEX = int(form.cleaned_data['SEX'])

            # data = [AGE, TT4, FTI]
            AGE = scaler.transform([[AGE]])[0][0]
            TT4 = scaler.transform([[TT4]])[0][0]
            FTI = scaler.transform([[FTI]])[0][0]

            # SURGERY = LabelEncoder().fit_transform([SURGERY])
            # SEX = LabelEncoder().fit_transform([SEX])
            # print(SURGERY, SEX)

            data = [AGE, SEX, SURGERY, TSH, T3, TT4, T4U, FTI]
            # prediction = format(reg_model.predict(data)[0], '.2f')

            prediction = reg_model.predict([data])[0]
            prediction_svm = svm_model.predict([data])[0]
            prediction_rf = rf_model.predict([data])[0]

            # print(prediction[0], prediction_svm[0], prediction_rf[0])
            predictions = [prediction, prediction_svm, prediction_rf]
            count_1 = 0
            count_0 = 0
            for i in range(len(predictions)):
                if predictions[i] == 1:
                    count_1 += 1
                else:
                    count_0 += 1
            final_prediction = None
            if count_1 > count_0:
                final_prediction = 'Postive'
            else:
                final_prediction = "Negative"
            print(predictions, final_prediction)
            return render(request, 'home.html', {'form': form, 'finalPrediction': final_prediction, 'predictions': predictions})
        else:
            error = form.errors.as_data()
            print(error)

            return render(request, 'home.html', {'message': error, 'form': form})
    return HttpResponse('Please Enter Data From Home Page')


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)[0]
