from django.shortcuts import render


def handler404(request, exception=None):
    """ Error Handler 404 - Page Not Found """
    return render(request, "errors/404.html", status=404)


def faq_view(request):
    return render(request, 'faq.html')