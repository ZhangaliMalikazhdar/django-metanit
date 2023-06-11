from .models import Person
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned


try:
    tom = Person.objects.get(name='Tom')
    alex = Person.objects.get(name='Akame')
except ObjectDoesNotExist:
    print('obj dsnt exst')
except MultipleObjectsReturned:
    print('on mor obj in sme')
