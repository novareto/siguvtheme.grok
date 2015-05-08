# -*- coding: utf-8 -*-

import os
import grok

from . import templates_dir
#from .resources import tune
from uvc.tbskin.skin import ITBSkin, Layout
from uvc.api.api import get_template


class ILayer(grok.IDefaultBrowserLayer):
    pass


class ISkin(ILayer, ITBSkin):
    grok.skin('siguvtheme')


class MasterLayout(Layout):
    grok.name("")
    grok.layer(ILayer)
    template = get_template('masterlayout', templates_dir)

    def update(self):
        #tune.need()
        Layout.update(self)
