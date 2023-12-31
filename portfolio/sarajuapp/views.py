# from urllib.request import urlopen
# from django.http import HttpRequest
# from verify_email import verify_email
from django.shortcuts import render, redirect
from sarajuapp.models import Connection, Viewed
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from datetime import datetime
import json
import requests

# Create your views here.
def home(request):
    def device_type():
        if request.user_agent.is_mobile:
            return 'Mobile'
        if request.user_agent.is_tablet:
            return 'Tablet'
        if request.user_agent.is_pc:
            return 'PC/Laptop'
        if request.user_agent.is_bot:
            return 'Bot'
    
    deviceType = device_type()
    os = request.user_agent.os.family + " " + request.user_agent.os.version_string
    browser = request.user_agent.browser.family
    
    # try:
    #     url = "http://ipinfo.io/json"
    #     responce = urlopen(url)
    #     data = json.load(responce)
    #     ip = data['ip']
    # except:
    #     ip = 'Not Found'
    # ----------------------------------------------
    # from requests import get
    # ip = get('https://api.ipify.org').text
    # print('My public IP address is: {}'.format(ip))

    if request.method=='POST':
        name = request.POST.get('name')
        print("Name",name)
        email = request.POST.get('email')
        print("Email", email)
        phone = request.POST.get('phone')
        print("Phone",phone)
        message = request.POST.get('message')
        print("Message",message)
        time = request.POST.get('time')
        print("Time",time)
        ip = request.POST.get('ip')
        print("IP",ip)
        
        try:
            # r = requests.get("https://get.geojs.io/")
            # ip_request = requests.get('https://get.geojs.io/v1/ip.json')
            # ipAdd = ip_request.json()['ip']
            url = 'https://get.geojs.io/v1/ip/geo/'+ip+'.json'
            geo_request = requests.get(url)
            geo_data = geo_request.json()
            city = 'Not Found'
            region = 'Not Found'
            country = 'Not Found'
            if 'city' in geo_data:
                city = geo_data['city']
            if 'region' in geo_data:
                region = geo_data['region']
            if 'country' in geo_data:
                country = geo_data['country']
            location = f"{city}, {region}, {country} ({geo_data['organization']})"
            latitude = geo_data['latitude']
            longitude = geo_data['longitude']
        except:
            location = 'Not Found'
            latitude = 'Not Found'
            longitude = 'Not Found'
            # print("Please check your internet connection")
        
        if len(phone) != 10:
            messages.info(request, "Phone number should be 10 Character long.")
            return redirect('/#contact')
        
        if phone.startswith('6') or phone.startswith('7') or phone.startswith('8') or phone.startswith('9'):
            pass
        else:
            messages.info(request, "Phone number should start with (6,7,8,9)")
            return redirect('/#contact')
        
        member = Connection(name=name, email=email, phone=phone, message=message, time=time, device_type=deviceType, os=os,  browser=browser,ip=ip, location=location, latitude=latitude, longitude=longitude)
        member.save()

        subject = f'Sarajuddin - {name} wants to connect with you through your Portfolio'
        message = f'Name : {name}\nEmail : {email}\nPhone : {phone}\n\nMessage :  {message}\n\nWe have got some confidential information of the visitor. Please look at them - \n\n Visiting Time : {time}\nDevice Type : {deviceType}\nOperating System : {os}\nBrowser : {browser}\nIP Address : {ip}\nVisitor\'s Location : {location}\nLatitude : {latitude}\nLongitude : {longitude}'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['saraju.work@gmail.com']
        send_mail( subject, message, email_from, recipient_list )

        messages.success(request, "Message is Sent")
        return redirect('/#contact')
    
    time = datetime.ctime(datetime.now())
    subject = f'Sarajuddin - Someone viewed your Portfolio'
    message = f'We have detected that someone viewed your portfolio. Some information of the user are given below - \n\nTime : {time}\nDevice Type : {deviceType}\nOperating System : {os}\nBrowser : {browser}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['saraju.work@gmail.com']
    send_mail( subject, message, email_from, recipient_list )
    
    member = Viewed(time=time, device_type=deviceType, browser=browser, os=os)
    member.save()
    
    return render(request, 'index.html')
