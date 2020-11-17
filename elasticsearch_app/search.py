from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import Text, Date, Document

#bulk indexing of data
from elasticsearch.helpers import bulk
from elasticsearch import Elasticsearch
import models

connections.create_connection()
class BlogPostIndex(Document):
    author = Text()
    posted_date = Date()
    title = Text()
    text = Text()
    
    class Meta:
        index = 'blogpost-index'

def bulk_indexing():
    BlogPostIndex.init()
    es = Elasticsearch()
    bulk(client=es, actions=(b.indexing() for b in models.BlogPost.objects.all().iterator()))