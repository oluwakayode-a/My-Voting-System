from django import forms
from django.http import Http404, HttpRequest


from .models import Aspirant, Position


class AddAspirant(forms.ModelForm):
    class Meta:
        model = Aspirant
        fields = ['name', 'post']


class VotingForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        # print(self.request.path)
        super(VotingForm, self).__init__(*args, **kwargs)
        self.fields['aspirants'].choices = self.get_url()

    def get_url(self):
        self._ = []
        for post in Position.objects.all():
            if self.request.get_full_path() == "/vote/pro":
                no_ = Position.objects.get(post='PRO')
                self._.clear()
                for i in Aspirant.objects.filter(post=no_):
                    self._.append(tuple([i.name, i.name]))
            elif self.request.get_full_path() == "/vote/gen-sec":
                no_ = Position.objects.get(post='General Secretary')
                self._.clear()
                for i in Aspirant.objects.filter(post=no_):
                    self._.append(tuple([i.name, i.name]))
            elif self.request.get_full_path() == "/vote/vp-admin":
                no_ = Position.objects.get(post='Vice President (Admin)')
                self._.clear()
                for i in Aspirant.objects.filter(post=no_):
                    self._.append(tuple([i.name, i.name]))
            elif self.request.get_full_path() == "/vote/vp-editorial":
                no_ = Position.objects.get(post='Vice President (Editorial)')
                self._.clear()
                for i in Aspirant.objects.filter(post=no_):
                    self._.append(tuple([i.name, i.name]))
            elif self.request.get_full_path() == "/vote/president":
                no_ = Position.objects.get(post='President')
                self._.clear()
                for i in Aspirant.objects.filter(post=no_):
                    self._.append(tuple([i.name, i.name]))

        return self._
    
    CHOICES = []

    aspirants = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)

    class Meta:
        model = Aspirant
        fields = ['aspirants']
