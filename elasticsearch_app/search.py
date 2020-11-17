""" from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import Text, Date, Document, Integer

#bulk indexing of data
from elasticsearch.helpers import bulk
from elasticsearch import Elasticsearch
from .models import BlogPost


#define a default Elasticsearch client
connections.create_connection()


class BlogPostIndex(Document):
    author = Text(analyzer='snowball', fields={'raw': String(index='not_analyzed')})
    posted_date = Date()
    title = Text(analyzer="snowball")
    text = Text()
    
    class Meta:
        index = 'blogpost-index'

def bulk_indexing():
    BlogPostIndex.init()
    es = Elasticsearch()
    blogpost_all = BlogPost.objects.all()
    bulk(client=es, actions=(b.indexing() for b in blogpost_all.iterator())) """