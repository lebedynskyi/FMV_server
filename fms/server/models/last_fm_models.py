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

from fms.server.utils import json_utils


class SearchArtist(json_utils.JsonSerializable):
    def __init__(self):
        self.url = None
        self.name = None
        self.image = None
        self.descr = None

    def get_values_keys(self):
        return ["url", "name", "image", "descr"]


class SearchAlbum(json_utils.JsonSerializable):
    def __init__(self):
        self.url = None
        self.name = None
        self.artist = None
        self.descr = None

    def get_values_keys(self):
        return ["url", "name", "artist", "descr"]