from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from googleplaces import GooglePlaces, types, lang
from django.core.mail import send_mail
from django.http import HttpResponseRedirect

YOUR_API_KEY = 'AIzaSyD3JqMSrCskCzqmhGmyxyP0Fd1MSoSGJn4'

google_places = GooglePlaces(YOUR_API_KEY)

def home(request):
    return render_to_response('search.html', context_instance=RequestContext(request))

def search(request):
    return render_to_response('search.html', context_instance=RequestContext(request))

def about(request):
    return render_to_response('about.html', context_instance=RequestContext(request))

def contact(request):
    errors = []
    if request.method == 'POST':
       if not request.POST.get('subject',''):
	             errors.append('Enter a subject.')
       if not request.POST.get('message',''):
	             errors.append('Enter a message.')
       if not errors:
	             send_mail(
		          request.POST['subject'],
		request.POST['message'],
		request.POST.get('email', 'findmyplacehelp@gmail.com'),
		['findmyplacehelp@gmail.com'],
	  )
       return HttpResponseRedirect('/thanks.html')
    return render(request, 'contact.html', {'errors': errors})

def thanks(request):
    return render_to_response('thanks.html')

def places(request):
    #define dictionary
    mylist = {}
    #define variables
    loc = ""
    key = ""
    if request.method == 'POST':
		loc = request.POST.get('location', '')
		key = request.POST.get('keyword','')
    	
    query_result = google_places.nearby_search(
       	   location=loc, keyword=key, radius=10000
	   )
			
    for place in query_result.places:
	     #print place.name
       #print place.geo_location
       #print place.place_id
       # Referencing any of the attributes below, prior to making a call to
       # get_details() will raise a googleplaces.GooglePlacesAttributeError.
       #print place.details # A dict matching the JSON response from Google.
       #print place.local_phone_number
       #print place.international_phone_number
	     #print place.website
	     #print place.url
	     place.get_details()
	     mylist[place.name] = [place.formatted_address, place.local_phone_number, place.international_phone_number]
	
    return render_to_response('display_list.html', {'location':loc, 'keyword':key, 'mylist':mylist}, context_instance=RequestContext(request))
