from django.shortcuts import redirect, render
from deneme.forms import ContactForm
from deneme.models import contactModel

def contact(request):
    form=ContactForm()
    print(request.POST)
    if request.method == 'POST':
        form= ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
        else:
            print('no valid')
    context={
        'form': form
    }
    return render(request,'pages/contact.html', context=context)