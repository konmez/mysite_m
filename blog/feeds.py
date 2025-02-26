import markdown   # type: ignore # markdown is a Python implementation of John Gruber’s Markdown
from django.contrib.syndication.views import Feed # type: ignore # Feed is a class that generates RSS feeds
from django.template.defaultfilters import truncatewords_html # type: ignore
from django.urls import reverse_lazy # type: ignore
from .models import Post

class LatestPostsFeed(Feed):
    title = 'My blog'
    link = reverse_lazy('blog:post_list')
    description = 'New posts of my blog.'

    def items(self):
        return Post.published.all()[:5]
    
    def item_title(self, item):
        return item.title
    
    def item_description(self, item):
        return truncatewords_html(markdown.markdown(item.body_comment), 30)
    
    def item_pubdate(self, item):
        return item.publish