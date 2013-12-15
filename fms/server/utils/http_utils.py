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
import urllib
import urllib2
import urlparse


def do_get(url, params=None):
    if not url:
        raise ValueError("url cannot be empty")

    valid_url = generate_url(url, params)
    headers = get_random_headers()

    req = urllib2.Request(valid_url)

    for k in headers.keys():
        req.add_header(k, headers[k])

    try:
        f = urllib2.urlopen(req)
        response = f.read()
        return response
    finally:
        f.close()


def get_random_headers():
    #TODO we need two method get random and get necessary
    return {"Content-Encoding": "UTF-8", "Accept-Charset": "UTF-8"}


def generate_url(base_url, params):
    if params is None:
        return base_url

    count = 0
    for k in params.keys():
        if count == 0:
            divider = "?"
        else:
            divider = "&"
        count += 1
        value = params[k]
        if value is None:
            continue
        base_url += divider + k + "=" + url_fix(str(value))
    return base_url


def url_fix(s, charset='utf-8'):
    if isinstance(s, unicode):
        s = s.encode(charset, 'ignore')
    scheme, netloc, path, qs, anchor = urlparse.urlsplit(s)
    path = urllib.quote(path, '/%')
    qs = urllib.quote_plus(qs, ':&=')
    return urlparse.urlunsplit((scheme, netloc, path, qs, anchor))
