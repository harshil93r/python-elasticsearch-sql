'''
parser

-	select 
-	group by
-	range
- 	
'''
from nested import is_nested
import sqlparse

def parse(query):
    if is_nested(query):
        pass
    else:
        _index = get_index(query)
        sqlparse.parse(query)


def get_index(query):
    query = query.split()
    index_pos = query.index('from') + 1
    return query[index_pos]


parse('select * from ')