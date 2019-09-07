from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'mainapp/homePage.html')

def contact(request):
    return render(request, 'mainapp/basic.html', {'values':['Если у вас остались вопросы то звоните по телефону', '12345678', 'example@mail.ru']})
