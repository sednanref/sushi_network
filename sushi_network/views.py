#from django.views import generic
#from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render
import pygeoip


# Rawdata that contains the mapping between Ip's and geolocations.
rawdata = pygeoip.GeoIP("./sushi_network/resources/GeoLiteCity.dat")
# function that returns the latitude and longitude of the received IP
def ipquery(ip):
    data = rawdata.record_by_name(ip)
    country = data['country_name']
    city = data['city']
    lat = data['latitude']
    longi = data['longitude']
    return (lat,longi, country, city)

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def HomeView(request):

    client_ip = get_client_ip(request)
    print client_ip
    location = ipquery(client_ip)
    context = {
        "ip": client_ip,
        "country": location[2],
        "city": location[3],
        "latitude":location[0],
        "longitude": location[1]
    }
    return render(request, 'home.html',
                  context=context
                  )


