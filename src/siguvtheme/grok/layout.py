# -*- coding: utf-8 -*-

import os
import grok

from . import templates_dir
from .resources import tune
from uvc.tbskin.skin import ITBSkin, Layout


grok.templatedir(templates_dir)


class ILayer(grok.IDefaultBrowserLayer):
    pass


class ISkin(ILayer, ITBSkin):
    grok.skin('siguvtheme')


class MasterLayout(Layout):
    grok.name("")
    grok.layer(ILayer)

    def update(self):
        tune.need()
        Layout.update(self)
