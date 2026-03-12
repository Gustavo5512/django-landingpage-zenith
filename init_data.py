import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'zenith_portfolio.settings')
django.setup()

from core.models import Categoria
from django.contrib.auth.models import User

# Criar Categorias
Categorias = [
    ('E-commerce', 'e-commerce'),
    ('Sistemas Internos', 'sistemas-internos'),
    ('Dashboards', 'dashboards'),
]

for nome, slug in Categorias:
    Categoria.objects.get_or_create(nome=nome, slug=slug)
    print(f"Categoria {nome} criada/já existe.")

# Criar Superusuário
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@zenith.com', 'admin123')
    print("Superusuário admin criado (senha: admin123).")
else:
    print("Superusuário admin já existe.")
