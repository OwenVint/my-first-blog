from django import forms

from .models import Post, Profile, Profile_CV

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class ProfileForm(forms.ModelForm):

	class Meta:
		model = Profile_CV
		fields = ('name', 'overview','personal_details','experience','education','skills','interests','references' )
	