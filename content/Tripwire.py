# -*- coding: utf-8 -*-
#
# File: Tripwire.py
#
# Copyright (c) 2008 by []
# Generator: ArchGenXML Version 2.1
#            http://plone.org/products/archgenxml
#
# GNU General Public License (GPL)
#

__author__ = """unknown <unknown>"""
__docformat__ = 'plaintext'

from AccessControl import ClassSecurityInfo
from Products.Archetypes.atapi import *
from zope.interface import implements
import interfaces

from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin

from Products.Tripwire.config import *

# additional imports from tagged value 'import'
from Products.ATContentTypes.content.link import ATLink

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    BooleanField(
        name='active',
        default="True",
        widget=BooleanField._properties['widget'](
            label='Active',
            label_msgid='Tripwire_label_active',
            i18n_domain='Tripwire',
        ),
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

Tripwire_schema = BaseSchema.copy() + \
    getattr(ATLink, 'schema', Schema(())).copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class Tripwire(BaseContent, ATLink, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.ITripwire)

    meta_type = 'Tripwire'
    _at_rename_after_creation = True

    schema = Tripwire_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods


registerType(Tripwire, PROJECTNAME)
# end of class Tripwire

##code-section module-footer #fill in your manual code here
##/code-section module-footer



