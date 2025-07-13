from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Review

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.role = 'regular'  # Default role for new users
        if commit:
            user.save()
        return user

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('rating', 'comment')
        widgets = {
            'rating': forms.Select(choices=[
                (5, '5 - Excellent'),
                (4, '4 - Very Good'),
                (3, '3 - Good'),
                (2, '2 - Fair'),
                (1, '1 - Poor'),
            ], attrs={'class': 'form-select'}),
            'comment': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Share your experience with this product...'
            })
        }
