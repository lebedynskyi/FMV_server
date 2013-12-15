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
import logging

from flask import Flask
from flask import request

from fms.server import handlers
from fms.server.utils import json_utils
from fms.server.utils import log_utils
from fms.server.exceptions import BaseFMSException, InnerServerError


class WrappedFlask(Flask):
    def run(self, host=None, port=None, debug=None, **options):
        super(WrappedFlask, self).run(host, port, debug, **options)

        log_utils.init_logger("*")
        LOG.warning("Logger configured")


LOG = logging.getLogger()
app = WrappedFlask(__name__)


@app.route("/test")
def test():
    return "TEST PAGE"


@app.route("/artists.search")
def search_artist():
    return safe_handle(handlers.SearchArtistHandler(None), request.args)


@app.route("/albums.search")
def search_albums():
    return safe_handle(handlers.SearchAlbumsHandler(None), request.args)


@app.route("/songs.search")
def search_songs():
    return safe_handle(handlers.SearchSongsHandler(None), request.args)


def safe_handle(handler, args):
    try:
        rez = handler.handle(args)
        return json_utils.to_json("response", rez)
    except BaseException as e:
        if not isinstance(e, BaseFMSException):
            LOG.exception(e)
        return json_utils.to_json("error", InnerServerError(e.message))


def start():
    pass