import grok
import megrok.pagetemplate as pt


from .layout import ILayer
from . import templates_dir
from uvc.api.api import get_template
from dolmen.forms.base import ApplicationForm


class FormTemplate(pt.PageTemplate):
    grok.layer(ILayer)
    grok.view(ApplicationForm)
    template = get_template(templates_dir, 'form.cpt')
    
