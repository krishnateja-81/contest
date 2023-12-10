from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from . import models

test = models.Questions.objects.all()
users = User.objects.all()

def user_login(request):
    if request.method == "POST":
        uname = request.POST['uname']
        password = request.POST['password']

        user = authenticate(username = uname, password = password )
        if user is not None:
            login(request, user)
            request.session['username'] = uname
            return redirect('questions')

        else:
            return redirect('register')
    return render(request, "login.html")

def register(request):
    values = {}
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        pass1 = request.POST['password']
        # email = request.POST['email']
        uname = request.POST['uname']
        if User.objects.filter(username=uname).exists():
            #print("email")
            values['emailerr'] = "email already exists."
            values['fname'] = fname
        else:
            userobj = User.objects.create_user(
                username=uname,
                password=pass1,
                # email=email,
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

# @login_required
# def home(request, qno=None):
#     qno = qno
#     test = models.Questions.objects.get(qno = qno)
#     print(qno)
#     code = ""
#     obj={}
#     qs = []
#     for i in test:
#         qs.append(i.question)
    
#     obj['question'] = qs[qno-1]
#     if request.method == "POST":
#         code = request.POST['seed']
#         obj['code'] = code
#         # print(code)
#     score = 0
#     test_cases = []
#     test_output = []
#     for i in test:
#         test_cases.append(i.inpu)
#         test_output.append(i.outpu)
#         test_cases.append(i.inpu2)
#         test_output.append(i.outpu2)
#         test_cases.append(i.inpu3)
#         test_output.append(i.outpu3)
#         test_cases.append(i.inpu4)
#         test_output.append(i.outpu4)

#     for i in test:
#         for j in range(4):
#             submission_path = f'''{code}'''
#             test_input = test_cases[j]

#             output = evaluate_submission(submission_path, test_input)
#             obj['output'] = output
#             # print(f"Output: {output}")
#             if str(output) == str(test_output[j]):
#                 score+=1
#     obj['score'] = score
#     # print(score)
    
#     return render(request, 'home.html', obj)

@login_required
def home(request, qno=None):
    qno = qno
    question = models.Questions.objects.get(qno=qno)
    # print(qno)
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
        # obj['output'] = output
        # print(f"Output: {output}")
        if str(output) == str(test_output[i]):
            score += 1
    soutput = evaluate_submission(submission_path, question.sinpu)
    obj['output'] = soutput
    obj['score'] = score
    obj['fscore'] = 4 - score
    # print(score)
    
    return render(request, 'home.html', obj)


# for i in test:
#     print(i.inpu)
#     print(i.outpu)

import subprocess

def evaluate_submission(submission_path, test_input):
    try:
        result = subprocess.run(['python', '-c', submission_path], input=test_input, text=True, capture_output=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr}"

# if __name__ == "__main__":
#     for i in test:
        
#         submission_path = r'C:\Users\Admin\seed\code.py'
#         test_input = i.inpu

#         output = evaluate_submission(submission_path, test_input)
#         print(f"Output: {output}")
    
    