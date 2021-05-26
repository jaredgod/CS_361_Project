import requests
import scraper

s = scraper.Settings()
s.add_requirement('wiki/Category:')
s.add_exclusion('article')
s.add_exclusion('Article')
s.add_exclusion('Wikidata')
scraper.flaskified_sockets(s)