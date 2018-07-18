from django import forms

class PostForm(forms.Form):
    eki1 = forms.CharField()
    eki2 = forms.CharField()
    time1 = forms.CharField()
    time2 = forms.CharField()
    flag = forms.IntegerField()
