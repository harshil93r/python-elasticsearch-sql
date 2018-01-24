'''
parser

-	select
-	group by
-	where
-	range
-
'''
from nested import is_nested
from clause import is_clause, selected_columns, get_size_from
import sqlparse


def parse(query):
	es_query = {}
    if is_nested(query):
        pass
    else:
        _index = get_index(query)
        selected_cols = selected_cols(query)
        if selected_cols:
        	es_query["_source"]= {
				"includes": selected_cols,
				"excludes": []
			} 

		es_query.update(get_size_from(query))
        if is_clause(query):
        	






def get_index(query):
    query = query.split()
    index_pos = query.index('from') + 1
    return query[index_pos]


parse('select * from pd where (x = 3) and (x=2 or x=9)')
