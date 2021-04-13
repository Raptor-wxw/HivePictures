from random import randint

import One
from One.models import Pic, Pics


def images():
    i = 1
    context = {}
    while i <= 13:
        package = str(randint(60000, 63436))
        try:
            url = Pic.objects.filter(available=1).get(package=package)
            context['photo' + str(i)] = url.first_pic
            context['text' + str(i)] = url.text
            context['package'+str(i)] = package
            i += 1
        except One.models.Pic.DoesNotExist:
            continue
        except One.models.Pic.MultipleObjectsReturned:
            continue
    return context


def show():
    i = 1
    context = {}
    while i <= 8:
        package = str(randint(60000, 64436))
        try:
            url = Pic.objects.get(package=package)
            context['photo' + str(i)] = url.first_pic
            context['text' + str(i)] = url.text
            get_package(package)
            i += 1
        except One.models.Pic.DoesNotExist:
            continue
        except One.models.Pic.MultipleObjectsReturned:
            continue
    return context


def get_package(pac):
    pics = Pics.objects.filter(package=pac)
    return pics


def search(condition):
    result = Pic.objects.filter(text__contains=condition)
    return result
