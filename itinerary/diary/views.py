from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Topic, Entry, Img
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from .forms import TopicForm, EntryForm


def index(request):
	return render(request, 'diary/index.html')


@login_required
def topics(request):

	topics = Topic.objects.filter(owner=request.user).order_by('date_added')
	context = {'topics': topics}
	return render(request, 'diary/topics.html', context)


@login_required
def topic(request, topic_id):
	topic = Topic.objects.get(id=topic_id)
	if topic.owner != request.user:
		raise Http404
	entries = topic.entry_set.order_by('-date_added')
	context = {'topic': topic, 'entries': entries}
	return render(request, 'diary/topic.html', context)


@login_required
def new_topic(request):
	if request.method != 'POST':
		form = TopicForm
	else:
		form = TopicForm(request.POST)
		if form.is_valid():
			new_topic = form.save(commit=False)
			new_topic.owner = request.user
			new_topic.save()
			return HttpResponseRedirect(reverse('diary:topics'))

	context = {'topic': topic, 'form': form}
	return render(request, 'diary/new_topic.html', context)


@login_required
def new_entry(request, topic_id):
	topic = Topic.objects.get(id=topic_id)
	if request.method != 'POST':
		form = EntryForm()
	else:
		form = EntryForm(data=request.POST)
		if form.is_valid():
			new_entry = form.save(commit=False)
			new_entry.topic = topic
			new_entry.save()
			return HttpResponseRedirect(reverse('diary:topic', args=[topic_id]))

	context = {'topic': topic, 'form': form}
	return render(request, 'diary/new_entry.html',context)


@login_required
def edit_entry(request, entry_id):
	entry = Entry.objects.get(id=entry_id)
	topic = entry.topic

	if request.method != 'POST':
		form = EntryForm(instance=entry)
	else:
		form = EntryForm(instance=entry, data=request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('diary:topic',args=[topic.id]))

	context = {'entry': entry, 'topic': topic, 'form':form}
	return render(request, 'diary/edit_entry.html',context)


@login_required
def showImg(request):
    imgs = Img.objects.filter(owner=request.user).order_by('date_added') # 从数据库中取出所有的图片路径
    context = {'imgs' : imgs}
    return render(request, 'diary/showImg.html', context)


@login_required
def uploadImg(request): # 图片上传函数
    if request.method == 'POST':
        img = Img(img_url=request.FILES.get('img'))
        img.save()
    return render(request, 'diary/imgUpload.html')
   

   