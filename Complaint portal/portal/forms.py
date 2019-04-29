from .models import *


from django import forms


class Complaint_form(forms.ModelForm):

    class Meta:
        model = Complaint
        fields = ['title','tag','content',]


class Comment_form(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['comment']