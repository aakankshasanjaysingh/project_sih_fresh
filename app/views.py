from django.shortcuts import render, redirect,HttpResponse
from .forms import RequestForm

def create_request(request):
    if request.method == 'POST':
        form = RequestForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print()
            #return HttpResponse(str(form.cleaned_data['title']))
            #return redirect('success')  # You can specify a success URL
    else:
        form = RequestForm()
    return render(request, 'request_form.html', {'form': form})

# Create your views here.
