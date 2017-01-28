from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib import messages

from .forms import LoginForm, RegisterForm
# Create your views here.
def user_login(request):
	
	if request.method == 'POST':
		#do some authentication stuff login as stay on the page
		login_form = LoginForm(request.POST)
		
		if login_form.is_valid():
			cleaned_form_data = login_form.cleaned_data
			user = authenticate(username = cleaned_form_data['username'],
								password = cleaned_form_data['password'])
			if user is not None:
				#proceed to login if active
				if user.is_active:
					login(request,user)
					#return HttpResponse('Successfully Logged In')
					messages.success(request,'Login successfull')
				else:
					return HttpResponse('Inactive User')

			else:
				return HttpResponse('Invalid Login')

	else:
		login_form = LoginForm()

	template = 'accounts/login.html'		
	context = {'form':login_form,}
	return render(request,template,context)

def register(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			new_user = form.save(commit = False)
			password = form.cleaned_data['password']
			new_user.set_password(password)				
			new_user.save()
			return render(request,'accounts/reg_success.html',{'new_user':new_user,})

	else:
		form = RegisterForm()
		template = 'accounts/register.html'
		context = {'form':form,}
		return render(request,template,context)

def test_context(request):

	message = "The message being serdver globally"


	return {'msg':message,}