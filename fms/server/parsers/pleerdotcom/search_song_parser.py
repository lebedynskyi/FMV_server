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
import json
import logging

from fms.server.models.pleer_dot_com_models import SearchSong


LOG = logging.getLogger(__name__)


def parse(json_response):
    data = json.loads(json_response)
    data.pop("playlists", None)
    songs_count = data.pop("found", None)
    songs_json = data.pop("tracks", None)
    songs = parse_songs(songs_json)
    return songs


def parse_songs(songs_json):
    songs = []
    for j in songs_json:
        songs.append(parse_one(j))
    return songs


def parse_one(jsonSong):
    song = SearchSong()

    song.name = jsonSong["track"]
    song.artist = jsonSong["artist"]
    song.id = jsonSong["id"]
    song.url = jsonSong["file"]
    song.bitrate = jsonSong["bitrate"]
    song.size = jsonSong["size"]
    song.length = jsonSong["length"]
    return song


