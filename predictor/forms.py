from django import forms

class HeartRiskForm(forms.Form):
    age = forms.FloatField(label="Yaş")
    dizziness = forms.BooleanField(label="Baş Dönmesi", required=False)
    cold_sweats_nausea = forms.BooleanField(label="Soğuk Terleme / Mide Bulantısı", required=False)
    palpitations = forms.BooleanField(label="Çarpıntı", required=False)
    shortness_of_breath = forms.BooleanField(label="Nefes Darlığı", required=False)
    fatigue = forms.BooleanField(label="Yorgunluk", required=False)
    swelling = forms.BooleanField(label="Şişme", required=False)
    pain_arms_jaw_back = forms.BooleanField(label="Kol / Çene / Sırt Ağrısı", required=False)
    chest_pain = forms.BooleanField(label="Göğüs Ağrısı", required=False)