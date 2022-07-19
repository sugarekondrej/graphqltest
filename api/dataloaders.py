from collections import defaultdict
from promise import Promise
from promise.dataloader import DataLoader
from api.models import Movies


class Movies_DirectorLoader(DataLoader):
    def batch_load_fn(self, director_ids):
        movie_director = defaultdict(list)

        for movie in Movies.objects.filter(director_id__in=director_ids).iterator():
            movie_director[movie.director_id].append(movie)

        return Promise.resolve([movie_director.get(director_id, [])
                                for director_id in director_ids])
