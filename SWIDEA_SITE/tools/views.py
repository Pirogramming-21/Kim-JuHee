from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Tool

# Create your views here.
def tool_list(request):
    tools = Tool.objects.all()
    context = {
        "tools": tools
    }
    return render(request, 'tool_list.html', context)

def tool_create(request):
    if request.method == 'POST':
        Tool.objects.create(     
            name=request.POST.get("name"),
            kindof=request.POST.get("kindof"),
            descrip=request.POST.get("descrip"),
        )
        return redirect("/tools")
    return render(request, 'tool_create.html')

def tool_detail(request, pk):
    tool = get_object_or_404(Tool, id=pk)
    
    previous_tool = Tool.objects.filter(id__lt=pk).order_by("-id").first()
    next_tool = Tool.objects.filter(id__gt=pk).order_by("id").first()
    
    context = {
        "tool": tool,
        "previous_tool_id": previous_tool.pk if previous_tool else None,
        "next_tool_id": next_tool.pk if next_tool else None
    }
    return render(request, 'tool_detail.html', context)

def tool_update(request, pk):
    tool = get_object_or_404(Tool, id=pk)
    if request.method == "POST":
        tool.name = request.POST["name"]
        tool.kindof = request.POST["kindof"]
        tool.descrip = request.POST["descrip"]
        
        tool.save()
        
        return redirect(f"/tools/{pk}")
    
    context = {
        "tool": tool
    }
    return render(request, 'tool_update.html', context)

def tool_delete(request, pk):
    if request.method == 'POST':
        tool = get_object_or_404(Tool, id=pk)
        tool.delete()
        return redirect("/tools")
    return HttpResponse("Invalid request method.", status=405)