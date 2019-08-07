"""
Contains misc and util functions used by multiple files in the app
"""
from django.core.exceptions import ValidationError


def validate_parent(self, parent, current_round):
    """
    Checks to see if a Match object being saved has valid 'prev_matches' fields
    Currently checks to see if the 'round' fields in 'prev_matches' are all lower
    than the 'round' in the request's body

    Used in:
        serializers.MatchSerializer.validate
        forms.MatchForm.clean

    :param self:
    :param parent: a parent match
    :param current_round: integer value that is guaranteed to be >= 1
    :return: Raises a ValidationError if field is invalid
    """

    if parent.round <= current_round:
        raise ValidationError(
            "The match '{0}' has a round of '{1}' "
            "which is less than or equal to "
            "the current round of '{2}'".format(parent, parent.round, current_round))