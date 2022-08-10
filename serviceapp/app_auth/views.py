

from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site


from .token import generatorToken

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail, EmailMessage
import serviceapp


def login_service(request):
    if request.method == "POST" :
        username = request.POST['username']
        pwd = request.POST['pwd']
        user = authenticate(username=username, password=pwd)
        my_user = User.objects.get(username=username)

        if user is not None:
            login(request, user)
            if user.is_entity:
                return redirect('index')
            else:
                return redirect('acteur')
        elif my_user.is_active == False:
            messages.error(request, "Vous n'avez pas confirmer votre compte email faite le avant de vous connecter merci!")
        else:
            messages.error(request, 'Erreur d"authentification')
            return render(request, 'app_auth/login.html')
    return render(request, 'app_auth/login.html')

def entity(request):
    return render(request, 'pageacc/index.html')

def acteur(request):
    return render(request, 'service/acteur.html')

def register_view(request):
    if request.method == "POST" :
        lastname = request.POST['lastname']
        firstname = request.POST['firstname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['pwd']
        password1 = request.POST['pwd1']
        if User.objects.filter(username=username):
            messages.error(request, 'Ce nom existe déjà')
            return render(request, 'app_auth/signup.html')

        if User.objects.filter(email=email):
            messages.error(request, 'Cet email possède un compte')
            return render(request, 'app_auth/signup.html')

        if not username.isalnum():
            messages.error(request, 'Le nom doit etre alphanumerique')
            return render(request, 'app_auth/signup.html')

        if password != password1:
            messages.error(request, 'Les deux mot de passe ne coincide pas')
            return render(request, 'app_auth/signup.html')

        my_user = User.objects.create_user(username, email, password)
        my_user.first_name = firstname
        my_user.last_name = lastname
        my_user.is_active = False
        my_user.save()
        messages.success(request, 'Votre compte a été créé avec succes')
        subject = "Bienvenue sur main d'oeuvre App "
        message = "Bienvenue " + my_user.first_name + " " + my_user.last_name + "\n Nous somme heureux de vous compter parmi nous \n\n Merci"
        from_email = serviceapp.settings.EMAIL_HOST_USER
        to_list = [my_user.email]
        send_mail(subject, message, from_email, to_list, fail_silently=False)
        current_site = get_current_site(request)
        email_subject = "Confirmation du compte email"
        message_confirm = render_to_string("app_auth/emailconfirm.html", {
            "name" : my_user.first_name,
            "domain" : current_site.domain,
            "uid" : urlsafe_base64_encode(force_bytes(my_user.pk)),
            "token" : generatorToken.make_token(my_user)
        })

        email = EmailMessage(
            email_subject,
            message_confirm,
            serviceapp.settings.EMAIL_HOST_USER,
            [my_user.email]
        )

        email.fail_silently = False
        email.send()
        return redirect('login')
    else:
        return render(request, 'app_auth/signup.html')

# def register_view(request):
#     form = UserForm()
#     if request.method == "POST":
#         form = UserForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')
#         return render(request, 'app_auth/signup.html', {'form':form})

def log_out(request):
    if User.is_superuser :
        pass
    else:
        logout(request)

    return redirect('index')

def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and generatorToken.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Votre compte a été activé félicitaion')
        return redirect('login')
    else:
        messages.error(request, 'Activation non effectuée')
        return redirect('index')