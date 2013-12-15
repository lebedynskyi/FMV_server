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
import logging.config


DEFAULT_FILE_FOR_LOGGING = "/var/log/FMS/server.log"


def init_logger(config_path):
    if config_path == "*":
        _init_default_logger()
        return

    try:
        _init_logger_from_path(config_path)
    except BaseException:
        print("Cannot init logger with config %s" % config_path)
        _init_default_logger()


def _init_logger_from_path(path):
    logging.config.fileConfig(path)


def _init_default_logger():
    print("Initialization of default logger")
    # create logger
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    # create file handler and set level to debug
    fh = logging.FileHandler(DEFAULT_FILE_FOR_LOGGING, encoding="utf-8")
    fh.setLevel(logging.WARNING)

    # create Console handler and set level to debug
    sh = logging.StreamHandler()
    sh.setLevel(logging.DEBUG)

    #create formatters for loggers
    simple_formatter = logging.Formatter("%(asctime)s - %(name)s - "
                                         "%(levelname)s - %(message)s")

    complex_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(module)s : %(lineno)d - %(message)s")

    # add formatter to handlers
    fh.setFormatter(complex_formatter)
    sh.setFormatter(simple_formatter)

    # add handlers to logger
    logger.addHandler(fh)
    logger.addHandler(sh)