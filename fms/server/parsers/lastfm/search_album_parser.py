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
import bs4
import logging

from fms.server.models.last_fm_models import SearchAlbum


LOG = logging.getLogger(__name__)


def parse(html):
    soup = bs4.BeautifulSoup(html)
    album_blocks = soup.find_all("div", {"class": "resContainer"})
    if album_blocks is None:
        return []

    albums = parse_albums(album_blocks)
    return albums


def parse_albums(blocks):
    albums = []
    for b in blocks:
        try:
            albums.append(parse_one(b))
        except BaseException as e:
            LOG.debug("Exception during parsing search artist %s" % e)
    return albums


def parse_one(node):
    album = SearchAlbum()
    summary_block = node.find("a", {"class": "summary"})
    if summary_block is not None:
        if hasattr(summary_block, "attrs") and "href" in summary_block.attrs:
            album.url = summary_block.attrs["href"]
        album.name = summary_block.text

    artist_block = node.find("a", {"class": "artist"})
    if artist_block is not None:
        album.artist = artist_block.text


    return album