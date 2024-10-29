from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from flower.models import Part
import datetime


def list_page_view(request):
    query = request.GET.get('q', '')
    items = Part.objects.filter(name__icontains=query) if query else Part.objects.all()
    
    paginator = Paginator(items, 10) 
    page_number = request.GET.get('page', 1)
    paginated_items = paginator.get_page(page_number)
    
    context = {
        'page_title': "Parts",
        'items': paginated_items,
        'query': query
    }
    
    return render(request, 'page.html', context)

def home(request):
    parts = Part.objects.all()
    parts_str = ''
    for part in parts:
        parts_str += get_full_part_layout(part)

    layout = f'''
        <main>
            <h1 style="padding:30px;">Parts</h1> 
            <input />
            <ul style="list-style-type:none;">
                <li style="display:flex; flex-direction:row; justify-content:space-evenly;">
                    <p style="font-weight: bold;">Name</p>
                    <p style="font-weight: bold;">Value</p>
                    <p style="font-weight: bold;">Weight</p>
                    <p style="font-weight: bold;">Created At</p>
                </li>
                {parts_str}
            </ul>
        </main>
    '''

    return HttpResponse(layout)
    
def get_full_part_layout(part):
    return f'''
        <li style="display:flex; flex-direction:row; justify-content:space-evenly;padding:30px;">
            <div style="display:block; width:80px;">{part.name}</div>
            <div style="display:block; width:80px;">{part.value}</div>
            <div style="display:block; width:80px;">{part.weight}</div>
            <div style="display:block; width:80px;">{part.created_at}</div>
        </li>
    '''

