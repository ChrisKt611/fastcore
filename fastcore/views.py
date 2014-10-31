from models import authmodels

user=User.objects.create(username='Jhon', password='111')
user_list = User.objects.all()
