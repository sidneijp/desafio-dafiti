from django.core.exceptions import ValidationError, FieldDoesNotExist
from django.core.validators import MinValueValidator
from django.db import models
from django.db import IntegrityError, transaction
from django.utils.translation import gettext_lazy as _


class Shoe(models.Model):
    sku = models.CharField(_('SKU'), max_length=32, unique=True)
    name = models.CharField(_('Name'), max_length=255)

    COLOR_DEFAULT = COLOR_RED = 'r'
    COLOR_GREEN = 'g'
    COLOR_BLUE = 'b'
    COLOR_CHOICES = (
        (COLOR_RED, _('Red')),
        (COLOR_GREEN, _('Green')),
        (COLOR_BLUE, _('Blue')),
    )
    color = models.CharField(
        _('Color'), max_length=1,
        choices=COLOR_CHOICES, default=COLOR_DEFAULT,
    )

    stock = models.IntegerField(
        _('Stock amount'), validators=[MinValueValidator(0)],
    )
    price = models.DecimalField(
        _('Price'), decimal_places=2, max_digits=10,
        validators=[MinValueValidator(0)],
    )

    class Meta:
        verbose_name = _('Shoe')
        verbose_name_plural = _('Shoes')

    def __str__(self):
        return f'{self.name}'

    def unit_price_for(self, total_stock_price):
        try:
            return total_stock_price / self.stock
        except (ZeroDivisionError, TypeError):
            raise ValueError(_(f"Can't calculate unit price for 'stock': {self.stock}"))
