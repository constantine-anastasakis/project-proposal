# Use this script to collect and organize information from Yelp.com

# This script requires the user to install Beautiful Soup, a Python package for parsing HTML and XML documents - documentation (including installation information) avaiable here: https://www.crummy.com/software/BeautifulSoup/bs4/doc/

# This script also requires the user to install pandas, a software library for data manipulation and analysis - documentation (including installation information) available here: https://pandas.pydata.org

# To handle unusual characters, this script produces a CSV using Pandas DataFrame (rather than the CSV module).

from bs4 import BeautifulSoup
import requests
import pandas

# The default starting URL in this script shows the first page of listings for "Restaurants" in "New York." User can swap the URL with the URL of the first page of search results for any search query.

# The starting URL will only provide the first 30 search listings, the script must be able to crawl ALL listings.

search_results = range(0,990,30)

products = []

for step in search_results:

    r = requests.get(f"https://www.yelp.com/search?find_desc=Restaurants&find_loc=New+York,+NY&start={step}")
    soup = BeautifulSoup(r.text, "html.parser")
    listings = soup.select(selector=".regular-search-result")

    for listing in listings:

        try: #There are many unusual characters or other issues that will cause the script to error out if we don't use Try/Except.
            business_name = listing.find("a",{"class":"biz-name"})
            category = listing.find("span",{"class":"category-str-list"})
            neighborhood = listing.find("span",{"class":"neighborhood-str-list"})
            address = listing.find("address")
            phone = listing.find("span",{"class":"biz-phone"})

            d = {"business_name":business_name.text.strip(),"category":category.text.strip(),"neighborhood":neighborhood.text.strip(),"address":address.text.strip(),"phone":phone.text.strip()}
            products.append(d)
            print(d)

        except Exception as e:
            print(str(e)) # Script will just print the error, wont halt.


df = pandas.DataFrame.from_records(products)

df.head()

df.shape

df.to_csv('yelp_scrapings.csv',index=False,header=True) # This will drop a CSV with the scraped data wherever the python script is run from.
