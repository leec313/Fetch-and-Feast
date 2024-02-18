from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q, Avg
from django.db.models.functions import Lower
from django.views.generic import DeleteView, UpdateView
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.http import HttpResponseNotFound

from .models import Product, Category, Rating
from checkout.models import Order
from .forms import ProductForm, RatingForm, CategoryForm
from profiles.models import UserProfile


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            elif sortkey == 'category':
                sortkey = 'category__name'
            elif sortkey == 'rating':
                # Annotate queryset with average rating based on Rating model
                products = products.annotate(avg_rating=Avg('rating__score'))
                sortkey = 'avg_rating'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(
                name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    # Calculate average rating for each product
    for product in products:
        product.average_rating = product.average_rating()

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)
    ratings = Rating.objects.filter(product=product).order_by("-created_on")
    user_has_purchased_product = False

    if request.user.is_authenticated:
        # Check if the user has any order line item for the given product
        user_orders = Order.objects.filter(
            user_profile=request.user.userprofile)
        for order in user_orders:
            if order.lineitems.filter(product=product).exists():
                user_has_purchased_product = True
                break

    # Paginate the ratings
    paginator = Paginator(ratings, 6)
    page = request.GET.get('page')

    try:
        ratings = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        ratings = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        ratings = paginator.page(paginator.num_pages)

    if request.method == 'POST':
        if request.user.is_authenticated:
            # Check if the user has already rated the product
            if not Rating.objects.filter(
                  user=request.user, product=product).exists():
                form = RatingForm(request.POST)
                if form.is_valid():
                    rating = form.save(commit=False)
                    rating.user = request.user
                    rating.product = product
                    # Check if the 'score' field is empty
                    if form.cleaned_data['score']:  # If not empty
                        rating.score = form.cleaned_data['score']
                    else:
                        messages.error(request, 'Please select a star rating!')
                        return redirect(
                            reverse('product_detail', args=[product_id]))
                    rating.save()
                    messages.success(request, 'Rating added successfully!')
                else:
                    messages.error(request, 'Invalid rating.')
            else:
                messages.error(request, 'You have already rated this product.')
        else:
            messages.error(
                request, 'You need to be logged in to submit a rating.')
        return redirect(reverse('product_detail', args=[product_id]))
    else:
        form = RatingForm()

    # Get profile images for each rating user
    rating_profiles = {}
    for rating in ratings:
        user_profile = UserProfile.objects.filter(
            user_id=rating.user.id).first()
        if user_profile and user_profile.profile_image:
            profile_image_url = user_profile.profile_image.url
        else:
            profile_image_url = None
        rating_profiles[rating.user.id] = profile_image_url

    context = {
        'product': product,
        'ratings': ratings,
        'average_rating': product.average_rating(),
        'form': form,
        'rating_profiles': rating_profiles,
        'user_has_purchased_product': user_has_purchased_product,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def manage_products(request):
    """ Product management page where the admin can
    add, edit, search or delete products. Only superusers"""
    if not request.user.is_superuser:
        return HttpResponseNotFound(render(request, 'errors/403.html'))

    query = request.GET.get('q')

    if query:
        products = Product.objects.filter(
            Q(name__icontains=query) |  # Search product name
            Q(sku__icontains=query) |   # Search SKU
            Q(category__name__icontains=query)  # Search category name
        ).distinct()  # Ensure distinct results
    else:
        products = Product.objects.all()
    category_form = CategoryForm()  # Instantiate an empty CategoryForm

    return render(
        request, 'products/manage_products.html', {
            'products': products, 'category_form': category_form})


@login_required
def add_category(request):
    """
    View to add a new category.

    Allows authenticated users to add a new category.
    The category name is manipulated from the friendly name
    and saved in lowercase with underscores instead of spaces.
    """
    if not request.user.is_superuser:
        return HttpResponseNotFound(render(request, 'errors/403.html'))

    if request.method == 'POST':
        category_form = CategoryForm(request.POST)
        if category_form.is_valid():
            # Extract the friendly name from the form
            friendly_name = category_form.cleaned_data['friendly_name']
            # Manipulate the friendly name to get the category name
            manipulated_name = friendly_name.lower().replace(' ', '_')
            # Check if a category with the same name exists
            if Category.objects.filter(name=manipulated_name).exists():
                # Display an error message if the category already exists
                messages.error(
                    request, f'A category with the name\
                        "{friendly_name}" already exists.')
            else:
                # Save the form but commit=False to get the instance
                category = category_form.save(commit=False)
                # Set the manipulated category name
                category.name = manipulated_name
                # Save the manipulated instance to the database
                category.save()
                # Display a success message
                messages.success(request, f'Category\
                    "{friendly_name}" added successfully.')
                # Redirect to the manage products page
                return redirect('manage_products')
    else:
        category_form = CategoryForm()

    # Get all products for rendering in the template
    products = Product.objects.all()

    # Render the add category template with the form and products
    return render(
        request,
        'products/manage_products.html',
        {'products': products, 'category_form': category_form}
    )


@login_required
def bulk_delete_products(request):
    """
    Allows bulk/single deletion of products
    """
    if not request.user.is_superuser:
        return HttpResponseNotFound(render(request, 'errors/403.html'))

    if request.method == 'POST':
        selected_product_ids = request.POST.getlist('selected_products')
        Product.objects.filter(id__in=selected_product_ids).delete()
        messages.success(request, 'Successfully deleted product(s)!')
    return redirect('manage_products')


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        return HttpResponseNotFound(render(request, 'errors/403.html'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            # Add a message to inform the user
            message = "Your post was created successfully!\
                <a href='{}'>Create another product</a>".format(
                    reverse('add_product'))
            messages.success(request, mark_safe(message))
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request, 'Failed to add product. Ensure the form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        return HttpResponseNotFound(render(request, 'errors/403.html'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request, 'Failed to update product. Ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store with confirmation """
    if not request.user.is_superuser:
        return HttpResponseNotFound(render(request, 'errors/403.html'))

    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        # User confirmed deletion
        product.delete()
        messages.success(request, 'Product deleted!')
        return redirect(reverse('products'))

    return render(
        request, 'products/confirm_delete.html', {'product': product})


class RatingUpdateView(UpdateView, LoginRequiredMixin, UserPassesTestMixin):
    """
    View for updating a single rating
    """
    model = Rating
    template_name = "edit_rating.html"
    fields = ['title', 'body', 'score']

    def get_success_url(self):
        messages.success(self.request, "Your rating has been updated.")
        return reverse_lazy('product_detail', kwargs={
            'product_id': self.object.product.id})

    # Pass the form context here
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = RatingForm(instance=self.object)
        return context


class RatingDeleteView(DeleteView, LoginRequiredMixin, UserPassesTestMixin):
    """
    View for deleting a single rating
    """
    model = Rating
    template_name = "delete_rating.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product'] = self.get_object().product
        return context

    def get_success_url(self):
        rating = self.get_object()  # Get the rating object being deleted
        product_id = rating.product.id  # Get the ID of the associated product
        messages.success(self.request, "Your rating has been deleted.")
        return reverse_lazy(
            'product_detail', kwargs={'product_id': product_id})
