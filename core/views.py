from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from core.forms import ContactForm
from django.views.generic import CreateView
from django.contrib import messages

def contact(request):
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.success(request, 'message sent !')
            return HttpResponseRedirect("")
    else:
        contact_form = ContactForm()
    context = {
        'form': contact_form,
    }
    return render(request, 'core/contact.html', context)