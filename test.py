import csv
import json
from justwatch_client import *
import numpy as np
from movie import Movie

from collections import defaultdict, Counter
class Group:
  def by_provider(self, movies):
    lista = []
    for mov in movies:
      for prov in mov.providers:
        lista.append((prov, mov))
    inp = defaultdict(list)
    for k, v in lista: inp[k].append(v)
    return [{'prov':k, 'movie':Counter(v)} for k,v in inp.items()]

class Formatter:
  def get_provider(self, offer):
    # package = offer['package_short_name']
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
      'qbt': 'QubitTV',
      'ptv': 'PlutoTV',
      'dnp': 'Disney+',
      'clv': 'Claro Video',
      'mbi': 'Mubi'
    }
    return provider_list.get(offer, offer)

  def providers(self, movie: Movie):
    providers = movie.providers
    result = map(self.get_provider, providers)
    return np.unique(np.array(list(result)))

class Presenter:
  def __init__(self):
    self.fmt = Formatter()

  def present(self, movie: Movie):
    print(f"Título: {movie.name}")
    print(f"Disponible en: {self.fmt.providers(movie)}")
  
  def group_present(self, diccio):
    for val in diccio:
      print(self.fmt.get_provider(val['prov']))
      for mov in val['movie']:
        print(f"    -> {mov.name}")

  # def pretty(self, jw_response):
  #   print(json.dumps(jw_response.offers, sort_keys=True, indent=3))

class Watchlist:
  def __init__(self):
    self.movies = []
    self.watchlist = []
    with open('watchlist.csv') as csv_file:
      csv_reader = csv.reader(csv_file, delimiter=',')
      next(csv_reader, None)    # Se saltea el header. Es más lindo con pandas

      for row in csv_reader:
        self.watchlist.append(row[1])
  
  def create_movie(self, query_name, name, providers):
    movie = Movie(query_name, name, providers)
    self.movies.append(movie)

  def fetch_movies(self):
    jw = JWQuery()
    print("Cargando películas en la base de datos")
    for titulo in self.watchlist:
      # print(f"Título en watchlist: {titulo}")
      results = jw.request(titulo)
      self.create_movie(titulo, results.title, results.offers)


  def where_to_watch(self):
    pres = Presenter()
    for movie in self.movies:
      pres.present(movie)
  
  def group(self):
    diccio = Group().by_provider(self.movies)
    pres = Presenter()
    pres.group_present(diccio)

if __name__ == "__main__":
  watchlist = Watchlist()
  watchlist.fetch_movies()
  #watchlist.where_to_watch()
  watchlist.group()
