from tastypie.resources import ModelResource, ALL_WITH_RELATIONS
from tastypie import fields
from api.models import UserDoc 
from tastypie.authorization import Authorization

class UserDocResource(ModelResource):
    class Meta:
        queryset = UserDoc.objects.all()
        resource_name = 'UserDoc'
        authorization = Authorization()




