from django.shortcuts import render, HttpResponse
from django.views import View
from .forms import AddGymForm, FindGymForm
from registration.models import Gym
from django.contrib.gis.geos import Point, GEOSGeometry


class HomeView(View):

	def get(self, request, *args, **kwargs):
		return render(request, "home.html", {})


class AddGymView(View):

	def get(self, request, *args, **kwargs):
		form = AddGymForm()
		return render(request, "addgym.html", { "form": form, })

	def post(self, request, *args, **kwargs):
		if request.POST['location']=='':
			form = AddGymForm(request.POST)
			form.errors['location'][0]=form.errors['location'][0].replace("No geometry value provided.", "Gym location not set!")
			return render(request, "addgym.html", { "form": form,})

		obj = Gym.objects.create(name=request.POST['name'], location=request.POST['location'])
		obj.save()

		return HttpResponse("Gym added successfully. This gym needs to be verified before it shows up on our website.")

class FindGymView(View):

	def get(self, request, *args, **kwargs):
		form = FindGymForm()
		return render(request, "gymfinder.html", { "form": form, })

	def post(self, request, *args, **kwargs):
		print(request.POST)
		if request.POST['location']=='':
			form = FindGymForm(request.POST)
			form.errors['location'][0]=form.errors['location'][0].replace("No geometry value provided.", "Need your location to find nearby gyms!")
			return render(request, "gymfinder.html", { "form": form,})
		radius = int(request.POST['max_distance'])
		location = GEOSGeometry(request.POST["location"])
		location = Point(location.coords)
		area = location.buffer(radius/ 40000 * 360)
		gyms_found = []
		for gym in Gym.objects.all():
			if gym.location.within(area):
				gyms_found.append(gym)

		for i in range(len(gyms_found)):
			dist = round(location.distance(gyms_found[i].location) / 360 *40000, 1)
			gyms_found[i] = (gyms_found[i], dist)

		context = {
			"gyms_found": len(gyms_found),
			"max_distance": radius,
			"gyms": gyms_found,
		}
		return render(request, "gyms_found.html", context)

class LandingView(View):

	def get(self, request, *args, **kwargs):
		return render(request, "dash.html", {})