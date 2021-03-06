from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from . import models


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Article
        exclude = ['gallery']


class CreatureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Creature
        fields = ['url', "genus","species", "feed"]

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = models.Article.objects.all()
    serializer_class = ArticleSerializer

class CreatureViewSet(viewsets.ModelViewSet):
    queryset = models.Creature.objects.all()
    serializer_class = CreatureSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('articles', ArticleViewSet)
router.register("creatures", CreatureViewSet)