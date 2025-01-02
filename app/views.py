from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact,Projects,Gallery
from .forms import Galleryform,Projectform
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from .models import Feedback 
from .forms import FeedbackForm
# Create your views here.


def registration(request):
    if not request.user.is_authenticated:

        if request.method == "POST":
            username = request.POST.get('username')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')
            password = request.POST.get('password')

            # Validation checks
            if not username or not first_name or not last_name or not email or not password:
                messages.error(request, 'Please fill in all the required fields')
                return redirect('register')

            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists. Please choose a different one')
                return redirect('register')

            if User.objects.filter(email=email).exists():
                messages.error(request, "Email already exists")
                return redirect('register')

            # Create the user
            user = User.objects.create_user(
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=password
            )

            # Authenticate and log the user in
            user = authenticate(request, username=username, password=password)
            if user is not None:
                print("Authentication successful.")
                login(request, user)
                messages.success(request, 'Registration successful. You are now logged in.')
                return redirect('home')
            else:
                print("Authentication failed.")
                messages.error(request, 'Authentication failed. Please try again.')
                return redirect('register')


        return render(request, 'registration.html')
    else:
        return redirect('home')



from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password

def login_page(request):
    error = None
    if request.method == 'POST':
        email = request.POST.get('email')
        
        password = request.POST.get('password')

        # Ensure user exists before attempting password verification
        try:
            user = User.objects.filter(email=email)
           
            if user.count() == 1:
                user = user.first()
            elif user.count() > 1:
    # Handle duplicate emails
                error="Multiple accounts found with this email. Please contact support."
                return redirect('login')
            else:
              error="No account found with this email."
              return redirect('login')

            # print(user.email)
        except User.DoesNotExist:
            messages.error(request,"User does not exist") 
            return render(request, 'login.html')

        # Verify the password manually
        if check_password(password, user.password):
            login(request, user)
            return redirect('home')  # Redirect to the desired page after login
        else:
            error = "Your email or password is incorrect"

    context = {
        'error': error
    }
    return render(request, 'login.html', context)



def logout_page(request):
    if request.user.is_authenticated:
        logout(request)  
    return redirect('login')  
def home(request):
    return render(request, 'home.html')

def blog(request):
    return render(request, 'blog.html')


def gallary(request):
    photos=Gallery.objects.all()
    return render(request, 'gallary.html',{'photos':photos})

def project(request):
    
    return render(request, 'project.html',{'project':project})

def detailproject(request):
    project=Projects.objects.all()
    return render(request, 'detailproject.html',{'project':project})

def privacy(request):
    return render(request, 'privacy.html')

def termscondition(request):
    return render(request, 'termscondition.html')

def aboutus(request):
    return render(request, 'aboutus.html')

def contact(request):
    if request.method == 'POST':
        
        name = request.POST.get('name')
        print(name)
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        company = request.POST.get('company')
        country = request.POST.get('country')
        job_title = request.POST.get('jobTitle')
        job_details = request.POST.get('jobDetails')

        
        Contact.objects.create(
            name=name,
            email=email,
            phone=phone,
            company=company,
            country=country,
            job_title=job_title,
            job_details=job_details
        )
        messages.success(request, "Thank you for contacting us! We'll get back to you soon.")
        return redirect('contact')

    return render(request, 'contact.html')


def add_project(request):
    if request.method == 'POST':
        form = Projectform(request.POST, request.FILES)  # Include request.FILES for image upload
        if form.is_valid():
            property = form.save(commit=False)
            
            
            property.save()
            return redirect('home')  # Redirect to avoid resubmission on page refresh
    else:
        form = Projectform()
    return render(request, 'add_projects.html', {'form': form})


    

def add_photos(request):
    if request.method == 'POST':
        form = Galleryform(request.POST, request.FILES)  
        if form.is_valid():
            property = form.save(commit=False)
            property.save()
            return redirect('home')  
    else:
        form = Galleryform()
    return render(request, 'add_photos.html', {'form': form})

def allproject(request):
    project=Projects.objects.all()
    return render(request,'allproject.html',{'project':project})

def updateproject(request,id):
    project=Projects.objects.get(id=id)
    if request.method == "POST":
      
        form = Projectform(request.POST, instance=project)
        if form.is_valid():
            updated_project= form.save(commit=False)
            
           
            
            updated_project.save()
            return redirect('home')  # Redirect to the seller dashboard
            
    else:
        form = Projectform(instance=project)
    
    context = {
        'form': form
    }
    return render(request, 'update_project.html', context)

def manageproject(request):
    property=Projects.objects.all()
    contacts=Contact.objects.all()
    return render(request,'manageproject.html',{'property':property,'contacts':contacts})


def deleteproject(request, id):
    message=""
    # Get the property instance by ID and ensure it belongs to the current user
    property = Projects.objects.get( id=id)
    if request.method == "POST":
        # Delete the property
        property.delete()
        message="Property  deleted successfully"
        return redirect('home')  

    context = {
        'property': property,
        message:""
    }
    return render(request, context) # type: ignore

from django.shortcuts import render
from .models import Contact

def view_messages(request):
    # Fetch all contact messages
    messages = Contact.objects.all()
    return render(request, 'view_messages.html', {'messages': messages})

def gallerydetail(request):
    photos=Gallery.objects.all()
    return render(request, 'gallerydetail.html',{'photos':photos})

def feedback_view(request):
    # Fetch the 3 most recent feedbacks in descending order of submission date
    recent_feedbacks = Feedback.objects.order_by('-date_submitted')[:3]

    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = FeedbackForm()

    return render(request, 'feedback.html', {'form': form, 'recent_feedbacks': recent_feedbacks})

	
def feedback_success_view(request): 
	return render(request, 'feedback_success.html')