

import os
from serpapi import GoogleSearch
import time
import csv
from dotenv import load_dotenv
load_dotenv()


#Order
# Geiger, Hennig, von Luxburg, Butz
# Hein, Lensch, Macke, Pons-Moll
# Zell, Schilling, Wichmann, Williamson
# Schölkopf
AUTHOR_ID_LIST=['u7w1MYcAAAAJ', '0uEkSPQAAAAJ', 'NxrQ794AAAAJ', 'G4MBruQAAAAJ',
                'DZ-fHPgAAAAJ' ]



# Saves the scraped articles of a prof as csv
def saveAsCSV(cur_author, articles, location=None):

    #remove dots and spaces from main author_name
    name_cleaned = cur_author.translate(str.maketrans('', '', ' .'))
    if location == None:
        location = f'Data/articles_{name_cleaned}.csv'
    

    with open(location, mode='w', newline='', encoding='utf-8') as csv_file:
        # Add 'author_name' at the beginning of fieldnames and exclude 'link' and 'citation_id'
        fieldnames = ['author_name'] + [key for key in articles[0].keys() if key not in ['link', 'citation_id']]
        
        # Replace 'cited_by' in fieldnames with 'cited_by_value'
        fieldnames = ['cited_by_value' if field == 'cited_by' else field for field in fieldnames]

        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()

        # Write the rows
        for article in articles:
            row = {'author_name': cur_author}

            # Exclude 'link' and 'citation_id' fields and extract 'value' from 'cited_by'
            for key in fieldnames:
                if key in article and key not in ['author_name', 'cited_by_value', 'link', 'citation_id']:
                    row[key] = article[key]
                if key == 'cited_by_value' and 'cited_by' in article:
                    row[key] = article['cited_by'].get('value', '')

            writer.writerow(row)



def fetch_results(params):
    print('token used')
    search = GoogleSearch(params)
    results = search.get_dict()
    return results


def main():

    api_key = os.getenv('SERPAPI_KEY')

    for author_id in AUTHOR_ID_LIST:

        print(author_id)

        params = {
            "engine": "google_scholar_author",
            "author_id": author_id,
            "api_key": api_key,
            "start": 0
        }

        articles = []

        # Fetch the first set of results
        results = fetch_results(params)
        cur_author = results['author']['name']
        articles.extend(results.get("articles", []))

        # Continue fetching until 'next' is not present
        while 'next' in results.get("serpapi_pagination", {}):
            params["start"] += 20  # Assuming 20 results per page
            results = fetch_results(params)
            articles.extend(results.get("articles", []))
            time.sleep(1)  # Pause to avoid rate limiting

        saveAsCSV(cur_author, articles)





if __name__ == "__main__":
    main()





