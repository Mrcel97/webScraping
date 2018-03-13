# WebScraping Project.

## 1. Introduction.
The aim of this project is to get as much information as we can from the daily free eBook from [Packtpub website](https://www.packtpub.com/).

## 2. Project composition.

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
  
  **5. Print collected information.**  
  
  **6. (Optional) Get the cover of the book.**  
  In this spet we will find the image (img) field to download to our directory the cover of the book.  
  `import urllib`
  
  **7. (Optional) Send Book information to an email address.**  
  Using the [Simple Mail Transfer Protocol](https://docs.python.org/2/library/smtplib.html) (SMTP) we will send all the collected 
  information to a private email address.  
  `import smtplib`
