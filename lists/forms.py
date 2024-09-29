from django import forms
from . models import TaskView
from jalali_date.fields import JalaliDateField,SplitJalaliDateTimeField
from jalali_date.widgets import AdminJalaliDateWidget,AdminSplitJalaliDateTime



class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskView
        fields = "__all__"
        

        labels = {
            "name":"Your Name",
            "description":"Your description",
            "deadline":"Your deadline"
        }
        error_messages = {
            "name":{
            "description":"NOP",
            "deadline":"Invalid"
        }}

    def __init__(self, *args, **kwargs):
        super(TaskForm,self).__init__(*args, **kwargs)
        self.fields["deadline"] = SplitJalaliDateTimeField(label=("deadline"), widget=AdminSplitJalaliDateTime)
    
