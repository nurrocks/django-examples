from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from django.core.mail import send_mail

from .models import Post
from .forms import EmailPostForm

# def post_list(request):
#     object_list = Post.published.all()
#     paginator = Paginator(object_list, 2) # 3 posts in each page
#     page = request.GET.get('page')

#     try:
#     	posts = paginator.page(page)
#     except PageNotAnInteger:
#     	posts = paginator.page(1)
#     except EmptyPage:
#     	posts = paginator.page(paginator.num_pages)

#     return render(request, 'blog/post/list.html', {
#     	'posts': posts
#     })


class PostListView(ListView):
	queryset = Post.published.all()
	context_object_name = 'posts'
	paginate_by = 2
	template_name = 'blog/post/list.html'



def post_detail(request, year, month, day, post):
	post = get_object_or_404(Post,slug=post,
	                              status='published',
	                              publish__year=year,
	                              publish__month=month,
	                              publish__day=day)
	return render(request,
	             'blog/post/detail.html',
	             {'post': post})



def post_share(request, post_id):
	# Retrieve post by id
	post = get_object_or_404(Post, id=post_id, status='published')
	sent = False

	if request.method == 'POST':
	   	# Form was submitted
	   	form = EmailPostForm(request.POST)
	   	if form.is_valid():
	   		clean_data = form.cleaned_data
	   		post_url = request.build_absolute_uri(post.get_absolute_url())

	   		subject = '{} ({}) recommends you reading "{}"'.format(clean_data['name'], clean_data['email'], post.title)
	   		message = 'Read "{}" at {}\n\n{}\'s comments: {}'.format(post.title, post_url, clean_data['name'], clean_data['comments'])
	   		# send_mail(subject, message, 'zhexiao421223@gmail',[clean_data['to']])
	   		sent = True
	else:
	   	form = EmailPostForm()
	return render(request, 'blog/post/share.html', {'post': post,
                                                    'form': form,
                                                    'sent' : sent
                                                    })