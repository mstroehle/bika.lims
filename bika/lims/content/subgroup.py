# -*- coding: utf-8 -*-
#
# This file is part of Bika LIMS
#
# Copyright 2011-2017 by it's authors.
# Some rights reserved. See LICENSE.txt, AUTHORS.txt.

from AccessControl import ClassSecurityInfo
from bika.lims import bikaMessageFactory as _
from bika.lims.utils import t
from bika.lims.config import PROJECTNAME
from bika.lims.interfaces import ISubGroup
from bika.lims.content.bikaschema import BikaSchema
from bika.lims.fields import *
from Products.Archetypes.public import *
from zope.interface import implements

schema = BikaSchema.copy() + Schema((
    ExtStringField(
        'SortKey',
        widget=StringWidget(
            label=_("Sort Key"),
            description=_("Subgroups are sorted with this key in group views")
        )
    ),
))
schema['description'].widget.visible = True
schema['description'].schemata = 'default'


class SubGroup(BaseContent):
    implements(ISubGroup)
    security = ClassSecurityInfo()
    displayContentsTab = False
    schema = schema

    _at_rename_after_creation = True

    def _renameAfterCreation(self, check_auto_id=False):
        from bika.lims.idserver import renameAfterCreation
        renameAfterCreation(self)

registerType(SubGroup, PROJECTNAME)
