from django.conf.urls.defaults import patterns, include, url
from recipes.api.api import RecipeResource
from django.contrib import admin
admin.autodiscover()

recipe_resource = RecipeResource()

urlpatterns = patterns('',
    url(r'^api/', include(recipe_resource.urls)),
    url(r'^admin/', include(admin.site.urls)),
)
