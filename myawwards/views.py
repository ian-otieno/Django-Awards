import json
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Avg
from rest_framework import serializers, status
from django.http import Http404, HttpResponse, QueryDict, response
from django.shortcuts import (get_list_or_404, get_object_or_404, redirect,
                              render)
from rest_framework.decorators import APIView, api_view
from .forms import EditProfileForm, ProfileUpdateForm, ProjectForm, RatingsForm
from .models import Project, Rating, UserProfile
from .serializers import ProjectSerializer, ProfileSerializer
from rest_framework.response import Response
from rest_framework import viewsets


# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    all_projects = Project.objects.reverse().annotate(
        avg_design = Avg('rating__design'),
        avg_usability = Avg('rating__usability'),
        avg_content=Avg('rating__content'),
       # avg_score = Avg('rating__design', 'rating__usability', 'rating__score')
    )
    return render(request, 'awards/index.html', {"all_projects":all_projects})

def project_detail(request, project_id):
    try:
        project = Project.objects.get(id = project_id)  
    
    except Project.DoesNotExist:
        raise Http404()

    current_user = request.user
    ratings = Rating.objects.all()
    if request.method == 'POST':
        review_form = RatingsForm(request.POST)
        if review_form.is_valid():
            design = review_form.cleaned_data['design']
            usability = review_form.cleaned_data['usability']
            content = review_form.cleaned_data['content']
            review = Rating()
            review.project=project
            review.user = current_user
            review.usability=usability
            review.design=design
            review.content = content
            review.save()

    else:
        review_form = RatingsForm()


    return render(request,"awards/project_detail.html", {"project":project, "review_form": review_form, "ratings":ratings})

@login_required(login_url='/accounts/login/')
def new_project(request):
    current_user =request.user
    if request.method == 'POST':
        project_form = ProjectForm(request.POST,request.FILES)
        if project_form.is_valid():
            project = project_form.save(commit = False)
            project.userprofile = current_user
            project.save()
            return redirect("index")

    else:
        project_form = ProjectForm()
    return render (request, 'awards/new_project.html', {"project_form":project_form})

@login_required(login_url='/accounts/login/')
def delete_project(request, project_id):
    item = Project.objects.get(id =project_id)
    if request.method =='POST':
        item.delete()
        return redirect('/')
    return render(request, 'awards/delete.html', {"item":item})
   
@login_required(login_url='/accounts/login/')
def update_project(request, project_id):
    project = Project.objects.get(id=project_id)
    update_form = ProjectForm(instance=project)
    context = {"update_form": update_form}
    if request.method =="POST":
        update_form = ProjectForm(request.POST, instance = project)
        if update_form.is_valid():
            update_form.save()
            return redirect("/")

    return render (request, 'awards/update_project.html', context)

@login_required(login_url='/accounts/login/')
def profile_view(request):
    user = request.user
    projects = Project.objects.all()
    user = User.objects.get(username = user.username)

    return render (request, 'awards/profile.html', {"user":user, "projects":projects})

@login_required(login_url='/accounts/login/')
def edit_profile(request):
    user = request.user
    if request.method == 'POST':
        user_form=EditProfileForm(request.POST, request.FILES,instance =request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            # messages.success(request, f'Your profile was updated successfuly')
            return redirect('profile')
    else:
        user_form=EditProfileForm(instance =request.user)
        profile_form = ProfileUpdateForm(instance=request.user.userprofile)

        context = {"user_form":user_form, "profile_form":profile_form, "user":user}
        return render(request, 'awards/edit_profile.html', context)

@login_required(login_url='/accounts/login/')
def search(request):
    
    if 'projects' in request.GET and request.GET["projects"]:
        search_term = request.GET.get("projects")
        searched_projects = Project.search_project(search_term)
        message = f"{search_term}"

        return render(request, 'awards/search.html',{"message":message,"projects": searched_projects})

    else:
        message = "You haven't searched for any project"
        return render(request, 'awards/search.html',{"message":message})

def rating(request, project_id):
    user = request.user
    project = Project.objects.get(id=project_id)
    if request.method == 'POST':
        rating_form = RatingsForm(request.POST, request.FILES, instance=project)
        if rating_form.is_valid():
            rating = rating_form.save(commit = False)
            rating.save()
            return redirect('index')
    else:
        rating_form = RatingsForm()

    return render(request, 'awards/rate.html' ,{"user":user, "rating_form":rating_form})

class ProjectList(APIView):
    user = User.objects.all()
    def get(self, request, format=None):
        projects = Project.objects.all()
        serializers = ProjectSerializer(projects, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers=ProjectSerializer(data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)

        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class ProfileList(APIView):
    user = User.objects.all()
    def  get(self, request, format = None):
        profile = UserProfile.objects.all()
        serializers =ProfileSerializer(profile, many=False)
        return Response(serializers.data)


