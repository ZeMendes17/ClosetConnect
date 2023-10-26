import os
import django



os.environ.setdefault("DJANGO_SETTINGS_MODULE", "TPW_project_1.settings")


django.setup()

from app.models import User, Product

# Crie o primeiro usuário
user1 = User.objects.create(
    username='joao',
    name='joao',
    email='joao@example.com',
    password='senha1',  # Você deve usar um método seguro para armazenar senhas reais
    admin=False  # Este usuário é um administrador
)

# Crie o segundo usuário
user2 = User.objects.create(
    username='jose',
    name='jose',
    email='jose@example.com',
    password='senha1',  # Você deve usar um método seguro para armazenar senhas reais
    admin=False  # Este usuário não é um administrador
)



user = User.objects.get(id=2)
products = [

    Product(name='Camiseta Estampada', description='Camiseta de algodão estampada', price=29.99, user_id=user),
    Product(name='Tênis Esportivo', description='Tênis esportivo de alta qualidade', price=59.99, user_id=user),
    Product(name='Relógio Elegante', description='Relógio de pulso elegante', price=49.99, user_id=user),
    Product(name='Boné de Beisebol', description='Boné de beisebol clássico', price=14.99, user_id=user),
    Product(name='Mochila Resistente', description='Mochila resistente para viagens', price=39.99, user_id=user),
    Product(name='Sapatos Formais', description='Sapatos de couro para ocasiões formais', price=69.99, user_id=user),
    Product(name='Jaqueta de Inverno', description='Jaqueta quente para inverno', price=79.99, user_id=user),
    Product(name='Calça Jeans Moderna', description='Calça jeans moderna e confortável', price=34.99, user_id=user),
    Product(name='Óculos de Sol Fashion', description='Óculos de sol na moda', price=19.99, user_id=user),
    Product(name='Bolsa Elegante', description='Bolsa elegante para mulheres', price=44.99, user_id=user),
]

for product in products:
    product.save()
