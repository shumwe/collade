from django.db import models
from taggit.managers import TaggableManager
from taggit.models import TaggedItemBase
from django.template.defaultfilters import slugify
from django.contrib.auth import get_user_model
from django.urls import reverse
User = get_user_model()

class TutorialAppBaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
def tutorial_upload_path(instance, filename):
    return "tutorials/{0}/{1}".format(instance, filename)

class TaggedTutorial(TaggedItemBase):
    content_object = models.ForeignKey('Tutorial', on_delete=models.CASCADE)
    
class Tutorial(TutorialAppBaseModel):
    title = models.CharField(max_length=155)
    slug = models.SlugField(unique=True, max_length=160)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    featured_image = models.ImageField(upload_to=tutorial_upload_path)
    content = models.TextField()
    tags = TaggableManager(through=TaggedTutorial)
    publish = models.BooleanField(default=True)
    views = models.PositiveIntegerField(blank=True, null=True, editable=False)
    
    def __str__(self):
        return f"{self.title}"
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse(
            'tutorial_detail', kwargs={
                'year': self.created.strftime('%Y'),
                'month': self.created.strftime('%m'),
                'day': self.created.strftime('%d'),
                'author':self.author,'slug': self.slug
                }
        )
    
    class Meta:
        ordering = ['-created',]
        
class Favourite(TutorialAppBaseModel):
    fav_tutorial = models.ForeignKey(Tutorial, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favourites')
    
    def __str__(self):
        return f"{self.fav_tutorial} - {self.user.username}"
    
    class Meta:
        ordering = ['-created',]