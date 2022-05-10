from urllib import request
from django.http import HttpResponse
from django.shortcuts import redirect, render

def unauthenticated_user(view_func):
    def wrapper_func(request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard/')
        else:
            return view_func(request,*args,**kwargs)

    return wrapper_func

# for user
def allowed_users(allowed_roles=[]):
	def decorator(view_func):
		def wrapper_func(request, *args, **kwargs):

			group = None
			if request.user.groups.exists():
				group = request.user.groups.all()[0].name

			if group in allowed_roles:
				return view_func(request, *args, **kwargs)
			else:
				return render(request,'403.html')
		return wrapper_func
	return decorator

# for Admin
def admin_only(view_func):        
    def wrapper_function(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
        if group == 'user':
            return redirect('userPage')
        elif group == 'Admin':
            return view_func(request, *args, **kwargs)
        elif group == 'Superadmin':
            return redirect("/admin/")

    return wrapper_function