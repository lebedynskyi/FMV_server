# coding=utf-8
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


from mock import Mock
from unittest import TestCase

from fms.server.utils import http_utils


class TestNetwork(TestCase):
    def test_do_get(self):
        pass

    def test_generate_url(self):
        base_url = "http://mega.co.hz"
        params = {"first": 1, "second": "2"}
        expected_url = "http://mega.co.hz?second=2&first=1"
        new_url = http_utils.generate_url(base_url, params)
        self.assertEquals(new_url, expected_url)

    def test_generate_url_with_none(self):
        base_url = "http://test.test.com"
        expected = base_url
        self.assertEquals(http_utils.generate_url(base_url, None), expected)

    def test__url_fix(self):
        latinos_words = "hello world"
        cyrillic_worlds = "привет мир"

        expected_latic = "hello%20world"
        expected_cyrillic = \
            "%D0%BF%D1%80%D0%B8%D0%B2%D0%B5%D1%82%20%D0%BC%D0%B8%D1%80"
        self.assertEquals(http_utils.url_fix(latinos_words), expected_latic)
        self.assertEquals(http_utils.url_fix(cyrillic_worlds),
                          expected_cyrillic)