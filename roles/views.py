from django.shortcuts import render, redirect
from .models import Role
from .forms import RoleForm
from django.contrib import messages
# Create your views here.
def roles(request):
    records  = Role.objects.all()
    return render(request, "roles.html",{'records': records})


def roleform(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = RoleForm(request.POST)
            if form.is_valid():
                role = request.POST['role']
                team = request.POST['team']
                data = Role(role=role,team=team)
                data.save()
                messages.success(request, "Role created Successfully")
                return redirect("roles")
        else:
            form = RoleForm()
            return render(request,"roles_form.html",{'form':form})
        
def view_role(request,pk):
    if request.user.is_authenticated:
        form = RoleForm()
        record = Role.objects.get(id=pk)
        return render(request, "view_roles.html",{'record': record,'form':form})
    else:
        messages.success('you not logged in')
        return redirect('index')
    
def delete_role(request, pk):
    if request.user.is_authenticated:
        view_record = Role.objects.get(id=pk)
        view_record.delete()
        return redirect('roles')
    else:
        messages.success('you not logged in')
        return redirect('index')
    
def update_role(request,  pk):
    if request.user.is_authenticated:
        current_record = Role.objects.get(id=pk)
        form = RoleForm(request.POST or None,instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record Updated Successfully")
            return redirect('roles')
        return render(request, "update_role.html",{'form':form})
    else:
        messages.success('you not logged in')
        return redirect('index')
