#from django.views import generic
#from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render
import foursquare
import pygeoip


# Rawdata that contains the mapping between Ip's and geolocations.
rawdata = pygeoip.GeoIP("./sushi_network/resources/GeoLiteCity.dat")
# function that returns the latitude and longitude of the received IP
def ipquery(ip):
    data = rawdata.record_by_name(ip)
    #country = data['country_name']
    #city = data['city']
    lat = data['latitude']
    longi = data['longitude']
    #print '[x] '+str(city)+',' +str(country)
    #print '[x] Latitude: '+str(lat)+ ', Longitude: '+ str(longi)
    return (lat,longi)

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def HomeView(request):

    f_client = foursquare.Foursquare(client_id="MSB3H0C14BLRSSAAYGELVLAAWVKWUL5DXYVMWF2UJPUVZOMC",
                                   client_secret="ZSDRDRBEZHO4DUH5TWS2DQMOUP1MMBBMEZJBNDZZVXTUFZX1",
                                   redirect_uri="http://www.icogroup.com")

    client_ip = get_client_ip(request)
    print client_ip
    
    #geolocation = ipquery(client_ip)
    #print geolocation
    #def get_queryset(self):
    #    print geolocation

    return render(request, 'home.html')


