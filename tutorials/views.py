from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import redirect, render
from django.views.generic import CreateView, DetailView, ListView
from django.core.exceptions import ObjectDoesNotExist
from taggit.models import Tag
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

class TutorialSearchView(ListView):
    model = Tutorial
    template_name = "tutorials/search.html"
    context_object_name = 'objects'
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        objects = Tutorial.objects.filter(
                title__icontains=query, publish=True
            ).order_by('-created')
        return objects
    
def tagged(request, tag_slug):
    tag = Tag.objects.get(slug=tag_slug)
    objects = Tutorial.objects.filter(
        tags=tag, publish=True
    )
    return render(request, 'tutorials/tagged.html', context={
        'tag':tag, "objects":objects
    })