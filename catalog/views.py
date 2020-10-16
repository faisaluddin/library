from django.shortcuts import render
from django.views import generic
from catalog.models import Book, Author, BookInstance, Genre


def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(
        status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    num_genre = Genre.objects.count()
    harry = Book.objects.filter(title__icontains='harry').count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_genre': num_genre,
        'harry': harry,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


class BookListView(generic.ListView):
    model = Book
    template_name = 'book_list.html'
    paginate_by = 2

    def get_queryset(self):
        return super().get_queryset()  # override the query set here if required

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["extra_data"] = 'This is extra data'
        return context


class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'book_detail.html'


class AuthorListView(generic.ListView):
    model = Author
    template_name = 'author_list.html'


class AuthorDetailView(generic.DetailView):
    model = Author
    template_name = 'author_detail.html'
