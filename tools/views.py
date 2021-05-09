from django import views
from django.shortcuts import render, redirect
from .models import Tool
from .forms import ToolForm
from .utils import tools_form_validations

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
            new_tool = form.save(commit=False)
            new_tool = tools_form_validations(form, new_tool)
            new_tool.save()
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

    def post(self, request, id):
        tool = Tool.objects.get(id=id)
        tool_actual_is_in_maintain_value = tool.is_in_maintain
        form = ToolForm(instance=tool, data=request.POST)
        if form.is_valid():
            tool_updated = form.save(commit=False)
            tool_updated = tools_form_validations(form, tool_updated, tool_actual_is_in_maintain_value)
            tool_updated.save()
            return redirect('tools:detail', tool_updated.id)
        else:
            context = {
                'form': form
            }
            return render(request, self.template_name, context)

def DeleteTool(request):
    tool = Tool.objects.get(id=request.POST['id'])
    tool.delete()
    return redirect('tools:list')
