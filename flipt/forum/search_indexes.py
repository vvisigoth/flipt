import datetime
from haystack.indexes import *
from haystack import site
from forum.models import Post

class PostIndex(SearchIndex):
    body = CharField(document=True, use_template=True)
    author= CharField(model_attr='creator')
    
    def index_queryset(self):
        return Post.objects.filter(created__lte=datetime.datetime.now())

site.register(Post, PostIndex)
