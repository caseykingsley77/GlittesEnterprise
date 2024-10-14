from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages

# Create your views here.
def home(request):
    return render (request, 'home/index.html')

def service(request):
    return render (request, 'home/service.html')


def contact(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        subject = request.POST.get('subject', 'No Subject')
        message = request.POST.get('message')

        if fullname and email and message:
            # Build the email content
            message_body = f"Name: {fullname}\nEmail: {email}\n\nMessage:\n{message}"

            try:
                # Send the email to glittesenterprise@gmail.com
                send_mail(
                    subject,  # Subject of the email
                    message_body,  # Message body
                    email,  # From email (user's email)
                    ['Caseykingsley77@gmail.com'],  # To email (recipient)
                    fail_silently=False,
                )
                messages.success(request, "Your message has been sent successfully!")
                return redirect('contact')  # Redirect back to the contact page
            except Exception as e:
                messages.error(request, f"Error sending message: {e}")
        else:
            messages.error(request, "Please fill in all fields.")

    return render(request, 'home/contact.html')
