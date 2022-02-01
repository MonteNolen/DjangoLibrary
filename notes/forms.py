from django import forms

class RenewNoteForm(forms.Form):
    renewal_date = forms.DateField(help_text="Какой-то текст")
    