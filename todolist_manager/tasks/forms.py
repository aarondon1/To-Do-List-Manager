from django import forms

# Form for adding tasks
class TaskForm(forms.Form):
    title = forms.CharField(max_length=200)
    description = forms.CharField(widget=forms.Textarea, required=False)
    priority = forms.IntegerField(min_value=1, max_value=10)