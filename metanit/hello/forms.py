from django import forms


class UserForm(forms.Form):
    name = forms.CharField(label='Name', initial='undefined', help_text='write name')
    age = forms.IntegerField(label='age', initial=18, step_size=10, help_text='write age')
    comment = forms.CharField(label='comma', widget=forms.Textarea)
    field_order = ['age', 'name']
