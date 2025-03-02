from django.shortcuts import get_object_or_404, render, redirect # type: ignore
from django.core.paginator import EmptyPage, Paginator, PageNotAnInteger # type: ignore
from .models import Post, Comment # type: ignore
from django.views.generic import ListView # type: ignore

from django.core.mail import send_mail # type: ignore
from django.views.decorators.http import require_POST # type: ignore
from taggit.models import Tag # type: ignore

from django.db.models import Count # type: ignore

from .forms import CommentForm, EmailPostForm, SearchForm, ContactUsForm, CommentEditForm # type: ignore

from django.contrib.postgres.search import SearchVector,SearchQuery,SearchRank # type: ignore
from django.contrib.postgres.search import TrigramSimilarity # type: ignore

from django.contrib import messages # type: ignore

from django.http import HttpResponseForbidden, HttpResponseRedirect # type: ignore


def home_page(request):
    return render(
        request,
        'blog/post/home.html'
        
    )





def post_list(request, tag_slug=None):

    post_list = Post.published.all()

    tag = None
    tag_exist = False
    if tag_slug:

        tags= Tag.objects.all()
        
        for tag in tags:
            if tag.slug == tag_slug:
                tag_exist = True
                break


        if  tag_exist:
            tag = get_object_or_404(Tag, slug=tag_slug)
        else:
            print('tag not exist')

        
        post_list = post_list.filter(tags__in=[tag])



        
    # Pagination with 3 posts per page
    paginator = Paginator(post_list, 3)
    page_number = request.GET.get('page', 1)

    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        # If page_number is not an integer get the first page
        posts = paginator.page(1)    
    except EmptyPage:
        # If page_number is out of range get last page of results
        posts = paginator.page(paginator.num_pages)

    

   # posts = Post.published.all()
    return render(
        request,
        'blog/post/list.html',
        {'posts': posts,
         'tag': tag,
         
         }
    )


def post_detail(request, year, month, day, post):
    post = get_object_or_404(
        Post,        
        status=Post.Status.PUBLISHED,
        slug=post,
        publish__year=year,
        publish__month=month,
    )

    # List of active comments for this post
    comments = post.comments.filter(active=True)
    # Form for users to comment
    form = CommentForm()

    # List of similar posts
    post_tags_ids = post.tags.values_list('id', flat=True)
    similar_posts = Post.published.filter(tags__in=post_tags_ids).exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags', '-publish')[:4]


    return render(
        request,
        'blog/post/detail.html',
        {
         'post': post,
         'comments': comments,
         'form': form,
         'similar_posts': similar_posts
        }
    )


class PostListView(ListView):
    """
    Alternative post list view
    """
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'


def post_share(request, post_id):
    # Retrieve post by id
    post = get_object_or_404(
        Post,
        id=post_id,
        status=Post.Status.PUBLISHED
    )
    sent = False


    if request.method == 'POST':
        # Form was submitted
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # Form fields passed validation
            cd = form.cleaned_data
            # ... send email


            post_url = request.build_absolute_uri(
                post.get_absolute_url()
            )
            subject = (
                f"{cd['name']} ({cd['email']}) "
                f"recommends you read {post.title}"
            )
            message = (
                f"Read {post.title} at {post_url}\n\n"
                f"{cd['name']}\'s comments: {cd['comments']}"
            )
            send_mail(
                subject=subject,
                message=message,
                from_email=None,
                recipient_list=[cd['to']]
            )
            sent = True
    else:
        form = EmailPostForm()
    return render(
        request,
        'blog/post/share.html',
        {'post': post,
        'form': form,
        'sent': sent
        }
    )    



@require_POST
def post_commented(request, post_id):
    post = get_object_or_404(
        Post,
        id=post_id,
        status=Post.Status.PUBLISHED
    )
    comment = None
    # A comment was posted
    form = CommentForm(data=request.POST)
    if form.is_valid():
        # Create a Comment object without saving it to the database
        comment = form.save(commit=False)
        # Assign the post to the comment
        comment.post = post
        # Save the comment to the database
        comment.save()
    return render(
        request,
        'blog/comment/commented.html',
        {
        'post': post,
        'form': form,
        'comment': comment
        }
    )

def post_search(request):
    form = SearchForm()
    query = None
    results = []
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            search_vector = SearchVector('title', weight='A') + SearchVector('body', weight='B')
            search_query = SearchQuery(query)
            # results = (
            #     Post.published.annotate(
            #             search=search_vector,
            #             rank=SearchRank(search_vector, search_query)
            #         )
            #         .filter(rank__gte=0.3)
            #         .order_by('-rank')
            # )

            results = (
                Post.published.annotate(
                    similarity=TrigramSimilarity('title', query),
                ).filter(similarity__gt=0.1).order_by('-similarity')
            )


    return render(
        request,
        'blog/post/search.html',
        {
            'form': form,
            'query': query,
            'results': results
        }
    )



def contact_us(request):
    sent = False
    if request.method == 'POST':
        # Form was submitted
        form = ContactUsForm(request.POST)
        if form.is_valid():
            # Form fields passed validation
            cd = form.cleaned_data

            # ... send email           
            subject = (               
                f"from {cd['first_name']} {cd['last_name']}  "
            )
            message = (
                f"{cd['message']}"               
            )
            send_mail(
                subject=subject,
                message=message,
                from_email=None,
                recipient_list=['kmezin@yahoo.com']
            )
            sent = True
    else:
        form = ContactUsForm()
    return render(
        request,
        'blog/post/contact_us.html',
        {
        'form': form,
        'sent': sent
        }
    )   


def comment_page(request, post_id):
     # Retrieve post by id
    post = get_object_or_404(
        Post,
        id=post_id,
        status=Post.Status.PUBLISHED
    )

     # List of active comments for this post
    comments = post.comments.filter(active=True)
    # Form for users to comment
    form = CommentForm()

    # List of similar posts
    post_tags_ids = post.tags.values_list('id', flat=True)
    similar_posts = Post.published.filter(tags__in=post_tags_ids).exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags', '-publish')[:4]

    return render(
        request,
        'blog/comment/comment_page.html' ,
        { 
            'post': post,
            'form': form,
            'comments': comments
        }     
        
    )



def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    
    

    if request.method == 'POST':

        print("POST data:", request.POST)

        # Check if the delete button was clicked
        if 'delete' in request.POST:
            post = comment.post  # Save post before deleting comment
            comment.delete()
            messages.success(request, 'Comment deleted successfully')
            return redirect('blog:post_detail', year=post.publish.year,
                          month=post.publish.month, day=post.publish.day,
                          post=post.slug)
        
        elif 'cancel' in request.POST:
            return HttpResponseRedirect(request.path_info)     

        
        else:
            form = CommentEditForm(request.POST, instance=comment)
            if form.is_valid():
                form.save()
                messages.success(request, 'Comment updated successfully')
                return redirect('blog:post_detail', year=comment.post.publish.year,
                                month=comment.post.publish.month, day=comment.post.publish.day,
                                post=comment.post.slug)
    else:
        form = CommentEditForm(instance=comment)
    
    return render(request, 'blog/comment/comment_edit.html', {
        'comment': comment,
        'form': form,
       
    })
        