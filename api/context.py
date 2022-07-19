
from django.utils.functional import cached_property
from api.dataloaders import Movies_DirectorLoader


class GQLContext:

    def __init__(self, request):
        self.request = request

    @cached_property
    def user(self):
        return self.request.user

    @cached_property
    def movies_loader(self):
        return Movies_DirectorLoader()
