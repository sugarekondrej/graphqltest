from turtle import title
from typing_extensions import Required
import graphene 

from graphene_django.types import DjangoObjectType
from  api import models
class MovieType(DjangoObjectType):
    class Meta:
        model = models.Movies

    movie_age=graphene.String()

    def resolve_movie_age(self,info):
        return "old movie" if self.year < 2000 else "New movie"

class DirectorType(DjangoObjectType):
    class Meta:
        model = models.Director

class Query(graphene.ObjectType):
    all_movies = graphene.List(MovieType)
    movie = graphene.Field(MovieType,id = graphene.Int(),title = graphene.String())
    all_directors = graphene.List(DirectorType)

    def resolve_all_movies(self,info,**kwargs):
        return models.Movies.objects.all()

    def resolve_all_directors(self,info,**kwargs):
        return models.Director.objects.all()
    
    def resolve_movie(self,info,**kwargs):
        id = kwargs.get("id")
        title = kwargs.get("title")
        if id is not None:

            return models.Movies.objects.get(pk=id)
        
        if title is not None:

            return models.Movies.objects.get(title=title)
        
        return None
class MovieCreateMutation(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        year = graphene.Int(required=True)

    movie = graphene.Field(MovieType)

    def mutate(self, info, title, year):
        movie = models.Movies.objects.create(title=title, year=year)

        return MovieCreateMutation(movie=movie)
class MovieUpdateMutation(graphene.Mutation):
    class Arguments:
        title = graphene.String()
        year = graphene.Int()
        id = graphene.ID(required=True)
    movie = graphene.Field(MovieType)

    def mutate(self,info,id,title,year):
        movie = models.Movies.objects.get(pk=id)
        if title is not None:
            movie.title = title
        if year is not None:
            movie.year = year
        movie.save()
        return MovieUpdateMutation(movie=movie)
class MovieDeleteMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
    movie = graphene.Field(MovieType)
    def mutate(self,info,id):
        movie=models.Movies.objects.get(pk=id)
        movie.delete()
class Mutation:
    create_movie = MovieCreateMutation.Field()
    update_movie = MovieUpdateMutation.Field()
    remove_movie= MovieDeleteMutation.Field()