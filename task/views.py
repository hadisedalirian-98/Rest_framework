from django.shortcuts import render
from task.models import TodoTask,Category
from task.forms import Taskcreateform
from django.http import HttpResponseRedirect
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404,redirect


def showtask(request):
    query =TodoTask.objects.all().order_by('created')
    
    form =Taskcreateform(request.POST)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')
    else:
        form =Taskcreateform()
        

    dict ={
    
    'query':query,
    'form':form,
}
    return render(request,'task/index.html',dict)


class TaskDetail(DetailView):
     model = TodoTask
     template_name='task/detail.html'
     
def delete_task(request, id):
    task= get_object_or_404(TodoTask,id=id)
    task.delete()
    return redirect('showtask')