import xadmin
from .models import Course, Lesson, Vidio, CourseResource

class CourseAdmin(object):	
	list_display =	['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'imge', 'click_nums', 'add_time']
	search_fields = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'click_nums']
	list_filter = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'click_nums', 'add_time']


class  LessonAdmin(object):
	list_display =	['course', 'name', 'add_time']
	search_fields = ['course', 'name']
	list_filter = ['course__name', 'name', 'add_time']

 
class VidioAdmin(object):
	list_display =	['name', 'add_time']
	search_fields = ['name']
	list_filter = ['name', 'add_time']
	

class CourseResourceAdmin(object):
	list_display =	['name', 'add_time']
	search_fields = ['name', 'add_time']
	list_filter = ['name', 'add_time']




xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Vidio, VidioAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)