from django import forms # type: ignore

from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(
        required=False,
        widget=forms.Textarea
    )

class SearchForm(forms.Form):
    query = forms.CharField()


class ContactUsForm(forms.Form):
    first_name = forms.CharField(max_length=25, label='First Name')
    last_name = forms.CharField(max_length=25, label='Last Name')
    email = forms.EmailField()
    
    message = forms.CharField(
        required=False,
        widget=forms.Textarea,
        label='Message'
    )




# in progress:
class CommentEditForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body', 'active']
        widgets = {
            'body': forms.Textarea(attrs={'rows': 5}),
        }

    def clean_email(self):
        data = self.cleaned_data['email']
        return data
       