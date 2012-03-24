from tastypie.resources import ModelResource
from recipes.models import Recipe

class RecipeResource(ModelResource):
    class Meta:
        queryset = Recipe.objects.all()
        resource_name = 'recipes'
        allowed_methods = ['get']
        include_resource_uri = False

    def alter_list_data_to_serialize(self, request, data_dict):
        if isinstance(data_dict, dict):
            if 'meta' in data_dict:
                #Get rid of the meta object
                del(data_dict['meta'])
        
        return data_dict

