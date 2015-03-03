# -*- coding: utf-8 -*-

import grok
import megrok.pagetemplate as pt

from . import templates_dir
from .layout import ILayer
from dolmen.forms.base import ApplicationForm
from uvc.layout.forms.components import Wizard
from uvcsite.homefolder import views
from zeam.form.layout import Form



grok.templatedir(templates_dir)


class Index(views.Index):
    grok.layer(ILayer)

    cssClasses = {'table': 'table table-hover'}


class WizardTemplate(pt.PageTemplate):
    grok.layer(ILayer)
    pt.view(Wizard)
