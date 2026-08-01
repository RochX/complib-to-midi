import requests

# parameter type is either "method" or "composition"

def api_request(complib_id, type):
  return requests.get(f"https://api.complib.org/{type}/{complib_id}/rows")

def get_rows(complib_id, type):
  r = api_request(complib_id, type)
  return r.json()['rows']