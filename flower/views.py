from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from flower.models import Part
import datetime


def list_page_view(request):
    query = request.GET.get('q', '')
    search_type = request.GET.get('search_type', 'contains')
    min_value = request.GET.get('min_value')
    max_value = request.GET.get('max_value')
    min_weight = request.GET.get('min_weight')
    max_weight = request.GET.get('max_weight')

    parts = Part.objects.all()

    if query:
        if search_type == 'contains':
            parts = parts.filter(name__icontains=query)
        elif search_type == 'starts_with':
            parts = parts.filter(name__istartswith=query)

    if min_value:
        parts = parts.filter(value__gte=float(min_value))
    if max_value:
        parts = parts.filter(value__lte=float(max_value))

    if min_weight:
        parts = parts.filter(weight__gte=float(min_weight))
    if max_weight:
        parts = parts.filter(weight__lte=float(max_weight))

    paginator = Paginator(parts, 10)
    page_number = request.GET.get('page', 1)
    paginated_parts = paginator.get_page(page_number)

    context = {
        'page_title': "Parts",
        'items': paginated_parts,
        'query': query,
        'search_type': search_type,
        'min_value': min_value,
        'max_value': max_value,
        'min_weight': min_weight,
        'max_weight': max_weight,
    }

    return render(request, 'page.html', context)
