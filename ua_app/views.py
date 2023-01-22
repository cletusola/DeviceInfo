from django.shortcuts import render
import requests 
import json 


url = "https://user-agent-parser4.p.rapidapi.com/user-agent/useragent.php"

def home(request):
    ua = request.META.get('HTTP_USER_AGENT', '') 
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')  


    querystring = {"ua":f"{ua}"}

    headers = {
        "X-RapidAPI-Key": "8211bedd48mshaeec0f8548aac97p1c9a0djsn0a939a85759c",
        "X-RapidAPI-Host": "user-agent-parser4.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    
    data = json.loads(response.text)

    context = {
        'user_agent': data['user_agent'],
        'status': data['status'],
        'device': data['device'],
        'isBot': data['isBot'],
        'browserFamily': data['browserFamily'],
        'osFamily': data['osFamily'],
        'type': data['clientInfo']['type'],
        'name': data['clientInfo']['name'],
        'short_name': data['clientInfo']['short_name'],
        'version': data['clientInfo']['version'],
        'engine': data['clientInfo']['engine'],
        'engine_version': data['clientInfo']['engine_version'],
        'family':data['clientInfo']['family'],
        'os_name': data['osInfo']['name'],
        'os_short_name': data['osInfo']['short_name'],
        'os_version': data['osInfo']['version'],
        'os_platform': data['osInfo']['platform'],
        'brand': data['brand'],
        'model': data['model'],
        'ip':ip,

    }

    return render(request, 'home.html', context)
