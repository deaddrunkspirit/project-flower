import os
import random
from faker import Faker
import django

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'flower.settings')  # Replace 'flower' with your project name
django.setup()

from flower.models import Part  # Make sure this import matches your app structure

fake = Faker()

def create_mock_data(num_rows=100):
    for _ in range(num_rows):
        part = Part(
            name=fake.word(),
            material=random.choice(['Steel', 'Aluminum', 'Plastic', 'Wood', 'Glass']),
            value=round(random.uniform(1.0, 100.0), 2),
            weight=round(random.uniform(0.1, 50.0), 2),
            created_at=fake.date_between(start_date='-5y', end_date='today')
        )
        part.save()

if __name__ == "__main__":
    create_mock_data(100)

