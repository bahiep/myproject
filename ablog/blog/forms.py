from .models import Comment
from django import forms
from mptt.forms import TreeNodeChoiceField

class CommentForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     self.author = kwargs.pop('author', None)
    #     self.post = kwargs.pop('post', None)
    #     form = super().__init__(*args, **kwargs)
        
    # def save(self, commit=True):
    #     comment=super().save(commit=False)
    #     comment.author=self.author
    #     comment.post = self.post
    #     comment.save()
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)

    #     self.fields['parent'].widget.attrs.update(
    #         {'class': 'd-none'})
    #     self.fields['parent'].label = ''
    #     self.fields['parent'].required = False
    parent = TreeNodeChoiceField(queryset=Comment.objects.all())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['parent'].widget.attrs.update(
            {'class': 'd-none'})
        self.fields['parent'].label = ''
        self.fields['parent'].required = False
    class Meta:
        model = Comment
        fields = ["body","parent"] 
        widgets={          
            'body':forms.Textarea(attrs={'class':'form-control form-control-sm', 'rows':'3'}),
        }