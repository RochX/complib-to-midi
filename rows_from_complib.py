import requests

# type is either "method" or "composition"
def get_rows(complib_id, type):
  r = requests.get(f"https://complib.org/{type}/{complib_id}/rows")

  rows = r.text.split()

  return rows