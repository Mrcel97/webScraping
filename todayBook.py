#!/user/bin/env python
# -*- coding: utf-8 -*-

import urllib2
import urllib
import bs4
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from TwitterAPI import TwitterAPI

email_user = ["example@gmail.com", "password"]
email_send = "example@gmail.com"
url = "https://www.packtpub.com/packt/offers/free-learning/"


class BookClient(object):

    @staticmethod
    def __get_html():
        f = urllib2.urlopen(url)
        html = f.read()
        f.close()
        return html

    @staticmethod
    def get_jpg(soup):
        picture_html = soup.find("div", "dotd-main-book-image float-left")
        images = picture_html.findAll('img')[0]['src']
        URL = "https://" + images.split("//")[1]
        urllib.urlretrieve(URL, "bookCover.jpg")

    @staticmethod
    def __check_none(parameter):
        if parameter is None:
            return "No data provided."
        else:
            return parameter

    def send_email(self, msg):
        filename = 'bookCover.jpg'
        attachment = open(filename, 'rb')

        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment", filename=filename)

        msg.attach(part)
        text = msg.as_string()

        self.__send_server(text)

    @staticmethod
    def generate_msg(title, description, strong_points):

        message = '\n' + title.text.strip() + '\n\n'
        message = message + description.text.strip() + "\n\n"
        for obj in strong_points:
            message = message + "   - " + obj + "\n"

        msg = MIMEMultipart()
        msg['From'] = email_user[0]
        msg['To'] = email_send
        msg['Subject'] = "Packtpub Daily Free eBook"

        body = message.encode('utf-8')
        msg.attach(MIMEText(body, 'plain'))
        return msg

    @staticmethod
    def __send_server(text):
        print "\nSending email..."
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.login(email_user[0], email_user[1])
            server.sendmail(email_user, email_send, text)
            server.close()
            print "Successfully sent email."
        except:
            print "Error while sending email (Service unavailable/Wrong authentication)."

    @staticmethod
    def send_tweet(message):
        print "\n Posting on Twitter..."
        access_token = 'ACCESS_TOKEN'
        access_token_secret = 'SECRET_ACCESS_TOKEN'
        consumer_key = 'CONSUMER_KEY'
        consumer_secret = 'CONSUMER_SECRET'

        api = TwitterAPI(consumer_key, consumer_secret, access_token, access_token_secret)

        file = open('bookCover.jpg', 'rb')
        data = file.read()
        r = api.request('statuses/update_with_media', {'status': message}, {'media[]': data})
        code = r.status_code
        if code is not 200:
            print "Error while posting on Twitter (Service unavailable/Wrong authentication)."
            return
        print "\Successfully post."

    def __parse_info(self, book_summary_html):
        loops = 0
        book_desc_html = "No data provided."
        strong_points = []

        for section in book_summary_html:
            if loops is 7:
                book_desc_html = section
                book_desc_html = self.__check_none(book_desc_html)
            if loops is 9:
                details_html = section.find("ul")
                details_html = self.__check_none(details_html)
                for strong_point in details_html:
                    try:
                        strong_points.append(strong_point.text)
                    except AttributeError:
                        pass
            loops += 1
        return book_desc_html, strong_points

    @staticmethod
    def __print_info(title, description, strong_points):
        print title.text.strip()
        print description.text.strip()
        for obj in strong_points: print("   - " + obj)

    def get_book_info(self):
        html = self.__get_html()

        soup = bs4.BeautifulSoup(html, "lxml")
        self.get_jpg(soup)
        book_summary_html = soup.find("div", "dotd-main-book-summary float-left")
        book_title_html = book_summary_html.find("div", "dotd-title")
        book_title_html = self.__check_none(book_title_html)

        book_desc_html, strong_points = self.__parse_info(book_summary_html)
        self.__print_info(book_title_html, book_desc_html, strong_points)
        return book_title_html, book_desc_html, strong_points


if __name__ == "__main__":
    packtClient = BookClient()
    title, description, strong_points = packtClient.get_book_info()
    msg = packtClient.generate_msg(title, description, strong_points)
    packtClient.send_email(msg)
    packtClient.send_tweet(title.text.strip() + '\n' + url)  # max. 280 characters
