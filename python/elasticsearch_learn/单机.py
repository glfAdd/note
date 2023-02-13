# -*- coding: utf-8 -*-

"""
pip install elasticsearch
"""

from elasticsearch import Elasticsearch

es = Elasticsearch(
    [{'host': '10.135.0.19', 'port': 9200}],
    timeout=3600,
    http_auth=('gonglongfei', '8hv_tUW24xD_wrrauqRBQT')
)
query = {
    "query": {
        "match_all": {}
    }
}
result = es.search(index="megacorp", body=query)
print(result)
