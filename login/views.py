from django.shortcuts import render, HttpResponse
import json
times = 0
def login(request):
    global times
    print('Login Page Opened!')
    times += 1
    if request.path == '/login/signin/':
        report_loc = '../signin/'
    else: report_loc = 'signin/'
    return render(request, 'login.html', {'loc':report_loc,'error': ''})
def signin(request):
    print('Login Request Made!')
    print('Reading Data from JSON')
    json2 = open('user_data.json',) 
    data = json.load(json2) 
    l1 = data['u_data'][0]
    emails = list(l1.keys())
    passwords = list(l1.values())
    json2.close() 
    print('Read data from JSON')
    global times
    times = times+1
    if request.path == '/login/signin/':
        report_loc = '../signin/'
    else: report_loc = 'signin/'
    email = request.POST['email']
    password = request.POST['password']
    if email in emails:
        if passwords[emails.index(email)] == password:
            times = 0
            print('Logged in User, returning HTTP response')
            return HttpResponse('You are registered')
        else:
            print('Email != Password, returning HTTP response')
            return render(request, 'login.html', {'loc':report_loc,'errorclass':'alert alert-danger','error': 'Sorry. The Email and Password do not match.'})
    else:
        print('Account does not exist, returning HTTP response')
        return render(request, 'login.html', {'loc':report_loc,'errorclass':'alert alert-danger','error': 'Sorry. No such account exists. Consider signing up!'})