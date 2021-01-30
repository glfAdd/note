import pysolr

solr = pysolr.Solr('http://localhost:8983/solr/test2', timeout=10)


def add_data():
    data = [
        {"id": "doc_1", "title": "A test document"},
        {"id": "doc_2", "title": "The Banana: Tasty or Dangerous? 2"}
    ]
    solr.add(data)
    solr.commit()


def search_data():
    res = solr.search('id:doc_1')
    # 相应数据概括
    print(res.raw_response)
    # 实际搜索到的数据
    print(res.docs)
    for i in res:
        print(i)


def delete_data():
    solr.delete(id='doc_1')
    solr.commit()


if __name__ == '__main__':
    # add_data()
    search_data()
