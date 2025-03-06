from django.shortcuts import render
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model  # type: ignore
from .forms import HeartRiskForm

# Modeli yükleyin (Bunu sadece bir kere yüklemek için global olarak tutabilirsiniz)
model_path = "heart_risk_model.h5"  # Model dosyanızın ismi
model = load_model(model_path)

def predict_risk(request):
    prediction = None
    if request.method == "POST":
        form = HeartRiskForm(request.POST)
        if form.is_valid():
            # Kullanıcı verilerini numpy array olarak al
            user_input = np.array([[
                form.cleaned_data['age'],
                int(form.cleaned_data['dizziness']),
                int(form.cleaned_data['cold_sweats_nausea']),
                int(form.cleaned_data['palpitations']),
                int(form.cleaned_data['shortness_of_breath']),
                int(form.cleaned_data['fatigue']),
                int(form.cleaned_data['swelling']),
                int(form.cleaned_data['pain_arms_jaw_back']),
                int(form.cleaned_data['chest_pain'])
            ]])

            # Modelden tahmin al
            if model:
                prediction = model.predict(user_input)[0][0]
                prediction = "Riskli" if prediction > 0.5 else "Sağlıklı"
            else:
                prediction = "Model yüklenemedi"

    else:
        form = HeartRiskForm()

    return render(request, "predictor/form.html", {"form": form, "prediction": prediction})
