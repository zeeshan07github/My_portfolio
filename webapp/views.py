from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import posts , tags
from .forms import *
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
# Create your views here.

def home(request):
    post = posts.objects.all()[0:3]
    return render(request , 'webapp/home.html',{'posts':post})

def profile(request):
    return  render(request , 'webapp/profile.html')

# Replace with your actual model


def Posts(request):
    items_per_page = 3  # Define how many items per page you want to display
    search_query = request.GET.get('q', '')  # Get the search query from the URL parameter

    # Filter posts based on both headlines and tags
    queryset = posts.objects.all()
    if search_query:
        queryset=queryset.filter( Q(tags__name__icontains=search_query))

    queryset = queryset.distinct()
    paginator = Paginator(queryset, items_per_page)
    page = request.GET.get('page')  # Get the current page number from the request
    items = paginator.get_page(page)

    return render(request, 'webapp/post.html', {'items': items, 'search_query': search_query})



def Post(request , pk):
    post= posts.objects.get(id=pk)
    # tag = tags.objects.all()
    return  render(request , 'webapp/posts.html' ,{'post':post })

@login_required(login_url='home')
def create_post(request):
    form = createForm()
    if request.method == 'POST':
        form = createForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            return redirect('posts')
    else:
        form = createForm()
    return render(request , 'webapp/post_form.html' , {'form': form})

@login_required(login_url='home')
def edit_post(request , pk):
    post = posts.objects.get(id=pk)
    form = createForm(instance=post)
    if request.method == 'POST':
        form = createForm(request.POST , request.FILES , instance=post)
        if form.is_valid():
            form.save()
        return redirect('posts')
    
    return render(request , 'webapp/post_form.html' , {'form': form})

def delete(request , pk):
    post = posts.objects.get(id=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('posts')
    return render(request , 'webapp/delete.html' , {'item': post} )


def submit_form(request):
    if request.method == 'POST':
        # Gather the form data
        name = request.POST['name']
        subject = request.POST['subject']
        email = request.POST['email']
        message = request.POST['message']

        # Create a dictionary with the form data
        context = {
            'name': name,
            'subject': subject,
            'email': email,
            'message': message,
        }

        # Render the email template with the context data
        email_message = render_to_string('webapp/email.html', context)

        # Create an EmailMessage instance and send it
        email = EmailMessage(
            subject,
            email_message,
            settings.EMAIL_HOST_USER,
            ['saloo9615@gmail.com'],  # Receiver's email
        )

        try:
            email.send()
            return HttpResponse('Thank you for your message. We will get back to you shortly.')
        except Exception as e:
            # Handle the exception, e.g., log the error
            return HttpResponse('Sorry, there was an error sending your message. Please try again later.')

    return HttpResponse('Method not allowed')
