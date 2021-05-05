from django import views
from django.shortcuts import render, redirect
from .models import Tool
from .forms import ToolForm

def ListTools(request):
    tools = Tool.objects.all()
    template_name = 'tools/list.html'
    context = {
        'tools': tools
    }
    return render(request, template_name, context)

def DetailTool(request, id):
    tool = Tool.objects.get(id=id)
    template_name = 'tools/detail.html'
    context = {
        'tool': tool
    }
    return render(request, template_name, context)

class CreateTool(views.View):
    template_name = 'tools/form.html'

    def get(self, request):
        form = ToolForm()
        context = {
            'form': form
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = ToolForm(data=request.POST)
        if form.is_valid():
            tool = form.save(commit=False)
            if not form.cleaned_data['has_been_maintained']:
                tool.mainteance_date = None
            tool.save()
            return redirect('tools:list')
        else:
            context = {
                'form': form
            }
            return render(request, self.template_name, context)

class UpdateTool(views.View):
    template_name = 'tools/form.html'

    def get(self, request, id):
        tool = Tool.objects.get(id=id)
        form = ToolForm(instance=tool)
        context = {
            'form': form,
            'tool': tool,
            'is_update': True
        }
        return render(request, self.template_name, context)
