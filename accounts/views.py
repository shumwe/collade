from django.shortcuts import render
from tutorials.models import Favourite, Tutorial

# Create your views here.
def profile(request):
    user = request.user
    user_fav_tutorials = Favourite.objects.filter(user=user)
    tutorials = Tutorial.objects.filter(publish=True).order_by('-created')
    
    favs = []
    for fav in user_fav_tutorials:
        for t in tutorials:
            if fav.fav_tutorial == t:
                favs.append(t)
     
    context = {
        'favs': favs,
    }
    return render(request, 'accounts/profile.html', context)