from django.conf import settings
from django.core.paginator import Paginator


def make_paginator(request, list):
    paginator = Paginator(list, settings.FILES_COUNT)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj
