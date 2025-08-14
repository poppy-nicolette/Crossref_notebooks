# reconstruct_abstract.py
# reconstruct abtract - from https://stackoverflow.com/questions/72093757/running-python-loop-to-iterate-and-undo-inverted-index

def reconstruct_abstract(abstract:dict)-> str:

    """
    For use on inverted abstracts from OpenAlex REST API.
    This takes a dictionary of the inverted abstract
    and returns a string of the reconstructed abstract.

    Args:
        abstract should be in the form of a dictionary.

        Example:
            abstract_inverted_index = {
            'Despite':[0],
            'growing':[1],
            'interest': [2],
            'in': [3],
            'Open': [4],
            'Access': [5],
            '...': [6]

    Returns:
        String
    """

    # Create a list of (word, index) pairs
    word_index = []
    for k, v in abstract.items():
        for index in v:
            word_index.append([k, index])

    #print(word_index) # uncomment to see the sublists
    # Sort the list based on index
    word_index = sorted(word_index, key=lambda x: x[1]) # this sorts based on the second item in the sublist

    # Join the words with a space
    abstract = ' '.join([word for word, index in word_index])
    return abstract
