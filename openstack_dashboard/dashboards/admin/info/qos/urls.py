# vim: tabstop=4 shiftwidth=4 softtabstop=4

#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
#
# Copyright (c) 2013-2017 Wind River Systems, Inc.
#


from django.conf.urls import url  # noqa

from openstack_dashboard.dashboards.admin.info.qos import views

QOS = r'^(?P<qos_id>[^/]+)/%s$'

urlpatterns = [
    url(r'^create/$', views.CreateView.as_view(), name='create'),
    url(QOS % 'update', views.UpdateView.as_view(), name='update'),
    url(QOS % 'detail', views.DetailView.as_view(), name='detail'),
    url(QOS % 'create',views.CreateRuleView.as_view(),name='create_rule'),
    url(QOS % 'delete', views.DeleteView.as_view(), name='delete'),
]
