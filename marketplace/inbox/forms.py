from django import forms

from .models import InboxMessage

class InboxMessageForm(forms.ModelForm):
    class Meta:
        model = InboxMessage
        fields = ('content',)
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'w-full py-4 px-2 border rounded'
            })
        }