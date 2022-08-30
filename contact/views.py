from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm

# Create your views here.
def contact(request):
     contact_form = ContactForm()
     
     if request.method == 'POST':
          contact_form = ContactForm(data=request.POST)
          if contact_form.is_valid():
               name = request.POST.get('name', '')
               email = request.POST.get('email', '')
               content = request.POST.get('content', '')
               # Si todo sale bien, redireccionamos
               # Enviamos al correo y redireccionar
               email = EmailMessage(
                    #Asunto
                    "Proyecto Django: Nuevo Mensaje", 
                    # Cuerpo
                    "De {} <{}>\n\nEscribió:\n\n{}".format(name, email, content), 
                    # Email Origen
                    "no-contestar@inbox.mailtrop.io",
                    ["chchema26@gmail.com"],
                    # Email Destino
                    reply_to=[email]
               )
               
               try:
                    email.send()
                    # Si salió bien
                    return redirect(reverse('contact') + "?ok")
               except:
                    # Algo salió mal
                    return redirect( reverse('contact')+"?fail" )     
     return render(request, 'contact/contact.html', {'form':contact_form})