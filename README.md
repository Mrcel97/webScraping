# WebScraping Project.

## 1. Introduction.
The aim of this project is to get as much information as we can from the daily free eBook from [Packtpub website](https://www.packtpub.com/).

## 2. Previous information.  
In code lines 13 and 14 replace email and password for your own personal information.  
`13. email_user = ["example@gmail.com", "password"]`  
`14. email_send = "example@gmail.com"`  

In code lines 90 to 93 replace deffault keys for your own personal [twitterAPI](https://developer.twitter.com/) keys.  
`90. access_token = 'ACCESS_TOKEN'`  
`91. access_token_secret = 'SECRET_ACCESS_TOKEN'`  
`92. consumer_key = 'CONSUMER_KEY'`  
`93. consumer_secret = 'CONSUMER_SECRET'`

## 3. Project composition.

  **1. Get all the HTML from Packtpub.**   
  This step sonsists in getting all webpage html information using [urllib2](https://docs.python.org/2/library/urllib2.html).  
   `import urllib2`
  
  **2. Get the book title from the HTML.**  
  On second step we will select the title from all the HTML webpage information using 
  [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/).  
  `import BS4`
  
  **3. Get the book description from the HTML.**  
  As we have done on the second step we will use BS4 tools to select the description from among all the information from the webpage.
  
  **4. Get the book strong point from the HTML.**  
  We will use a loop to collect the book strong points from the `<dive>` objects from the website because this objects does not provide any
  a class to ease the webScraping process.
  
  **5. (Optional) Get the cover of the book.**  
  In this spet we will find the image (img) field to download to our directory the cover of the book.  
  `import urllib`
  
  **6. (Optional) Send Book information to an email address.**  
  Using the [Simple Mail Transfer Protocol](https://docs.python.org/2/library/smtplib.html) (SMTP) we will send all the collected 
  information to a private email address.  
  `import smtplib`
  
  **7. (Optional) Send Book title and cover using twitter.**  
  Using [Twitter API](https://github.com/geduldig/TwitterAPI) post a new tweet which will contain the title of the book and a picture of
  its cover. Here we will not post the book
  description or its strong points due the Twitter characters restriction.
  
 ## 4. Libraries.  
 Application needed libraries are:  
 * BeautifulSoup4 (4.6.0): `pip intall beautifulsoup4`  
 * lxml XML toolkit (4.1.1): `pip install lxml`
 * Twitter API (2.5.0): `pip install TwitterAPI`
