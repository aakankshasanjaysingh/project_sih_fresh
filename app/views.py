
from django.shortcuts import render, redirect
from django.http import HttpResponse



from .forms import RequestForm
from .models import Request

def create_request(request):
    if request.method == 'POST':
        form = RequestForm(request.POST, request.FILES)
        if form.is_valid():

            user_data = Request(
                title = form.cleaned_data['title'],
                description = form.cleaned_data['description'],
                pdf = request.FILES['pdf'],
                agency_name = form.cleaned_data['agency_name'],
                video_name = form.cleaned_data['video_name']
            )
            user_data.save()
            return HttpResponse('<p>success</p>')  # You can specify a success URL

            
            
            #return HttpResponse(str(form.cleaned_data['title']))
            #return redirect('success')  # You can specify a success URL

    else:
        form = RequestForm()
    return render(request, 'request_form.html', {'form': form})

# Create your views here.
