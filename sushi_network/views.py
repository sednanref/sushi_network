from django.views import generic
import foursquare



class HomeView(generic.ListView):
    template_name = 'home.html'
    context_object_name = 'home_page'
    client = foursquare.Foursquare(client_id="MSB3H0C14BLRSSAAYGELVLAAWVKWUL5DXYVMWF2UJPUVZOMC",
                                   client_secret="ZSDRDRBEZHO4DUH5TWS2DQMOUP1MMBBMEZJBNDZZVXTUFZX1",
                                   redirect_uri="http://www.icogroup.com")
    def get_queryset(self):

        return ""


