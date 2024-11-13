from django.shortcuts import render
from django.core.paginator import Paginator
from flower.models import Part

def list_page_view(request):
    query = request.GET.get('q', '')
    search_type = request.GET.get('search_type', 'contains')
    
    min_length = request.GET.get('min_length')
    max_length = request.GET.get('max_length')
    
    min_thickness = request.GET.get('min_thickness')
    max_thickness = request.GET.get('max_thickness')
    
    min_diameter = request.GET.get('min_diameter')
    max_diameter = request.GET.get('max_diameter')
    
    min_weight = request.GET.get('min_weight')
    max_weight = request.GET.get('max_weight')
    
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')

    selected_materials = request.GET.getlist('materials')

    parts = Part.objects.all()

    # Filter by name
    if query:
        if search_type == 'contains':
            parts = parts.filter(name__icontains=query)
        elif search_type == 'starts_with':
            parts = parts.filter(name__istartswith=query)

    # Filter by length
    if min_length:
        parts = parts.filter(length__gte=int(min_length))
    if max_length:
        parts = parts.filter(length__lte=int(max_length))

    # Filter by thickness
    if min_thickness:
        parts = parts.filter(thickness__gte=int(min_thickness))
    if max_thickness:
        parts = parts.filter(thickness__lte=int(max_thickness))

    # Filter by diameter
    if min_diameter:
        parts = parts.filter(diameter__gte=int(min_diameter))
    if max_diameter:
        parts = parts.filter(diameter__lte=int(max_diameter))

    # Filter by weight
    if min_weight:
        parts = parts.filter(weight__gte=float(min_weight))
    if max_weight:
        parts = parts.filter(weight__lte=float(max_weight))

    # Filter by price
    if min_price:
        parts = parts.filter(price__gte=float(min_price))
    if max_price:
        parts = parts.filter(price__lte=float(max_price))

    # Filter by selected materials
    if selected_materials:
        parts = parts.filter(material__in=selected_materials)

    # Pagination
    paginator = Paginator(parts, 10)
    page_number = request.GET.get('page', 1)
    paginated_parts = paginator.get_page(page_number)

    # Get unique materials for the dropdown
    all_materials = Part.objects.values_list('material', flat=True).distinct()

    context = {
        'page_title': "Детали",
        'items': paginated_parts,
        'query': query,
        'search_type': search_type,
        'min_length': min_length,
        'max_length': max_length,
        'min_thickness': min_thickness,
        'max_thickness': max_thickness,
        'min_diameter': min_diameter,
        'max_diameter': max_diameter,
        'min_weight': min_weight,
        'max_weight': max_weight,
        'min_price': min_price,
        'max_price': max_price,
        'selected_materials': selected_materials,
        'all_materials': all_materials,
    }

    return render(request, 'page.html', context)
