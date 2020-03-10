from django.shortcuts import render
from django.core.mail import send_mail

def home(request): 
	return render(request, 'home.html', {})

def contact(request): 
	if request.method == "POST":
		# kreiramo promenljive za svako od polja za unos: message-name, message-email, message
		# radi obrade unosa
		message_name = request.POST ['message-name']
		message_email = request.POST ['message-email']
		message =  request.POST ['message']

		# Send mail 
		send_mail(
			'Poruka od: ' + message_name, # subject
			message, # message
			message_email, # from, šalje posetilac sajta
			['momchileto@gmail.com'], # to, šalje doktoru
			fail_silently=False,
			)

		return render(request, 'contact.html', {'message_name': message_name})
	else:
		# nema unosa samo prikaz stranice 	
		return render(request, 'contact.html', {})