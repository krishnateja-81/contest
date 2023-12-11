from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from . import models

test = models.Questions.objects.all()
users = User.objects.all()

def user_login(request):
    if request.method == "POST":
        uname = request.POST['uname'].upper()
        password = request.POST['password']
        user = authenticate(username = uname, password = password )
        if models.fraud_model.objects.filter(username=uname).exists():
            return redirect('fraud')
        else:
            if user is not None :
                login(request, user)
                return redirect('landing')

            else:
                return redirect('register')
    return render(request, "login.html")

def register(request):
    values = {}
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        pass1 = request.POST['password']
        uname = request.POST['uname'].upper()
        if User.objects.filter(username=uname).exists():
            values['emailerr'] = "email already exists."
            values['fname'] = fname
        else:
            userobj = User.objects.create_user(
                username=uname,
                password=pass1,
                first_name=fname,
                last_name=lname
            )
            userobj.save()

            return redirect('login')
    return render(request, "register.html", values)


@login_required
def landing(request):
    time = models.time.objects.all()
    for i in time:
        t = i.time
    dic = {'time':t}
    return render(request, 'landing.html', dic)

@login_required
def questions(request):
    l = {}
    for i in test:
        # question = i.question
        l[i.qno] = i.question
    return render(request, 'questions.html', {'questions': l})

@login_required
def leaderboard(request):
    
    leaderboard_entries = models.score.objects.all().order_by('-score')[:10] 
    return render(request, 'leaderboard.html', {'leaderboard_entries': leaderboard_entries})



def fraud(request):
    
    uname = request.user
    if uname is not None:
        fraud_user = models.fraud_model.objects.get_or_create(
            username = uname,
            fraud = True
        )
        logout(request)
    return render(request, 'fraud.html')
@login_required
def home(request, qno=None):
    uname = request.user
    # print(uname)
    qno = qno
    qs_str = f"question{qno}"
    question = models.Questions.objects.get(qno = qno)
    try:
        user_score = models.score.objects.get(uname = uname)
    except:
        models.score.objects.create(uname = uname)   
        user_score = models.score.objects.get(uname = uname)
    max_score = getattr(user_score, qs_str, None)
    code = ""
    obj = {}
    qs = []
    qs.append(question.question)
    
    obj['question'] = qs[0]
    obj['sinput'] = question.sinpu
    obj['soutput'] = question.soutpu
    if request.method == "POST":
        code = request.POST['seed']
        obj['code'] = code
        # print(code)
    score = 0
    test_cases = []
    test_output = []
    
    test_cases.extend([question.inpu, question.inpu2, question.inpu3, question.inpu4])
    test_output.extend([question.outpu, question.outpu2, question.outpu3, question.outpu4])

    for i in range(4):
        submission_path = f"{code}"
        test_input = test_cases[i]

        output = evaluate_submission(submission_path, test_input)
        if str(output) == str(test_output[i]):
            score += 1
    soutput = evaluate_submission(submission_path, question.sinpu)
    obj['output'] = soutput
    obj['score'] = score
    obj['fscore'] = 4 - score
    if max_score is None or score > max_score:
        setattr(user_score, qs_str, score)
        user_score.save()
    
    return render(request, 'home.html', obj)


import subprocess

def evaluate_submission(submission_path, test_input):
    try:
        result = subprocess.run(['python', '-c', submission_path], input=test_input, text=True, capture_output=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr}"

    
    