class Movie:
  def __init__(self, query_name, name, providers) -> None:
    self.query_name = query_name
    self.name = name
    self.providers = self.get_provider(providers)
    self.available = len(self.providers) > 0
  
  def get_provider(self, providers):
    pr = []
    for prov in providers:
      pr.append(prov['package_short_name'])
    return pr
  