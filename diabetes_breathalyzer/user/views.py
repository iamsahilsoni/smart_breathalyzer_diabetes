from django.shortcuts import render , reverse , redirect 
from user.models import patient
from django.conf import settings


# Create your views here.
def login(request):
	if 'userid' in request.session:
		del request.session['userid']
	if request.method == 'POST':
		userid=request.POST['userid']
		password=request.POST['password']
		print(userid)

		user_patient = patient.objects.get(p_userid = userid)
		print(user_patient)
		if user_patient:
			if user_patient.p_pass==password:
				request.session['userid'] = userid;
				return redirect('pdashboard')
				# return redirect('/student/dashboard')

	return render(request,'user/login.html')

def dashboard(request):
	if 'userid' not in request.session:
		return redirect(reverse('plogin'))	
	else:	
		user_patient=patient.objects.get(p_userid=request.session['userid'])

		# print("^^^^^^^^^^^" + s.s_name)
		return render(request,'user/dashboard.html',{ 'user_patient': user_patient })


def logout(request):
	try:
		del request.session['userid']
	except KeyError:
		pass 
	return redirect(reverse('plogin'))	


def profile(request):
	if 'userid' not in request.session:
		return redirect(reverse('plogin'))
	user_patient=patient.objects.get(p_userid=request.session['userid'])
	
	if 	request.method == 'POST' :
		user_patient.p_name=request.POST['name']
		user_patient.p_email=request.POST['email']
		user_patient.p_ph=request.POST['phone']
		user_patient.p_gender=request.POST['gender']
		user_patient.p_diabetic=request.POST['diabetic']
		user_patient.save()
		
	return render(request ,'user/profile.html' , {'user_patient' : user_patient })


def  change_pass(request):
	if 'userid' not in request.session:
		return redirect(reverse('plogin'))

	user_patient=patient.objects.get(p_userid=request.session['userid'])
	password=user_patient.p_pass
	if request.method == 'POST':
		old_pass=request.POST['old_password']
		new_pass=request.POST['new_password']
		conf_pass = request.POST['conf_pass']

		if old_pass==password and new_pass==conf_pass:
			user_patient.p_pass=new_pass
			user_patient.save()

	return render(request , 'user/profile.html', {'user_patient' : user_patient})	

def prev_readings(request):
	if 'userid' not in request.session:
		return redirect(reverse('plogin'))
	user_patient=patient.objects.get(p_userid=request.session['userid'])
		
	return render(request ,'user/prev-readings.html' , {'user_patient' : user_patient })


