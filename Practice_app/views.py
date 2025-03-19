from django.shortcuts import render
from .models import MyModel

def my_view(request):
    my_models = MyModel.objects.all()
    return render(request, 'my_template.html', {'my_models': my_models})
