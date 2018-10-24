# Copyright 2017 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""WSGIApplication definition for Upvote's web-facing API."""

import webapp2

from webapp2_extras import routes

from upvote.gae.modules.upvote_app.api.web import alerts
from upvote.gae.modules.upvote_app.api.web import blockables
from upvote.gae.modules.upvote_app.api.web import constants
from upvote.gae.modules.upvote_app.api.web import emergency
from upvote.gae.modules.upvote_app.api.web import events
from upvote.gae.modules.upvote_app.api.web import hosts
from upvote.gae.modules.upvote_app.api.web import index_handler
from upvote.gae.modules.upvote_app.api.web import lookups
from upvote.gae.modules.upvote_app.api.web import rules
from upvote.gae.modules.upvote_app.api.web import settings
from upvote.gae.modules.upvote_app.api.web import users
from upvote.gae.modules.upvote_app.api.web import votes
from upvote.gae.utils import handler_utils

_ALL_ROUTES = [

    # Warmup
    webapp2.Route('/_ah/warmup', handler=handler_utils.AckHandler),

    # API handlers
    routes.PathPrefixRoute(
        '/api/web',
        [
            webapp2.Route('/ack', handler=handler_utils.AckHandler),
            alerts.ROUTES,
            blockables.ROUTES,
            constants.ROUTES,
            emergency.ROUTES,
            events.ROUTES,
            hosts.ROUTES,
            lookups.ROUTES,
            rules.ROUTES,
            settings.ROUTES,
            users.ROUTES,
            votes.ROUTES
        ]),

    # Index handler
    webapp2.Route(
        r'/admin<:/?><:.*>',
        handler=index_handler.IndexHandler,
        handler_method='GetAdmin',
        methods=['GET']),
    webapp2.Route(
        r'/<:/?><:.*>',
        handler=index_handler.IndexHandler,
        handler_method='GetUser',
        methods=['GET']),
]

app = webapp2.WSGIApplication(routes=_ALL_ROUTES)
handler_utils.CreateErrorHandlersForApplications([app])