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
from bs4 import BeautifulSoup
import logging

from fms.server.models.last_fm_models import SearchArtist
from fms.server.parsers.lastfm import pagination_utils


LOG = logging.getLogger(__name__)


def parse(html):
    soup = BeautifulSoup(html)

    artists_block = soup.find("ul", {"class": "artistsWithInfo"})
    if artists_block is None:
        return []

    artists = artists_block.find_all("li")
    result = parse_artists(artists)
    return result


def parse_artists(artists):
    artists_array = []
    for art_data in artists:
        try:
            artists_array.append(parse_one(art_data))
        except BaseException as e:
            LOG.debug("Exception during parsing search artist %s" % e)

    return artists_array


def parse_one(node):
    artist_model = SearchArtist()

    #getting url and image
    summary_block = node.find("a", {"class": "artist"})
    artist_model.name = summary_block.text
    if hasattr(summary_block, "href") and "href" in summary_block.attrs:
        artist_model.url = summary_block.attrs["href"]

    #getting brief description
    bio_block = node.find("p", {"class": "bio"})
    artist_model.descr = bio_block.text.strip()

    #getting url on image
    image_block = node.find("img")
    if hasattr(image_block, "attrs") and "src" in image_block.attrs:
        artist_model.image = image_block.attrs["src"]

    return artist_model