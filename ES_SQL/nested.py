def is_nested(query):
    '''
    Argumenets:
            Query : the SQL query to which to check.

    Returns:
            Boolean : if the query is nested ot not.
    '''

    if query.count('select') > 1:
        return True

    return False
