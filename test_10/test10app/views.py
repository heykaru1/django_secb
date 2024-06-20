from django.shortcuts import render, redirect
from .models import Gender, User, Activities, Incomplete
from django.contrib import messages
from django.contrib.auth.hashers import make_password


# Create your views here.
def index_main(request):
    return render(request, 'include/main.index.html')

def index_gender(request):
    genders= Gender.objects.all()# SELECT * FROM genders
    
    context = {
        'genders': genders
    }
    
    return render(request, 'gender/index.html', context)

def create_gender(request):
    return render(request, 'gender/create.html')

def store_gender(request):
    gender = request.POST.get('gender')
    Gender.objects.create(gender=gender) #INSERT INTO genders(gender) VALUES(gender)
    messages.success(request,'Gender successfully saved!')
    return redirect('/genders')

def show_gender(request, gender_id):
    gender = Gender.objects.get(pk=gender_id) # SELECT * FORM GENDER WHERE gender_id = gender_id
    
    context = {
        'gender': gender,
    }
    return render(request, 'gender/show.html', context) 

def edit_gender(request, gender_id):
    gender = Gender.objects.get(pk=gender_id)
    
    context = {
        'gender': gender,
    }
    return render(request, 'gender/edit.html', context) 

def update_gender(request, gender_id):
    gender = request.POST.get('gender')
    
    Gender.objects.filter(pk=gender_id).update(gender=gender) 
    messages.success(request, 'Gender successfully updated.')
    
    return redirect('/genders')

def delete_gender(request, gender_id):
    gender =  Gender.objects.get(pk=gender_id)
   
    context = {
        'gender': gender,
    }
    
    return render(request, 'gender/delete.html', context) 

def destroy_gender(request, gender_id):
    Gender.objects.filter(pk=gender_id).delete()
    messages.success(request, 'Gender is successfully deleted.')
    
    return redirect('/genders')


#
#incomplete section
def index_incomplete(request):
    incomplete = Incomplete.objects.all()# SELECT * FROM genders
    
    context = {
        'incomplete': incomplete
    }
    
    return render(request, 'incomplete/index.html', context)

def create_incomplete(request):
    incomplete = Incomplete.objects.all()
    return render (request, 'incomplete/create.html', {'incomplete': incomplete})

def store_incomplete(request):
    incomplete = request.POST.get('incomplete')
    Incomplete.objects.create(incomplete=incomplete) 
    messages.success(request,'Activty successfully saved!')
    return redirect('/incompletes')
  
def show_incomplete(request, inc_id):
    incomplete = Incomplete.objects.get(pk=inc_id) 
    
    context = {
        'incomplete': incomplete,
    }
    return render(request, 'incomplete/show.html', context) 

def edit_incomplete(request, inc_id):
    incomplete = Incomplete.objects.get(pk=inc_id)
    
    context = {
        'incomplete': incomplete,
    }
    return render(request, 'incomplete/edit.html', context)

def update_incomplete(request, inc_id):
    incomplete = request.POST.get('incomplete')
    
    Incomplete.objects.filter(pk=inc_id).update(incomplete=incomplete) 
    messages.success(request, 'incomplete successfully updated.')
    
    return redirect('/incompletes')

def delete_incomplete(request, inc_id):
    incomplete =  Incomplete.objects.get(pk=inc_id)
   
    context = {
        'incomplete': incomplete,
    }
    
    return render(request, 'incomplete/delete.html', context)

def destroy_incomplete(request, inc_id):
    Incomplete.objects.filter(pk=inc_id).delete()
    messages.success(request, 'Activity is successfully deleted.')
    
    return redirect('/incompletes')






def show_user(request, user_id):
    user = User.objects.get(pk=user_id) # SELECT * FORM GENDER WHERE gender_id = gender_id
    
    context = {
        'user': user,
    }
    return render(request, 'user/show.html', context) 

def edit_user(request, user_id):
    user = User.objects.get(pk=user_id)
    genders = Gender.objects.all()
    
    context = {
        'user': user,
        'genders':genders,
    }
    return render(request, 'user/edit.html', context) 


def update_user(request, user_id):
    firstName = request.POST.get('firstName')
    middleName = request.POST.get('middleName')
    lastName = request.POST.get('lastName')
    genderID =  request.POST.get('gender_id')
    username = request.POST.get('username')
    
    
    User.objects.filter(pk=user_id).update(first_name=firstName, middle_name=middleName, last_name=lastName, gender_id=genderID, username=username) 
    messages.success(request, 'User successfully updated.')
    
    return redirect('/users')


def delete_user(request, user_id):
    user =  User.objects.get(pk=user_id)
   
    context = {
        'user': user,
    }
    
    return render(request, 'user/delete.html', context) 


def destroy_user(request, user_id):
    User.objects.filter(pk=user_id).delete()
    messages.success(request, 'Gender is successfully deleted.')
    
    return redirect('/users')

def index_user(request):
    users = User.objects.select_related('gender')
    
    context = {
        'users':users,
    }
    
    return render(request, 'user/index.html', context)


def create_user(request):
    genders = Gender.objects.all() # SELECT * from genders
    
    context = {
        'genders' : genders,
        
    }
     
    return render(request,'user/create.html', context)

def store_user(request):
    firstName = request.POST.get('first_name')
    middleName = request.POST.get('middle_name')
    lastName = request.POST.get('last_name')
    age = request.POST.get('age')
    birthDate = request.POST.get('birth_date')
    gender = request.POST.get('gender_id')
    username = request.POST.get('username')
    password = request.POST.get('password')
    confirmPassword = request.POST.get('confirm_password')
    
    if password == confirmPassword:
        encryptedPassword = make_password(password)
        
        User.objects.create(first_name=firstName, middle_name=middleName, last_name=lastName, age=age, birth_date=birthDate,gender_id=gender, username=username,password=encryptedPassword)
        
        messages.success(request, 'User successfully saved.')
        return redirect('/users')
    else: 
        messages.error(request, 'Password do not match')
        return redirect('/user/create')




#activities section   
def index_activities(request):
    activities= Activities.objects.all()# SELECT * FROM genders
    
    context = {
        'activities': activities
    }
    
    return render(request, 'activities/index.html', context)

def create_activities(request):
    return render (request, 'activities/create.html')

def store_activities(request):
    activity = request.POST.get('activity')
    description = request.POST.get('description')
    Activities.objects.create(activity=activity,description=description) 

    messages.success(request,'Activty successfully saved!')
    return redirect('/activities')
  
def show_activities(request, act_id):
    activity = Activities.objects.get(pk=act_id) # SELECT * FORM GENDER WHERE gender_id = gender_id
    
    context = {
        'activity': activity,
    }
    return render(request, 'activities/show.html', context) 

def edit_activities(request, act_id):
    activity = Activities.objects.get(pk=act_id)
    
    context = {
        'activity': activity,
    }
    return render(request, 'activities/edit.html', context)

def update_activities(request, act_id):
    activity = request.POST.get('activity')
    description = request.POST.get('description')
    
    Activities.objects.filter(pk=act_id).update(activity=activity,description=description) 
    messages.success(request, 'activity successfully updated.')
    
    return redirect('/activities')

def delete_activities(request, act_id):
    activity =  Activities.objects.get(pk=act_id)
   
    context = {
        'activity': activity,
    }
    
    return render(request, 'activities/delete.html', context)

def destroy_activities(request, act_id):
    Activities.objects.filter(pk=act_id).delete()
    messages.success(request, 'Activity is successfully deleted.')
    
    return redirect('/activities')


