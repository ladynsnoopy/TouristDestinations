# TouristDestinations

To run this: 
Please install Selenium and Scrapy packages, download a chrome driver for your chrome version and place it in the Drivers folder. 
Replace the csv readers and writers's path with your own in tourdestination\navigateTripAdvisor.py and in tourdestination\spiders\samplecountry.py

Selenium is used for navigation of Trip Advisor page for all countries in tourdestination\navigateTripAdvisor.py
Scrapy is used for web scraping in tourdestination\spiders\samplecountry.py

To run the web scraper, 
go to the touristdestination directory and execute the command "scrapy crawl SampleCountry -o items.csv" (any name for csv)

I have already saved the result data in resultdata.csv

