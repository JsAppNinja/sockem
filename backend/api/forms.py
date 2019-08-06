""""
Contains forms used by the API app
"""
from django import forms
from .models import Match
from .util import validate_prev_matches


class MatchForm(forms.ModelForm):
    """
    Used for the Match model in the Admin page
    """
    class Meta:
        model = Match
        fields = '__all__'

    def clean(self):
        """
        Checks that all the prev_matches are valid and form a tree based on 'round'.
        """
        prev_matches = self.cleaned_data.get('prev_matches')
        current_round = self.cleaned_data.get('round')
        if prev_matches:
            validate_prev_matches(self, prev_matches, current_round)
        return self.cleaned_data
