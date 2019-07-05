from django.contrib.auth import get_user_model
import factory


class UserFactory(factory.django.DjangoModelFactory):
    username = factory.Faker('name')

    class Meta:
        model = get_user_model()

