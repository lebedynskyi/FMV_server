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
from setuptools import find_packages, setup
from pip.req import parse_requirements


def get_requirements():
    install_reqs = parse_requirements("requirements.txt")
    reqs = [str(ir.req) for ir in install_reqs]
    return reqs

setup(name="FMS server",
      version="1.0",
      author="Vitalii Lebedynskyi",
      description="API server for FMS client",
      entry_points = {"console_scripts":
                          ["fms = fms.server_starter:start"]},
      packages = find_packages(),
      author_email="vetal.lebed@gmail.com",
      install_requires=get_requirements()
      )