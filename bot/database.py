import os
import sys
import django
import asyncio
from asgiref.sync import sync_to_async

# Добавляем путь к проекту
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

# Указываем путь к настройкам Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'admin_panel.admin_panel.settings')

django.setup()

from admin_panel.apps.models import Restaurant

@sync_to_async
def get_restaurants():
    return list(Restaurant.objects.all())

print(get_restaurants())
