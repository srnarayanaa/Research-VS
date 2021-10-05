import arxivscraper
scraper = arxivscraper.Scraper(category='cs', date_from='2015-09-21',date_until='2021-09-25')
output = scraper.scrape()

import pandas as pd
cols = ('id', 'title', 'categories', 'abstract', 'doi', 'created', 'updated', 'authors')
df = pd.DataFrame(output,columns=cols)
df.to_csv('papers.csv')

