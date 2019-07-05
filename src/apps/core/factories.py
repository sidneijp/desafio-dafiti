import factory
import factory.fuzzy

from apps.core.models import Shoe


class ShoeFactory(factory.django.DjangoModelFactory):
    sku = factory.Sequence(lambda n: f'SKU-{n}')
    name = factory.Faker('name')
    color = factory.fuzzy.FuzzyChoice(Shoe.COLOR_CHOICES, getter=lambda x: x[0])
    stock = factory.fuzzy.FuzzyInteger(low=0, high=999, step=1)
    price = factory.fuzzy.FuzzyDecimal(low=0, high=999, precision=2)

    class Meta:
        model = Shoe

