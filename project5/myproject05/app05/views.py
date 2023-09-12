from django.shortcuts import render,redirect
from .models import UserInput
from .forms import UserInputForm
from django.http import HttpResponse
# Create your views here.

def index(request):
    if request.method == 'POST':
        form = UserInputForm(request.POST)
        if form.is_valid():
            # Process the user input here
            input_data = form.cleaned_data['input_field']
            input_data = form.cleaned_data['input_field1']
            # Save to the database or perform any desired actions
            form.save()  # If you have a model
            #return redirect('success_page',input_data)  # Redirect to a success page
            # return HttpResponse("Data Saved Successfuly.")
        return redirect('/index1/')
            
    else:
        form = UserInputForm()
    
    return render(request, 'index.html', {'form': form})



# views.py in your app

def index1(request):
    if request.method == 'GET':
        product = UserInput.objects.all().values().order_by('-id')
        product_dict = {
            "products": product
        }
        return render(request,'index.html',product_dict)
    



   
