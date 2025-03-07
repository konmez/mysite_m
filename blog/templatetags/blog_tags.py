from django import template # type: ignore
from ..models import Post # type: ignore
from django.db.models import Count # type: ignore
import markdown # type: ignore




register = template.Library()

@register.simple_tag
def total_posts():
    return Post.published.count()

@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = Post.published.order_by('-publish')[:count]
    return {'latest_posts': latest_posts}


#from django.db.models import Count
@register.simple_tag
def get_most_commented_posts(count=4):
    return Post.published.annotate(
        total_comments=Count('comments')
    ).order_by('-total_comments')[:count]

#import markdown
from django.utils.safestring import mark_safe # type: ignore
@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))