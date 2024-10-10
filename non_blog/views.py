from django.shortcuts import render
from .models import Trustees, Leading_Team, Advisory

# Create your views here.
def about_us(request):
    return render(request,'non-blog/about/about.html')

def advisory_board(request):
    advisory = Advisory.objects.all()
    return render(request,'non-blog/about/advisory_board.html', {'advisory': advisory})

def leadership(request):
    leading_team = Leading_Team.objects.all()
    return render(request,'non-blog/about/leadership_team.html',{'leading_team': leading_team})

def trustees(request):
    trustees = Trustees.objects.all()
    return render(request,'non-blog/about/trustees.html',{'trustees':trustees,})

def vision_and_mission(request):
    return render(request,'non-blog/about/vision_and_mission.html')

# what we do section
def colleges_covered(request):
    return render(request,'non-blog/what-we-do/colleges_covered.html')

def educational_seminars(request):
    return render(request,'non-blog/what-we-do/educational_seminars.html')

def experience(request):
    return render(request,'non-blog/what-we-do/experience.html')

def free_education(request):
    return render(request,'non-blog/what-we-do/free_education.html')

def our_work(request):
    return render(request,'non-blog/what-we-do/our_work.html')

def our_reach(request):
    return render(request,'non-blog/what-we-do/our_reach.html')

def school_covered(request):
    return render(request,'non-blog/what-we-do/schools_covered.html')

def research(request):
    return render(request,'non-blog/what-we-do/research.html')

def donation(request):
    return render(request,'forms/donations.html')


# sample
# def our_work(request):
    # return render(request,'non-blog//our_work.html')



