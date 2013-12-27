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
import time

from flask import Flask
from flask import request
from flask import make_response

from fms.server import handlers
from fms.server.utils import json_utils
from fms.server.utils import log_utils
from fms.server.exceptions import BaseFMSException, InnerServerError


log_utils.init_logger("*")
LOG = logging.getLogger()
app = Flask(__name__)


@app.route("/test")
def test():
    LOG.debug("TEST PAGE called")
    LOG.info("TEST PAGE called")
    LOG.warning("TEST PAGE called")
    LOG.error("TEST PAGE called")
    LOG.critical("TEST PAGE called")
    return "TEST PAGE"


@app.route("/artists.search")
def search_artist():
    return _safe_handle(handlers.SearchArtistHandler(None), request.args)


@app.route("/albums.search")
def search_albums():
    return _safe_handle(handlers.SearchAlbumsHandler(None), request.args)


@app.route("/songs.search")
def search_songs():
    return _safe_handle(handlers.SearchSongsHandler(None), request.args)


def _safe_handle(handler, args):
    try:
        start_time = time.time()
        rez = handler.handle(args)
        json_response = json_utils.to_json("response", rez)

        request_time = time.time() - start_time

        response = make_response(json_response)
        response.headers['Request-time'] = str(request_time)

        return response
    except BaseException as e:
        if not isinstance(e, BaseFMSException):
            LOG.exception(e)
        return json_utils.to_json("error", InnerServerError(e.message))


if __name__ == "__main__":
    app.run("0.0.0.0", port=6985)