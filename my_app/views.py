from django.shortcuts import render, redirect
from .models import Pet, Toy
from .forms import FeedingForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class Home(LoginView):
    template_name = 'home.html'

def about(request):
    return render(request, 'about.html')

@login_required
def pet_index(request):
    pets = Pet.objects.filter(user=request.user)
    return render(request, 'pets/index.html', {'pets': pets})

@login_required
def pet_detail(request, pet_id):
    pet = Pet.objects.get(id=pet_id)
    toys_pet_doesnt_have = Toy.objects.exclude(id__in = pet.toys.all().values_list('id'))
    feeding_form = FeedingForm()
    return render(request, 'pets/detail.html', {'pet': pet, 'feeding_form': feeding_form, 'toys': toys_pet_doesnt_have})

@login_required
def add_feeding(request, pet_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.pet_id = pet_id
        new_feeding.save()
    return redirect('pet_detail', pet_id=pet_id)

@login_required
def associate_toy(request, pet_id, toy_id):
    Pet.objects.get(id=pet_id).toys.add(toy_id)
    return redirect('pet_detail', pet_id=pet_id)

@login_required
def remove_toy(request, pet_id, toy_id):
    Pet.objects.get(id=pet_id).toys.remove(toy_id)
    return redirect('pet_detail', pet_id=pet_id)

class PetCreate(LoginRequiredMixin, CreateView):
    model = Pet
    fields = ['name', 'type', 'description', 'age']
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class PetUpdate(LoginRequiredMixin, UpdateView):
    model = Pet
    fields = ['description', 'age']
    
class PetDelete(LoginRequiredMixin, DeleteView):
    model = Pet
    success_url = '/pets/'

class ToyCreate(LoginRequiredMixin, CreateView):
    model = Toy
    fields = '__all__'

class ToyList(LoginRequiredMixin, ListView):
    model = Toy

class ToyDetail(LoginRequiredMixin, DetailView):
    model = Toy
    
class ToyUpdate(LoginRequiredMixin, UpdateView):
    model = Toy
    fields = ['name', 'color']
    
class ToyDelete(LoginRequiredMixin, DeleteView):
    model = Toy
    success_url = '/toys/'

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('pet_index')
        else:
            error_message = 'Could not sign up - please try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)