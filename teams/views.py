from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import TeamForm
from .models import Team
# Create your views here.
def teams(request):
    records = Team.objects.all()
    return render(request, "teams.html",{'records': records})

def teamsform(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = TeamForm(request.POST)
            if form.is_valid():
                print(request.user)
                team_name = request.POST['team']
                team_manager = request.POST['team_manager']
                data = Team(team=team_name, team_manager= team_manager,created_by=request.user)
                data.save()
                messages.success(request, "Team Created Successfully")
                return redirect('teams')
            else:
                form = TeamForm()
                messages.success(request, "Form is InValid")
                return render(request, "teams_form.html",{'form': form})

        else:
            form = TeamForm()
            return render(request, "teams_form.html",{'form': form})


def view_role(request,pk):
    if request.user.is_authenticated:
        form = TeamForm()
        record = Team.objects.get(id=pk)
        return render(request, "view_team.html",{'record': record,'form':form})
    else:
        messages.success('you not logged in')
        return redirect('index')
    
def delete_role(request, pk):
    if request.user.is_authenticated:
        view_record = Team.objects.get(id=pk)
        view_record.delete()
        return redirect('teams')
    else:
        messages.success('you not logged in')
        return redirect('index')
    
def update_role(request,  pk):
    if request.user.is_authenticated:
        current_record = Team.objects.get(id=pk)
        form = TeamForm(request.POST or None,instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record Updated Successfully")
            return redirect('teams')
        return render(request, "update_team.html",{'form':form})
    else:
        messages.success('you not logged in')
        return redirect('index')

