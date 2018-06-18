# Project Planning

## Problem Statement

### Primary User

The operator of an ecommerce marketplace (for ex: Etsy) that wants to locate new sellers to participate by scraping information from relevant sites (for ex: Yelp).

### User Needs Statement 

As the operator of a marketplace, I need to acquire new sellers who can offer products that there is high demand for.

### To-be Process Description

1. Locate a website that contains the contact information for high-intent sellers.
2. Run a script that crawls the given website and writes the data to a CSV file.
3. Provide the list to an employee to reach out to these potential sellers.

## Information Requirements

### Information Inputs

1. A website with structured data to be crawled.
2. A CSV with headers to be written to.

### Information Outputs

1. A results.csv file containing the results of the crawling process.

## Technology Requirements

### APIs and Web Service Requirements

This application does not require any third-party APIs.

### Python Package Requirements

This application requires the BeautifulSoup package.

### Hardware Requirements

The application will be running on my own local machine. I have no plans to deploy this application to a public server.
