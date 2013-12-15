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

from fms.server.utils import decorators


class TestDecorators(TestCase):
    def setUp(self):
        super(TestDecorators, self).setUp()

        @decorators.none_values
        class TestClass(object):
            pass

        self.object = TestClass()
        self.value = "value"

    def test_existed_value(self):
        self.object.value = "value"
        self.assertEqual(self.object.value, "value")

    def test_nont_existed_value(self):
        self.assertEqual(self.object.non, None)