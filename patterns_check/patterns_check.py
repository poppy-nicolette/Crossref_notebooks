# patterns_check.py
import re

"""
This contains functions for checking patterns in abstracts, such as math, HTML, and URLs.
Can be used for checking abstracts from sources such as Crossref, OpenAlex, PubMed, and more.
Only finds the first occurrence of each pattern and returns True if found.
Good for raising flags for potential errors or issues in the abstract.
Used with Pandas to create a new column with the results of the checks.
"""


def check_for_math_ml(abstract:str)->bool:
    """
    Checks if the abstract contains MathML tags.

    Args:
        abstract (str): The abstract to check.

    Returns:
        bool: True if MathML tags are found, False otherwise.
    """
    math_pattern = r"(<mml:.*>)"
    if re.search(math_pattern, abstract):
        a=True
    else:
        a=False
    return a

def check_for_tex_math(abstract:str)->bool:
    """
    Checks if the abstract contains TeX math tags.

    Args:
        abstract (str): The abstract to check.

    Returns:
        bool: True if TeX math tags are found, False otherwise.
    """
    pattern = r"(<jats:tex-math>)"
    if re.search(pattern, abstract):
        a=True
    else:
        a=False
    return a

# (http.*)|(?:!<mml:.*>)
def check_for_http(abstract:str)->bool:
    """
    Checks if the abstract contains HTTP or HTTPS links.

    Args:
        abstract (str): The abstract to check.

    Returns:
        bool: True if HTTP or HTTPS links are found, False otherwise.
    """
    pattern = [r"(https://.*)", r"(http://.*)"]
    if re.search(pattern[0], abstract):
        a = True
    elif re.search(pattern[1], abstract):
        a = True
    else:
        a = False
    return a

def check_for_HTML(abstract:str)->bool:
    """
    Checks if the abstract contains HTML tags.

    Args:
        abstract (str): The abstract to check.

    Returns:
        bool: True if HTML tags are found, False otherwise.
    """
    pattern = [r"(&lt)", r"(&gt)", r"(div class=.*)"]
    if re.search(pattern[0], abstract):
        a = True
    elif re.search(pattern[1], abstract):
        a = True
    elif re.search(pattern[2], abstract):
        a = True
    else:
        a = False
    return a

def check_for_figure(abstract:str)->bool:
    """
    Checks if the abstract contains figure references.

    Args:
        abstract (str): The abstract to check.

    Returns:
        bool: True if figure references are found, False otherwise.
    """
    pattern = [r"Figure \d*", r"Fig. \d*"]
    if re.search(pattern[0], abstract):
        a = True
    elif re.search(pattern[1], abstract):
        a = True
    else:
        a = False
    return a

def check_for_table(abstract:str)->bool:
    """
    Checks if the abstract contains table references.

    Args:
        abstract (str): The abstract to check.

    Returns:
        bool: True if table references are found, False otherwise.
    """
    pattern = [r"Table \d*"]
    if re.search(pattern[0], abstract):
        a = True
    else:
        a = False
    return a

def check_for_copyright(abstract:str)->bool:
    """
    Checks for copyright information in the abstract.

    Args:
        abstract (str): The abstract to check.

    Returns:
        bool: True if copyright information is found, False otherwise.
    """
    pattern = [r"(copyright-.*)", r"(<jats:copyright.*>)"]
    if re.search(pattern[0], abstract) or re.search(pattern[1], abstract):
        a = True
    else:
        a = False
    return a
