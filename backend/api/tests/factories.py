"""
Factories used for testing models
"""
import factory
from ..models import User


class UserFactory(factory.django.DjangoModelFactory):
    """
    Factory for User models
    """
    class Meta:
        model = User

    email = factory.Sequence(lambda n: 'user{0}@sockemboppem.com'.format(n))
