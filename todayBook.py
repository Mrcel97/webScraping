#!/user/bin/env python
# -*- coding: utf-8 -*-
#vim: set filencoding=utf-8 :

"""
Client weatherUnderground
.json pot canviar-se per .xml normalment
"""
import urllib2
import bs4


class BookClient(object):

    @staticmethod
    def __get_html():
        url = "https://www.packtpub.com/packt/offers/free-learning/"

        f = urllib2.urlopen(url)
        html = f.read()
        f.close()
        return html


if __name__ == "__main__":
    packtClient = BookClient()