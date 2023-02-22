from django import forms


class emp(forms.Form):
    id=forms.IntegerField()
    name=forms.CharField(max_length=50)
    sal=forms.IntegerField()
    job=forms.CharField(max_length=50)
    