# Planning

## Problem Statement

### Primary User

The operator of a platform that allows consumers to order food for delivery from local restaurants (for example: Seamless or UberEats) that wants to locate new restaurants to participate by scraping information from relevant sites (for ex: Yelp).

### User Needs Statement 

As the operator of an online food ordering platform, I need to acquire new restaurants in New York who can offer menu items that there is high demand for.  

### To-be Process Description

1. Locate a website that contains the contact information for high-intent sellers.
2. Run a script that crawls the given website and writes the data to a CSV file.
3. Provide the list to an employee to reach out to these potential sellers.

## Information Requirements

### Information Inputs

1. A website with structured data to be crawled.
2. A CSV with headers to be written to.

### Information Outputs

1. A file containing the results of the crawling process called "yelp_scrapings.csv."

## Technology Requirements

### APIs and Web Service Requirements

This application does not require any third-party APIs.

### Python Package Requirements

This script requires the user to install Beautiful Soup, a Python package for parsing HTML and XML documents - documentation (including installation information) avaiable here: https://www.crummy.com/software/BeautifulSoup/bs4/doc/

This script also requires the user to install pandas, a software library for data manipulation and analysis - documentation (including installation information) available here: https://pandas.pydata.org

### Hardware Requirements

The application will be running on my own local machine. I have no plans to deploy this application to a public server.
