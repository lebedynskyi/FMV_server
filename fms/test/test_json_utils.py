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


from unittest import TestCase

from fms.server.utils import json_utils


class TestJson(TestCase):
    def test_exception(self):
        exception = ValueError("test")
        expected = '{"resp": "test"}'
        self.assertEqual(json_utils.to_json("resp", exception), expected)

    def test_dict(self):
        pass

    def test_none(self):
        pass

    def test_other(self):
        pass

    def test_json_serializable(self):
        class JsonClass(json_utils.JsonSerializable):
            pass

        obj = JsonClass()
        json_utils.to_json("k", obj)

