from group import is_grouped
import re
from config import DEAFULT_SIZE


def is_clause(query):
    if ' where ' in query:
        return True


def parse_clauses(query):
	


def selected_columns(query):
    query = re.split(' |, ', query)
    query = [q if q for q in query]
    cols = []
    for col in query[:query.index('from')]:
        if col != '*':
            cols.append(col)

    return cols


def get_size_from(query):
	query = re.split(' |, ', query)
    query = [q if q for q in query]

    if 'limit' in query:
    	_limit = query[query.index('limit')+1]
    else:
    	_limit = DEAFULT_SIZE

    if 'from' in query:
    	_from  = query[query.index('from')+1]
    else:
    	_from = 0

    return {"from": _from,"size": _limit}
