# vim: tabstop=4 shiftwidth=4 softtabstop=4

# copyright [2013] [Vitalii Lebedynskyi]
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from fms.server.exceptions import RequiredValueException
from fms.server.parsers.lastfm import search_artist_parser
from fms.server.parsers.lastfm import search_album_parser
from fms.server.parsers.pleerdotcom import search_song_parser
from fms.server.utils import http_utils


LAST_FM_SEARCH = "http://last.fm/search"
PLEER_DOT_COM_URL = "http://pleer.com/browser-extension/search"


class BaseHandler(object):
    def __init__(self, manager):
        self.manager = manager
        self.url = None
        self.parser = None
        self.additional_params = {}
        self.required_params = []

    def handle(self, args):
        params = self.extract_params_from_req(args)
        self.check_required_params(params)
        params.update(self.additional_params)
        return self._handle_request(params)

    def extract_params_from_req(self, args):
        received_args = {}
        if args is None or len(args) == 0:
            return received_args

        for k in args.keys():
            received_args[k] = args.get(k)

        return received_args

    def check_required_params(self, params):
        for p in self.required_params:
            if p not in params:
                raise RequiredValueException(p)

    def _handle_request(self, params):
        if not self.url or self.parser is None:
            raise RuntimeError("url or parser cannot be None")

        html = http_utils.do_get(self.url, params)
        if not html:
            raise RuntimeError("Unknown server error")

        result = self.parser.parse(html)
        return result


class SearchArtistHandler(BaseHandler):
    def __init__(self, manager):
        super(SearchArtistHandler, self).__init__(manager)
        self.url = LAST_FM_SEARCH
        self.parser = search_artist_parser
        self.additional_params.update({u"type": u"artist"})
        self.required_params.append(u"q")


class SearchAlbumsHandler(BaseHandler):
    def __init__(self, manager):
        super(SearchAlbumsHandler, self).__init__(manager)
        self.url = LAST_FM_SEARCH
        self.parser = search_album_parser
        self.additional_params.update({u"type": u"album"})
        self.required_params.append(u"q")


class SearchSongsHandler(BaseHandler):
    def __init__(self, manager):
        super(SearchSongsHandler, self).__init__(manager)
        self.url = PLEER_DOT_COM_URL
        self.parser = search_song_parser
        self.additional_params.update({u"limit": u"20"})
        self.required_params.append(u"q")
