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

    username = factory.Sequence(lambda n: 'user{0}'.format(n))
    email = factory.LazyAttribute(lambda obj: '{0}@sockemboppem.com'.format(obj.username))
    password = factory.LazyAttribute(lambda obj: '{0}'.format(obj.username))
