from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    # TODO: Define other fields here

    class Meta:
        model = Post
        fields = ('author', 'title', 'text',)

        widgets = {
            'title':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})
        }




class CommentForm(forms.ModelForm):
    # TODO: Define other fields here

    class Meta:
        model = Comment
        fields = ('author', 'text',)

        widgets = {
            'author':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'})
        }
