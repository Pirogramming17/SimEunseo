import json
from django.shortcuts import render, get_object_or_404, redirect
from .models import Idea, Tool
from .forms import IdeaForm, ToolForm
from datetime import datetime
from django.http import HttpResponse,JsonResponse


def main(request):
    order_list = ['찜한순','이름순','등록순','최신순']
    order = request.GET.get('order', None)
    if order == order_list[0]:
        ideas=Idea.objects.all().order_by('-like')
    elif order == order_list[1]:
        ideas=Idea.objects.all().order_by('name')
    elif order == order_list[2]:
        ideas=Idea.objects.all().order_by('created_date')
    else : #기본 정렬을 작성시간순으로 한다
        ideas = Idea.objects.all().order_by('-created_date')
        
    context = {
        "ideas" : ideas,
        "order_list" : order_list,
        "order" : order,
    }
    return render(request, template_name='ideas/main.html', context=context)

def register(request):
    ideas = Idea.objects.all()

    if request.method == 'POST':
        form = IdeaForm(request.POST, request.FILES)
        if form.is_valid():
            idea = form.save(commit=False)
            idea.user = request.user
            idea.save()
            return redirect('/')
        else :
            return redirect('/')
    else :
        form = IdeaForm()
        context={
            'form':form,
            'ideas':ideas,
        }
        return render(request, 'ideas/register.html', context=context)

def detail(request, id):
    idea = Idea.objects.get(id=id)
    tools = Tool.objects.all()
    for tool in tools:
        if tool.name == idea.tool_choice:
            tool_id = tool.id
    context = {
        "idea":idea,
        "tool_id":tool_id
    }
    return render(request, template_name="ideas/detail.html",context=context)

def edit(request, id):
    idea = get_object_or_404(Idea, id=id)

    if request.method == "POST":
        form = IdeaForm(request.POST, request.FILES, instance=idea)
        if form.is_valid():
            idea = form.save()
            idea.save()
        return redirect(f'/detail/{id}')
    else:
        form = IdeaForm(instance=idea)
        context = {
            "idea" : idea,
            "form" : form
        }
        return render(request, 'ideas/edit.html', context=context)

def delete(request, id):
    if request.method == "POST":
        idea = Idea.objects.get(id=id)
        idea.delete()
    return redirect('/')

def tool(request):
    tools = Tool.objects.all()
    context = {
        "tools" : tools
    }
    return render(request, template_name='ideas/tool.html', context=context)

def tool_register(request):
    if request.method == 'POST':
        form = ToolForm(request.POST)
        if form.is_valid():
            tool = form.save(commit=False)
            tool.save()
            return redirect('/tool')
        else :
            return redirect('/tool')
    else :
        form = ToolForm()
        return render(request, 'ideas/tool_register.html', {'form' : form})
    
def tool_detail(request,id):
    tool = Tool.objects.get(id=id)
    ideas = Idea.objects.all()
    context = {
        "tool":tool,
        "ideas":ideas,
    }
    return render(request, template_name="ideas/tool_detail.html",context=context)

def tool_edit(request, id):
    tool = get_object_or_404(Tool, id=id)

    if request.method == "POST":
        form = ToolForm(request.POST, instance=tool)
        if form.is_valid():
            tool = form.save()
            tool.save()
        return redirect(f'/tool/detail/{id}')
    else:
        form = ToolForm(instance=tool)
        context = {
            "tool" : tool,
            "form" : form
        }
        return render(request, 'ideas/tool_edit.html', context=context)
    
def tool_delete(request, id):
    if request.method == "POST":
        tool = Tool.objects.get(id=id)
        tool.delete()
    return redirect('/tool')

def likes(request): 
    if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        idea_id = request.GET['idea_id'] 
        idea = Idea.objects.get(id=idea_id) 
				
        if not request.user.is_authenticated:
            message = "로그인을 해주세요"
            context = {'like_count' : idea.like.count(),"message":message}
            return HttpResponse(json.dumps(context), content_type='application/json')

        user = request.user
        if idea.like.filter(id = user.id).exists():
            idea.like.remove(user) 
            message = "좋아요 취소" 
        else: 
            idea.like.add(user) 
            message = "좋아요" 

        context = {'like_count' : idea.like.count(),"message":message}
        return HttpResponse(json.dumps(context), content_type='application/json')
    
def interest_plus(request):
    if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        idea_id = request.GET['idea_id'] 
        idea = Idea.objects.get(id=idea_id)
        idea.interest += 1
        idea.save()
        context={'interest':idea.interest}
        return HttpResponse(json.dumps(context), content_type='application/json')
        
def interest_minus(request):
    if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        idea_id = request.GET['idea_id'] 
        idea = Idea.objects.get(id=idea_id) 
        idea.interest -= 1
        idea.save()
        context={'interest':idea.interest}
        return HttpResponse(json.dumps(context), content_type='application/json')