# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from coffin.views.generic import TemplateView
from django.utils.translation import ugettext_lazy as _


class HomePage(TemplateView):
    template_name = 'home.html'