from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages
# Create your views here.
def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing_name= request.POST['rahul']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contaced = Contact.objects.all().filter(listing_id = listing_id, user_id =user_id)
            if has_contaced:
                messages.error(request, 'you have already made an requeset')
                return redirect('/listings/'+ listing_id)

        contact = Contact(listing=listing_name, listing_id=listing_id, name=name, email=email, phone=phone, message=message, user_id=user_id)
        contact.save()
        messages.success(request, "your request has been submitted a realtor will get back to you")
        return redirect('/listings/'+ listing_id)




