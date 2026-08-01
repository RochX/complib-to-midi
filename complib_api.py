import requests

# parameter type is either "method" or "composition"

def api_request(complib_id, type):
  """
  Gets the reponse from the complib API.

  Parameters:
    complib_id: ID to fetch on complib.
    type: either "method" or "composition"
  """
  return requests.get(f"https://api.complib.org/{type}/{complib_id}/rows")

def get_rows(complib_id, type):
  """
  Gets the full API JSON response.

  Includes rows, the spoken calls, and row analysis.
  The result returns 2 rows of rounds before the start of the method/composition.

  See complib.org/api for more details on row analysis.
  """
  r = api_request(complib_id, type)
  return r.json()['rows']

def get_rows_short(complib_id, type):
  """
  Gets the rows from the API JSON response.

  The result returns 2 rows of rounds before the start of the method/composition.
  """
  r = api_request(complib_id, type)
  return [x[0] for x in r.json()['rows']]