from django.shortcuts import render
from django.views.generic import View

from .models import CourseOrg, CityDict
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger


class OrgView(View):
	def get(self, request):
		all_orgs  = CourseOrg.objects.all()		
		all_citys = CityDict.objects.all()
		hot_orgs = all_orgs.order_by('-click_nums')[:3]
		city_id = request.GET.get('city', "")
		if city_id:
			all_orgs = all_orgs.filter(city_id=int(city_id))

		category = request.GET.get('ct', "")
		if category:
			all_orgs = all_orgs.filter(category=category)

		sort = request.GET.get('sort', "")
		if sort:
			if sort == "students":
				all_orgs = all_orgs.order_by("-students")
			elif sort == "courses":
				all_orgs = all_orgs.order_by("-course_nums")

		org_nums = all_orgs.count()



		try:
			page = request.GET.get('page', 1)
		except PageNotAnInteger:
			page = 1
		p = Paginator(all_orgs, 3, request=request)
		orgs = p.page(page)

		return render(request, "org-list.html", {
			'all_orgs': orgs, 
			'all_citys': all_citys,
			'org_nums': org_nums,
			'city_id': city_id,
			'category': category,
			'hot_orgs': hot_orgs,
			'sort': sort,
		})
