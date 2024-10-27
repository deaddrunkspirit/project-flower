from django.http import HttpResponse
from flower.models import Part
import datetime

def home(request):
    parts = Part.objects.all()
    parts_str = ''
    for part in parts:
        parts_str += get_full_part_layout(part)

    layout = f'''
        <main>
            <h1 style="padding:30px;">Parts</h1> 
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

