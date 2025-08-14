#get_openalex_data()

# [x]: added requests.Session()<--
# get_openalex_data.py
import requests
import time
from functools import lru_cache
from reconstruct_abstract import reconstruct_abstract

# Create a session object
session = requests.Session()

# send call to OpenAlex API
@lru_cache
def get_openalex_data(doi: str) -> dict:
    """
    Used to retrieve data from the OpenAlex API.
    Arg: takes a DOI as a string without the resolver.
    Return: A dictionary of values.

    Note: oa_abstract is reconstructed from the function reconstruct_abstract(). You will need to install

    Example usage
        doi = "10.1234/example"
        data = get_openalex_data(doi)
        print(data)
    """


    URL = f"https://api.openalex.org/works?filter=doi:{doi}&select=doi,title,id,type,type_crossref,language,abstract_inverted_index,cited_by_count,is_paratext,primary_location"

    try:
        result = session.get(URL)

        if result.status_code == 200:
            data = result.json()

            # Parse json data into each element:
            oa_doi = data['results'][0]['doi'].lstrip('https://doi.org/')
            oa_title = data['results'][0]['title']
            oa_id = data['results'][0]['id']
            oa_type = data['results'][0]['type']
            oa_type_crossref = data['results'][0]['type_crossref']
            oa_language = data['results'][0]['language']
            oa_abstract_inverted_index = data['results'][0]['abstract_inverted_index']
            oa_cited_by_count = data['results'][0]['cited_by_count']
            oa_is_paratext = data['results'][0]['is_paratext']
            oa_primary_location_pdf_url = data['results'][0]['primary_location']['pdf_url']
            oa_license = data['results'][0]['primary_location']['license']
            oa_version = data['results'][0]['primary_location']['version']

            # Reconstruct abstract
            oa_abstract = reconstruct_abstract(oa_abstract_inverted_index)

            return {
                'oa_doi': oa_doi,
                'oa_type': oa_type,
                'oa_type_crossref': oa_type_crossref,
                'oa_is_paratext': oa_is_paratext,
                'oa_title': oa_title,
                'oa_abstract': oa_abstract,
                'oa_language': oa_language,
                'oa_cited_by_count': oa_cited_by_count,
                'oa_primary_location_pdf_url': oa_primary_location_pdf_url,
                'oa_version': oa_version,
                'oa_license': oa_license,
                'oa_id': oa_id,
            }
        else:
            print(f"Error: Received status code {result.status_code} for DOI {doi}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Request failed for DOI {doi}: {e}")
        return None
    finally:
        # Sleep so that you are below the 10 per second limit or 100k per day.
        time.sleep(0.11)
