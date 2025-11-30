from django.shortcuts import render

# Create your views here.
def user_signup_page(request):
    name = request.GET.get('name')
    password = request.GET.get('password')
    print(f'name is {name} and password is {password}')
    return render(request, 'adduser/adduser.html')