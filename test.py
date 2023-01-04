import csv
import json
from justwatch_client import *
import numpy as np

class Formatter:
  def get_provider(self, offer):
    package = offer['package_short_name']
    provider_list = {
      'hbm': 'HBO Max',
      'itu': 'Apple TV',
      'ply': 'Google Play',
      'mvp': 'Movistar Play',
      'prv': 'Amazon Prime Video',
      'lgu': 'Lionsgate Plus',
      'srp': 'Star+',
      'pmp': 'Paramount+',
      'nfx': 'Netflix',
    }
    return provider_list.get(package, package)

  def providers(self, jw_response):
    offers = jw_response.offers
    result = map(self.get_provider, offers)
    return np.unique(np.array(list(result)))

class Presenter:
  def __init__(self):
    self.fmt = Formatter()

  def present(self, jw_response):
    print(f"Título: {jw_response.title}")
    print(f"Disponible en: {self.fmt.providers(jw_response)}")

  def pretty(self, jw_response):
    print(json.dumps(jw_response.offers, sort_keys=True, indent=3))

class Watchlist:
  def __init__(self):
    self.movies = []
    with open('watchlist.csv') as csv_file:
      csv_reader = csv.reader(csv_file, delimiter=',')
      next(csv_reader, None)    # Se saltea el header. Es más lindo con pandas

      for row in csv_reader:
        self.movies.append(row[1])

  def where_to_watch(self):
    jw = JWQuery()
    pres = Presenter()
    for movie in self.movies:
      print(f"Pre req: {movie}")
      results = jw.request(movie)
      pres.present(results)

watchlist = Watchlist()
watchlist.where_to_watch()
