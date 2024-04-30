from django import forms


class GameForm(forms.Form):
    choice = forms.ChoiceField(choices=[('C', 'Монетка'), ('K', 'Кубик'),('N', 'Случайные числа')])
    count = forms.IntegerField(max_value=64, min_value=1)
