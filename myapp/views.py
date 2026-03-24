from django.shortcuts import render, redirect, get_object_or_404
from .models import Patient
import pickle
import os

def patient_home(request):
    patients = Patient.objects.all()
    return render(request, "home.html", {"patients": patients})

def patient_reg(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        age = request.POST.get('age', '')
        gender = request.POST.get('gender', '')
        height = request.POST.get('height', '')
        weight = request.POST.get('weight', '')
        address = request.POST.get('address', '')
        phone = request.POST.get('phone', '')
        email = request.POST.get('email', '')
        date = request.POST.get('date', '')
        disease = request.POST.get('disease', '')
        cost = request.POST.get('cost', 0)

        patient = Patient(
            name=name,
            age=age,
            gender=gender,
            height=height,
            weight=weight,
            address=address,
            phone=phone,
            email=email,
            date=date,
            disease=disease,
            cost=cost
        )
        patient.save()
        return redirect('home')

    return render(request, "reg.html")

def delete_patient(request, patient_id):
    patient = get_object_or_404(Patient, patient_id=patient_id)  # id -> patient_id
    patient.delete()
    return redirect('home')

def edit_patient(request, patient_id):
    patient = get_object_or_404(Patient, patient_id=patient_id)  # id -> patient_id
    return render(request, "edit.html", {"patient": patient})

from django.shortcuts import get_object_or_404

from django.shortcuts import render, redirect, get_object_or_404
from .models import Patient

def update_patient(request):
    if request.method == 'POST':
        patient_id = request.POST.get('patient_id')

        # Make sure you are using get_object_or_404 for proper error handling
        patient = get_object_or_404(Patient, patient_id=patient_id)

        patient.name = request.POST.get('name')
        patient.age = request.POST.get('age')
        patient.gender = request.POST.get('gender')
        patient.height = request.POST.get('height')
        patient.weight = request.POST.get('weight')
        patient.address = request.POST.get('address')
        patient.phone = request.POST.get('phone')
        patient.email = request.POST.get('email')
        patient.date = request.POST.get('date')
        patient.disease = request.POST.get('disease')
        patient.cost = request.POST.get('cost')
        patient.save()

        return redirect('home')  # or wherever you want to redirect
    else:
        return redirect('home')




# Diabetes prediction
def index(request):
    if request.method == 'POST':
        try:
            NP = float(request.POST.get('NP'))
            GL = float(request.POST.get('GL'))
            BPL = float(request.POST.get('BPL'))
            SKV = float(request.POST.get('SKV'))
            IL = float(request.POST.get('IL'))
            IBMV = float(request.POST.get('IBMV'))
            DPFV = float(request.POST.get('DPFV'))
            AP = float(request.POST.get('AP'))
        except (TypeError, ValueError):
            return render(request, "index.html", {'error': 'Invalid input!'})

        path = os.path.dirname(__file__)
        model_path = os.path.join(path, 'diabetes.pkl')

        with open(model_path, 'rb') as f:
            model = pickle.load(f)
        res = int(model.predict([[NP, GL, BPL, SKV, IL, IBMV, DPFV, AP]])[0])

        return render(request, "index.html", {'res': res})

    return render(request, "index.html")


# Heart disease prediction
def heart(request):
    if request.method == 'POST':
        try:
            age = float(request.POST.get('age'))
            sex = float(request.POST.get('sex'))
            cp = float(request.POST.get('cp'))
            trestbps = float(request.POST.get('trestbps'))
            chol = float(request.POST.get('chol'))
            fbs = float(request.POST.get('fbs'))
            restecg = float(request.POST.get('restecg'))
            thalach = float(request.POST.get('thalach'))
            exang = float(request.POST.get('exang'))
            oldpeak = float(request.POST.get('oldpeak'))
            slope = float(request.POST.get('slope'))
            ca = float(request.POST.get('ca'))
            thal = float(request.POST.get('thal'))
        except (TypeError, ValueError):
            return render(request, "heart.html", {'error': 'Invalid input!'})

        path = os.path.dirname(__file__)
        model_path = os.path.join(path, 'dataset.pkl')

        with open(model_path, 'rb') as f:
            model = pickle.load(f)
        res = int(model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])[0])

        return render(request, "heart.html", {'res': res})

    return render(request, "heart.html")


# Parkinson's prediction
def parkinson(request):
    if request.method == 'POST':
        try:
            fo = float(request.POST.get('fo'))
            fhi = float(request.POST.get('fhi'))
            flo = float(request.POST.get('flo'))
            jitter_percent = float(request.POST.get('jitter_percent'))
            jitter_abs = float(request.POST.get('jitter_abs'))
            rap = float(request.POST.get('rap'))
            ppq = float(request.POST.get('ppq'))
            ddp = float(request.POST.get('ddp'))
            shimmer = float(request.POST.get('shimmer'))
            shimmer_db = float(request.POST.get('shimmer_db'))
            apq3 = float(request.POST.get('apq3'))
            apq5 = float(request.POST.get('apq5'))
            apq = float(request.POST.get('apq'))
            dda = float(request.POST.get('dda'))
            nhr = float(request.POST.get('nhr'))
            hnr = float(request.POST.get('hnr'))
            rpde = float(request.POST.get('rpde'))
            dfa = float(request.POST.get('dfa'))
            spread1 = float(request.POST.get('spread1'))
            spread2 = float(request.POST.get('spread2'))
            d2 = float(request.POST.get('d2'))
            ppe = float(request.POST.get('ppe'))
        except (TypeError, ValueError):
            return render(request, "parkinson.html", {'error': 'Invalid input!'})

        path = os.path.dirname(__file__)
        model_path = os.path.join(path, 'parkinsons.pkl')

        with open(model_path, 'rb') as f:
            model = pickle.load(f)
        res = int(model.predict([[fo, fhi, flo, jitter_percent, jitter_abs, rap, ppq, ddp, shimmer, shimmer_db, apq3, apq5, apq, dda, nhr, hnr, rpde, dfa, spread1, spread2, d2, ppe]])[0])

        return render(request, "parkinson.html", {'res': res})

    return render(request, "parkinson.html")
