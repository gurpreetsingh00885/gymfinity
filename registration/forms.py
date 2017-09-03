from django import forms
from registration.models import Gym
from mapwidgets.widgets import GooglePointFieldWidget

class AddGymForm(forms.ModelForm):

    class Meta:
        model = Gym
        fields = ("name", "contact_no" ,"location",)
        widgets = {
            'location': GooglePointFieldWidget,
        }

    def __init__(self, *args, **kwargs):
        super(AddGymForm, self).__init__(*args, **kwargs)

        self.fields["name"].widget.attrs['placeholder'] = "Gym's Name"
        self.fields["contact_no"].widget.attrs['placeholder'] = "Contact No."

class FindGymForm(forms.ModelForm):

    class Meta:
        model = Gym
        fields = ("location",)
        widgets = {
            'location': GooglePointFieldWidget,
        }

    def __init__(self, *args, **kwargs):
    	super(FindGymForm, self).__init__(*args, **kwargs)
    	self.fields["max_distance"] = forms.IntegerField(required=True)
