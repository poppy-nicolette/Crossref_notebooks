#check_for_multiple_abstracts.py
"""
This script checks for multiple abstracts in an XML api call using a pandas dataframe which includes
a column for the DOI. The DOI should be formatted as prefix and suffix, without the resolver.
Returns:
    bool: True if multiple abstracts are found, False otherwise
    int: Number of empty abstracts found
Usage:
    #adds two columns to the abstract_check dataframe
    # Note use of tqdm
    from tqdm import tqdm
    tqdm.pandas(colour='magenta')# whatever colour you like
    #this returns a tuple of (bool,int) in a Series which is unpacked into two columns
    abstract_check[['has_multiple_flag', 'empty_count']] = abstract_check['DOI'].progress_apply(main_for_multiple_abstracts).apply(pd.Series)
    print(Fore.GREEN + f"All done for the abstracts!")
"""
import requests
import re
import time
from functools import lru_cache
from tqdm import tqdm


def check_for_multiple_abstracts(xml_text: str) -> bool:
    """
    Looks for multiple abstracts in an XML api call
    Returns True if multiple abstracts are found, False otherwise
    """
    # Pattern to match jats:abstract elements (including multi-line content)
    pattern = r"<jats:abstract[^>]*>.*?</jats:abstract>"

    #find all matches using re.DOTALL flag to match across newlines
    matches = re.findall(pattern, xml_text, re.DOTALL)
    matches_count = len(matches)
    #print(f"Found {matches_count} abstract elements")

    # Print each abstract for inspection
    #for i, abstract in enumerate(matches, 1):
    #    print(f"\nAbstract {i}:")
    #    print(abstract[:200] + "..." if len(abstract) > 200 else abstract)

    # Pattern to match empty abstracts
    empty_pattern = [r"<jats:p />", r"<jats:p/>"]
    empty_matches = re.findall(empty_pattern[0], xml_text, re.DOTALL) or re.findall(empty_pattern[1], xml_text, re.DOTALL)
    empty_count = len(empty_matches)

    return matches_count > 1, empty_count

@lru_cache
def main_for_multiple_abstracts(x:str):
    """
    Checks for multiple abstracts. Runs function check_for_multiple_abstracts(xml_text)
    Inputs:
        DOI:str
    Returns:
        - boolean if there are empty abstracts
        - int of empty abstract count
    """
    doi:str = x
    print(Fore.LIGHTCYAN_EX + f"Running DOI: {doi}")
    API:str = f"https://doi.crossref.org/search/doi?pid=pnriddle@dal.ca&format=unixsd&doi={doi}"
    time.sleep(0.5)
    r = requests.get(API)
    #print(r.status_code)
    xml_text = r.text

    # Call the func
    has_multiple, empty_count = check_for_multiple_abstracts(xml_text)

    return has_multiple, empty_count
