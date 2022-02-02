from django.forms import ModelForm
from .models import Task

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import datetime


class RenewTaskForm(ModelForm): 
    def clean_must_do(self):
        data = self.cleaned_data['must_do']

       #Проверка того, что дата не в прошлом
        if data < datetime.date.today():
           raise ValidationError(_('Invalid date - renewal in past'))

       #Check date is in range librarian allowed to change (+4 weeks)
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
           raise ValidationError(_('Invalid date - renewal more than 4 weeks ahead'))

       # Не забывайте всегда возвращать очищенные данные
        return data

    class Meta:
        model = Task
        fields = ['must_do',]
        labels = { 'must_do': _('Renewal date'), }
        help_texts = { 'must_do': _('Укажите дату от сейчас и до 4 недель вперед.'), }
