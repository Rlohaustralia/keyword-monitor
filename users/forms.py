from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
    confirm_password = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
    
    def clean(self):
         cleaned_data = super().clean()
         password = cleaned_data.get('password')
         confirm_password = cleaned_data.get('confirm_password')

         if password and confirm_password and password != confirm_password:
              raise ValidationError("Passwords do not match.")
         return cleaned_data

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise ValidationError("Password must be at least 8 character long.")
        return password 
    
    def save(self, commit=True):
        user = super().save(commit=False) # DB에 저장하지 않고 User 객체 생성
        user.set_password(self.cleaned_data['password']) # set_password 비밀번호 해싱하여 저장   
        if commit:
            user.save() # 최종적으로 DB에 저장
        return user
