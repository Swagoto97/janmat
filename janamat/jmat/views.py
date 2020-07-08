from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import *
from django.contrib import messages
from django.contrib.sessions.models import Session
from django.contrib.auth import authenticate
from django.contrib.auth import logout, login
from django.core.files.storage import FileSystemStorage


def user_credential(request):
    if request.session.has_key('is_logged'):
        user = User.objects.get(username=request.session['username'])
        userProfile = UserProfile.objects.get(
            user=User.objects.get(username=user))
        firstName = user.first_name
        lastName = user.last_name
        profileImage = userProfile.profile_image
        # print(profileImage)
        if profileImage == "":
            profileImage = "False"
            # print(profileImage)
        user_context = {
            'user':   user,
            'userProfile':   userProfile,
            'firstName':   firstName,
            'lastName':   lastName,
            'profileImage':   profileImage
        }
        return user_context
    return {}


def chellenge_list_context():
    chellenge_list = Chellenge.objects.all()
    comment_list = Comment.objects.order_by('-date_comment')

    context = {
        'chellenge_list':   chellenge_list,
        'comment_list': comment_list,

    }
    return context


def home(request):
    if request.method == 'GET':  # http://127.0.0.1:8000/
        context = chellenge_list_context()
        # if request.GET:  # http://127.0.0.1:8000/?chellenge_id=1
        #     chellenge_id = request.GET['chellenge_id']
        #     selected_chellenge = Chellenge.objects.get(id=chellenge_id)
        #     topic_list = TopicList.objects.filter(Chellenge_id=chellenge_id)
        #     votes = Vote.objects.filter(Chellenge_id=chellenge_id)
        #     comment_list = Comment.objects.all()
        #     print(comment_list)
        #     try:
        #         user = User.objects.get(username=request.session['username'])
        #         is_votted = Vote.objects.get(
        #             User_id=user.id, Chellenge_id=chellenge_id).is_votted
        #     except:
        #         is_votted = False
        #     context = {
        #         'chellenge_list':   Chellenge.objects.all(),
        #         'selected_chellenge':   selected_chellenge,
        #         'topic_list':   topic_list,
        #         'comment_list':   Comment.objects.all(),
        #         'is_logged':   request.session.has_key('is_logged'),
        #         'is_votted':   is_votted,
        #     }
        #     context.update(user_credential(request))
        #     return render(request, 'index.html', context=context)
        context.update(user_credential(request))
        return render(request, 'index.html', context=context)
    # Execute this block when user is have just login
    context = chellenge_list_context()
    context.update(user_credential(request))
    return render(request, 'index.html', context=context)


# def signup(request):
#     pass


def signup(request):
    if request.method == 'GET':
        return render(request, 'signin.html', context={})
    else:
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        phone = request.POST['phone']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        UserName = email
        UserName_qs = User.objects.filter(username=UserName)
        if UserName_qs.exists():
            messages.error(request, 'user already exiest')
            return render(request, 'signin.html', context={})
        else:

            if password == cpassword:
                # UserName = email.split('@')[0]
                u = User(username=UserName, first_name=firstname,
                         last_name=lastname, email=email)  # Django user model
                u.save()
                u.set_password(cpassword)
                u.save()
                up = UserProfile(user=u, dob=datetime.now(), phone=phone, )
                up.save()
                return render(request, 'signin.html', context={})
            else:
                messages.error(request, 'password does not match')
                return render(request, 'signin.html', context={})


def signin(request):
    if request.method == 'GET':
        print('in get method')
        if request.session.has_key('is_logged'):
            return home(request)
        else:
            return render(request, 'signin.html', context={})
    else:
        # print('In post method')
        username = request.POST['username']
        password = request.POST['password']
        # print(username, password)
        user = authenticate(username=username, password=password)
        if not user:
            messages.error(request, 'Please check your username and password')
            return render(request, 'signin.html', context={})
            # context = {"is_SigninFailed": "Sign in failed."}
        # if not user.check_password(password):
        #     messages.error(request, 'Please check password')
        #     return render(request, 'signIn.html', context={})
        else:
            # print(user)
            user.last_login = datetime.today()
            user.save()
            request.session['is_logged'] = True
            request.session['username'] = username
            login(request, user)
            # print("Signin successfull and is_logged value is : {}".format(
            #     request.session.has_key('is_logged')))
            return home(request)
        # else:
        #     if not user:
        #         messages.error(request, 'Username does not exiest')
        #         return render(request, 'signIn.html', context={})
        #     # context = {"is_SigninFailed": "Sign in failed."}
        #     if not user.check_password(password):
        #         messages.error(request, 'Please check password')
        #         return render(request, 'signIn.html', context={})


def signout(request):
    logout(request)
    return home(request)


# def acceptVote(request):
#     if request.method == 'GET':
#         topic = TopicList.objects.get(id=request.GET['topic_id'])
#         user = User.objects.get(username=request.session['username'])
#         try:
#             vote = Vote.objects.get(
#                 User_id=user.id, Chellenge_id=topic.Chellenge_id)
#             return HttpResponse('Votting already done '+str(vote.Topic))
#         except:
#             vote = Vote(Chellenge_id=topic.Chellenge_id,
#                         Topic_id=request.GET['topic_id'], User_id=user.id, is_votted=True)
#             vote.save()
#             TopicList.objects.filter(id=request.GET['topic_id']).update(
#                 voteCount=F("voteCount") + 1)
#             return HttpResponse('Votting Done Successfully in : ' + str(vote.Topic))


def test(request):
    comments = Comment.objects.all()
    print(comments)
    return render(request, 'ajaxTest.html', context={'posts': comments})


def pic_update(request):

    if request.method == 'GET':

        if request.session.has_key('is_logged'):
            return home(request)
        else:
            return render(request, 'signin.html', context={})
    else:
        pic = request.FILES['pic_update']
        user = User.objects.get(username=request.session['username'])
        userProfile = UserProfile.objects.get(
            user=User.objects.get(username=user))
        # print(user)
        # print(userProfile)

        up = UserProfile(user=user, profile_image=pic)
        up.save()
        fs = FileSystemStorage()
        fs.save(pic.name, pic)
        return home(request)


def postComment(request):
    if request.method == 'POST':
        comment = request.POST.get('comment')
        user = request.user
        postSno = request.POST.get('postSno')
        post = Chellenge.objects.get(id=postSno)

        com = Comment(user_id=user, message=comment, chellenge_id=post)
        com.save()
        messages.success(request, 'yor comment posted success fully')
        # comme = Comment.objects.all()
        # print(comme)

    return redirect('/')


def contact(request):
    if request.method == 'POST':
        email = request.POST['email']
        mesg = request.POST['message']
        con_us = contact_us(email=email, message=mesg)
        con_us.save()
    return redirect('/')
