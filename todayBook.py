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

    @staticmethod
    def __check_none(parameter):
        if parameter is None:
            print("Today there is no book available, sorry :(")
            exit(0)

    def __parse_info(self, book_summary_html):
        loops = 0

        for section in book_summary_html:
            if loops is 7:
                book_desc_html = section
                self.__check_none(book_desc_html)
            loops += 1
        return book_desc_html

    def get_book_info(self):
        html = self.__get_html()

        soup = bs4.BeautifulSoup(html, "lxml")
        book_summary_html = soup.find("div", "dotd-main-book-summary float-left")
        self.__check_none(book_summary_html)
        book_title_html = book_summary_html.find("div", "dotd-title")

        book_desc_html = self.__parse_info(book_summary_html)


if __name__ == "__main__":
    packtClient = BookClient()
    packtClient.get_book_info()