from django.shortcuts import render
import requests
import json
url = url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-key': "e5f8a1198cmsh659340523c10f93p1eddffjsn914493d4e904",
    'x-rapidapi-host': "covid-193.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers).json()

# Create your views here
def helloword(request):
	if request.method=="POST":
		list=[]
		noresults=int(response['results'])
		for x in range(0,noresults):
			list.append(response['response'][x]['country'])
		selectedcountry=request.POST['selectedcountry']
		noresults=int(response['results'])
		for x in range(0,noresults):
			if selectedcountry==response['response'][x]['country']:
				new=response['response'][x]['cases']['new']
				active=response['response'][x]['cases']['active']
				critical=response['response'][x]['cases']['critical']
				recovered=response['response'][x]['cases']['recovered']
				total=response['response'][x]['cases']['total']
				deaths=int(total)-int(active)-int(recovered)
		context={'selectedcountry':selectedcountry,'list':list,'new':new,'active':active,'critical':critical,'recovered':recovered,'deaths':deaths,'total':total}
		return render(request,'hello.html',context)
	
	
	context={'list':list}
	return render(request,'hello.html',context)