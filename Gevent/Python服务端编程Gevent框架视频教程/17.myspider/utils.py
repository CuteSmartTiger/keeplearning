#!/usr/bin/env python
#-*- coding: utf-8 -*-

import re
import urllib
import urlparse
from pyquery import PyQuery

class HtmlAnalyzer(object):

    @staticmethod
    def detectCharSet(html):
        pq = PyQuery(html)
        metas = pq('head')('meta')
        for meta in metas:
            for key in meta.keys():
                if key == "charset":
                    charset = meta.get('charset')
                    return charset
                elif key == "content":
                    try:
                        content = meta.get('content')
                        p = re.match(r".+charset=(.*)\W*", content)
                        charset = p.group(1)
                        return charset
                    except:
                        continue

    @staticmethod
    def extractLinks(html, baseurl, charset):
        def _extract(url, attr):
            link = url.attrib[attr]
            link = link.strip("/ ").strip('\\"')
            if link is None:
                raise

            link = urlparse.urljoin(baseurl, link)
            link = urlparse.urldefrag(link)[0]

            try:
                link = urllib.quote(link, ':?=+&#/@')
            except (UnicodeDecodeError, KeyError):
                try:
                    link = urllib.quote(link.encode(charset), ':?=+&#/@')
                except:
                    pass

            return link

        def _isValidLink(url):
            try:
                return all([UrlFilter.checkScheme(url),
                            UrlFilter.checkInvalidChar(url),
                            UrlFilter.checkInvalidExtention(url)
                            ])
            except:
                return False

        pq = PyQuery(html)

        allLinks = []

        for url in pq('a'):
            try:
                link = _extract(url, 'href')
            except:
                continue
            if _isValidLink(link):
                allLinks.append(link)

        for url in pq('form'):
            try:
                link = _extract(url, 'action')
            except:
                continue
            if _isValidLink(link):
                allLinks.append(link)
        return allLinks

class UrlFilter(object):

    invalid_chars = {'\'': None,
                     '\"': None,
                     '\\': None,
                     ' ': None,
                     '\n': None,
                     '\r': None,
                     '+': None
                     }

    invalid_extention = {
        'jpg':  None,
        'gif':  None,
        'bmp':  None,
        'jpeg':  None,
        'png':  None,

        'swf':  None,
        'mp3':  None,
        'wma':  None,
        'wmv':  None,
        'wav':  None,
        'mid':  None,
        'ape':  None,
        'mpg':  None,
        'mpeg':  None,
        'rm':  None,
        'rmvb':  None,
        'avi':  None,
        'mkv':  None,

        'zip':  None,
        'rar':  None,
        'gz':  None,
        'iso':  None,
        'jar':  None,

        'doc':  None,
        'docx':  None,
        'ppt':  None,
        'pptx':  None,
        'chm':  None,
        'pdf':  None,

        'exe':  None,
        'msi':  None,
    }

    @staticmethod
    def checkScheme(url):
        scheme, netloc, path, pm, q, f = urlparse.urlparse(url)
        return scheme in ('http', 'https')

    @classmethod
    def checkInvalidChar(cls, url):
        exist_invalid_char = False
        for c in url:
            if c in cls.invalid_chars:
                exist_invalid_char = True
                break
        return (not exist_invalid_char)

    @classmethod
    def checkInvalidExtention(cls, url):
        dotpos = url.rfind('.') + 1
        typestr = url[dotpos:].lower()
        return (typestr not in cls.invalid_extention)