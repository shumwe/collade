from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import redirect, render
from django.views.generic import CreateView, DetailView, ListView
from django.core.exceptions import ObjectDoesNotExist

from tutorials.models import Favourite, Tutorial


class TutorialListView(ListView):
    queryset = Tutorial.objects.filter(publish=True)
    template_name = 'tutorials/tutorials.html'
    context_object_name = 'objects'
    paginate_by = 12
    
class TutorialDetailView(DetailView):
    queryset = Tutorial.objects.filter(publish=True)
    template_name = 'tutorials/tutorial_detail.html'
    context_object_name = 'obj'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = self.get_object()
        context["related"] = Tutorial.objects.filter(
            publish=True, tags__in=obj.tags.all(),
        ).exclude(pk=obj.pk).order_by('-created')[:6]
        user = self.request.user
        if user.is_authenticated:
            context["is_fav"] = Favourite.objects.filter(user=user,fav_tutorial=obj).exists()
        return context

@login_required
def favourite_tutorials(request, slug):
    user = request.user
    tutorial = Tutorial.objects.get(slug=slug)
    try:
        fav = Favourite.objects.get(user=user, fav_tutorial=tutorial)
        fav.delete()
        messages.success(request, 'Removed from favourites!')
    except ObjectDoesNotExist:
        fav = Favourite(user=user, fav_tutorial=tutorial)
        fav.save()
        messages.success(request, 'Added to favourites!')
        
    return redirect(tutorial.get_absolute_url())