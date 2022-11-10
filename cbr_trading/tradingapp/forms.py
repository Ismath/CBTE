from django import forms
from rest_framework.exceptions import ValidationError

from .models import t_user



class MyForm(forms.ModelForm):
    class Meta:
        model = t_user


        fields = ["username", "secret","email","full_name","nic","address","telephone", "type","verified","creation_date","modification_date"]
        labels = {'username': "username",'secret':"Password",'full_name':"Full Name",'email':"Email",'nic':"NIC Number",'address':"Address",'telephone': "Mobile Number",'type':"Type",'verified':"Verified",'creation_date':"Creation Date",'modification_date':"Modification Date" }

    #def clean_email(self):
     #   email = self.cleaned_data["email"]
      #  if t_user.objects.filter(email=email).exists():
      #      raise ValidationError("An user with this email already exists!")
      #  return email


