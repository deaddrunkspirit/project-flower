import os
import random
from faker import Faker
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'flower.settings')  
django.setup()

from flower.models import Part  

fake = Faker()

def create_mock_data(num_rows=100):
    for _ in range(num_rows):
        mat = ['Сталь', 'Алюминий', 'Нержавеющая сталь']
        p = [0.008, 0.0027, 0.0077]
        prices = [20, 140, 52]
        choice = random.choice([0,1,2])
        
        _material=mat[choice]
        _diameter=round(random.uniform(11, 100), 2)
        _thickness=round(random.uniform(1, 5), 2)
        _length=random.choice([6, 12])
        _name = f'Труба {_material} {int(_diameter)} мм'
        _weight=int(3.14 * (_diameter - _thickness) * _thickness * _length * p[choice])
        _price = prices[choice]*_weight
        part = Part(
            name=_name,
            material=_material,
            diameter=int(_diameter),
            length=int(_length),
            weight=int(_weight),
            price = int(_price),
            thickness=int(_thickness),
            created_at=fake.date_between(start_date='-5y', end_date='today')
        )
        part.save()

if __name__ == "__main__":
    create_mock_data(100)

