from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.views import View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import (
    HttpResponseRedirect,
    HttpResponseNotFound,
    JsonResponse,
)
from django.utils.text import slugify
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from profiles.models import UserProfile
from .models import Post, Comment
from .forms import (
    CommentForm,
    PostForm,
)
from django.db.models import Q, Case, When
from django.utils.safestring import mark_safe


class PostListView(ListView):
    """
    View for listing all blog posts on the index.html
    Using the ListView method
    """
    model = Post
    context_object_name = "posts"
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    paginate_by = 6

    def get_queryset(self):
        """
        Search function for posts
        """
        queryset = super().get_queryset()
        search_query = self.request.GET.get('search', None)

        # Use Q objects to combine filters with OR logic
        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query) |
                Q(author__username__icontains=search_query) |
                Q(content__icontains=search_query) |
                Q(excerpt__icontains=search_query)
            )

            # Prioritize matches in the title by using order_by
            queryset = queryset.order_by(
                Case(
                    When(title__icontains=search_query, then=0),
                    When(title__icontains=search_query, then=1),
                    default=2
                ),
                "-created_on"  # Additional ordering by created_on
            )

        return queryset

    def render_to_response(self, context, **response_kwargs):
        """
        If no posts found, return 'no_results'
        """
        if not context['posts']:
            context['no_results'] = True

        return super().render_to_response(context, **response_kwargs)


class PostDetailView(DetailView):
    """
    View for displaying the details of a post,
    including comments and comment form.
    """
    model = Post
    template_name = "post_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        post = context['post']
        comments = post.comments.filter(approved=True).order_by("-created_on")

        # Pagination for comments
        page = self.request.GET.get('page', 1)
        paginator = Paginator(comments, 6)
        try:
            paginated_comments = paginator.page(page)
        except PageNotAnInteger:
            paginated_comments = paginator.page(1)
        except EmptyPage:
            paginated_comments = paginator.page(paginator.num_pages)

        context['comments'] = paginated_comments
        context['paginator'] = paginator

        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
            context['liked'] = liked

        # Adding the comment form to the context
        comment_form = CommentForm()
        context['comment_form'] = comment_form

        # Add profile images of commenters to the context
        commenter_profile_images = {}
        for comment in comments:
            user_id = comment.user.id
            user_profile = UserProfile.objects.filter(user_id=user_id).first()
            profile_image_url = user_profile.profile_image.url if user_profile and user_profile.profile_image else None # noqa
            commenter_profile_images[user_id] = profile_image_url

        return context

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data()

        # AJAX pagination for comments
        if request.is_ajax():
            page = request.GET.get('page', 1)
            paginator = context['paginator']
            try:
                comments = paginator.page(page)
            except PageNotAnInteger:
                comments = paginator.page(1)
            except EmptyPage:
                comments = paginator.page(paginator.num_pages)

            comment_html = render_to_string(
                'comment_list.html', {'comments': comments}, request=request)

            return JsonResponse({'comment_html': comment_html})

        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data()

        # Retrieve the comment form from the request
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment_form.instance.user = request.user
            comment = comment_form.save(commit=False)
            comment.post = self.object
            comment.save()

            # Add a message to inform the user
            messages.success(self.request, "Comment posted!")

            # Redirect the user back to the post detail page w/ hash fragment
            return redirect(reverse(
                'post_detail', args=[self.object.slug]) + '#comments-section')

            # Set commented to True in context
            context['commented'] = True

        # Add the comment form to the context
        context['comment_form'] = comment_form

        # Return the response without handling AJAX pagination here
        return render(request, "post_detail.html", context)


class PostCreateView(LoginRequiredMixin, CreateView):
    """
    View for creating a post and assigning a slug to the new post
    """
    model = Post
    template_name = "post_form.html"
    form_class = PostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.slug = slugify(form.instance.title)
        response = super().form_valid(form)

        # Add a message to inform the user
        message = "Your post was created successfully!\
            <a href='{}'>Create another post</a>".format(
                reverse('post_new'))
        messages.success(self.request, mark_safe(message))

        return response

    def get_success_url(self):
        return reverse('post_detail', kwargs={'slug': self.object.slug})


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    View for creating a post and assigning a slug to the new post
    Removed LoginRequiredMixin, UserPassesTestMixin as I want any user
    with admin access to be able to edit blog posts
    """
    model = Post
    template_name = "post_form.html"
    form_class = PostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.slug = slugify(form.instance.title)
        response = super().form_valid(form)

        # Add a message to inform the user
        messages.success(self.request, "Your post has been updated!.")

        return response

    # Checks to see if the user who created the post is the one updating it
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

    def get_success_url(self):
        return reverse('post_detail', kwargs={'slug': self.object.slug})


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    View for deleting a single post
    Removed LoginRequiredMixin, UserPassesTestMixin as I want any user
    with admin access to be able to edit blog posts
    """
    model = Post
    template_name = "post_confirm_delete.html"
    success_url = '/blogs'

    # Checks to see if the user who created the post is the one deleting it
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

    # Add a message to inform the user
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Your post has been deleted.")
        return super().delete(request, *args, **kwargs)


class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    View for updating a single comment
    """
    model = Comment
    template_name = "comment_update.html"
    fields = ['body']

    def get_success_url(self):
        messages.success(self.request, "Your comment has been updated.")
        return reverse_lazy('post_detail', kwargs={
            'slug': self.object.post.slug})


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    View for deleting a single comment
    """
    model = Comment
    template_name = "comment_delete.html"

    def get_success_url(self):
        messages.success(self.request, "Your comment has been deleted.")
        return reverse_lazy('post_detail', kwargs={
            'slug': self.object.post.slug})


class PostLike(LoginRequiredMixin, UserPassesTestMixin, View):
    """
    View for liking a post. If liked, the view passes the information
    to the template to show the updated icon for confirmation of like
    """
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)

        # Toggle the like status for the user
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        # Redirect to the same URL to avoid issues with refreshing
        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


@login_required
def manage_blogs(request):
    """ Blog management page where the admin can
    add, edit, or delete blogs. Only accessible to superusers. """
    if not request.user.is_superuser:
        return HttpResponseNotFound(render(request, 'errors/403.html'))

    query = request.GET.get('q')

    if query:
        blogs = Post.objects.filter(Q(title__icontains=query)).distinct()
    else:
        blogs = Post.objects.all()

    return render(request, 'blog/manage_blogs.html', {'blogs': blogs})


@login_required
def bulk_delete_blogs(request):
    """ Bulk delete blog items from Blog management page """
    if not request.user.is_superuser:
        return HttpResponseNotFound(render(request, 'errors/403.html'))

    if request.method == 'POST':
        selected_blog_slugs = request.POST.getlist('selected_blogs')
        Post.objects.filter(slug__in=selected_blog_slugs).delete()

        messages.success(request, "Blog(s) successfully deleted!")
    return redirect('manage_blogs')
