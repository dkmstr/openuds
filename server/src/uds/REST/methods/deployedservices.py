# -*- coding: utf-8 -*-

#
# Copyright (c) 2014 Virtual Cable S.L.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification, 
# are permitted provided that the following conditions are met:
#
#    * Redistributions of source code must retain the above copyright notice, 
#      this list of conditions and the following disclaimer.
#    * Redistributions in binary form must reproduce the above copyright notice, 
#      this list of conditions and the following disclaimer in the documentation 
#      and/or other materials provided with the distribution.
#    * Neither the name of Virtual Cable S.L. nor the names of its contributors 
#      may be used to endorse or promote products derived from this software 
#      without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE 
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE 
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE 
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR 
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER 
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, 
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE 
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

'''
@author: Adolfo Gómez, dkmaster at dkmon dot com
'''
from __future__ import unicode_literals

from django.utils.translation import ugettext as _


from uds.models import DeployedService, Service

from uds.core.util import log
from uds.core.Environment import Environment
from uds.REST.model import ModelHandler
from uds.REST import NotFound, ResponseError, RequestError
from django.db import IntegrityError

import logging

logger = logging.getLogger(__name__)


class DeployedServices(ModelHandler):
    model = DeployedService
    save_fields = ['name', 'comments', 'service', 'osmanager', 'initial_srvs', 'cache_l1_srvs', 'cache_l2_srvs', 'max_srvs']

    table_title =  _('Deployed services')
    table_fields = [
            { 'name': {'title': _('Name'), 'visible': True, 'type': 'iconType' } },
            { 'comments': {'title':  _('Comments')}},
    ]
    
    def item_as_dict(self, item):
        type_ = item.getType()
        return { 'id': item.id,
                 'name': item.name, 
                 'comments': item.comments,
        }
        
    # Gui related
    def getGui(self, type_):
        try:
            return self.addDefaultFields(['name', 'comments'])
        except:
            raise NotFound('type not found')
