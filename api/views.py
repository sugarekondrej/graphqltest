from django.shortcuts import render

# Create your views here.
from django.utils.functional import cached_property
from graphene_django.views import GraphQLView
from api.dataloaders import Movies_DirectorLoader
from api.context import GQLContext


class CustomGraphQLView(GraphQLView):
    def get_context(self, request):
        return GQLContext(request)
