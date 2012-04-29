import datetime
from haystack import indexes
from haystack import site
from forum.models import Post

class PostIndex(indexes.SearchIndex):
    body = indexes.CharField(document=True, use_template=True)
    author= indexes.CharField(model_attr='creator')
    content_auto = indexes.EdgeNgramField(model_attr='body')

    def index_queryset(self):
        return Post.objects.filter(created__lte=datetime.datetime.now())

site.register(Post, PostIndex)
