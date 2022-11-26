from django.shortcuts import render,redirect
from .forms import UserRegistrationForm,ProfileUpdateForm
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
UserModel = get_user_model()

# Create your views here.
def Register(request):
    
    if (request.method == "POST"):
        
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your account.'
            
            message = render_to_string('accounts/acc_active_email.html', 
            {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            }
                                       )

            to_email = form.cleaned_data.get('email')
            email = EmailMessage(mail_subject, message, to=[form.cleaned_data.get("email")])
            email.send()
            return render(request,'accounts/activate_account_confirm.html')
    
    else:
        form=UserRegistrationForm()

    return render(request,"accounts/register.html",{'form':form})


def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = UserModel._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    
    if (user is not None and default_token_generator.check_token(user, token)):
        user.is_active = True
        user.save()
        return render(request,'accounts/activate_account_done.html')
    else:
        return HttpResponse('Activation link is invalid!')
        user.delete()

def Profile(request):
    return render(request,"accounts/profile.html")

@login_required
def profile(request):
    if request.method=="POST":
        p_form=ProfileUpdateForm(request.POST,instance=request.user.profile)
    else:
        
        p_form=ProfileUpdateForm(request.POST,instance=request.user.profile)
    
    context={ 'p_form':p_form }

    return render(request,"accounts/profile.html",context)