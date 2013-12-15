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
import os
from unittest import TestCase

from fms.server.parsers.lastfm import search_artist_parser


class TestSearchArtist(TestCase):
    def test_call_main_func(self):
        work_f = os.getcwd()
        file_path = os.path.join(work_f, "files", "search_artist_response.txt")
        with open(file_path) as f:
            html = f.read()
            search_artist_parser.parse(html)