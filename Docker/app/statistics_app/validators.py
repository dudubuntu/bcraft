from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def positive_value_validation(value: float):
    """Валидация на позитивное число для модели Statistics"""
    if not value >= 0:
        raise ValidationError(
            _('%(value)s is negative.'),
            params={'value': value},
        )