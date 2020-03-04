from django.db.models import Q
from rest_framework import generics, filters
from rest_framework.pagination import PageNumberPagination

from users.serializer import UserSerializer
from .models import User

# Create your views here.


class UsersListView(generics.ListCreateAPIView):

    serializer_class = UserSerializer
    pagination_class = PageNumberPagination
    paginate_by_param = 'limit'
    ordering_fields = '__all__'
    sort_fields = ('age', '-age', 'first_name', '-first_name', 'last_name', '-last_name',
                   'company_name', '-company_name', 'city', '-city', 'zip', '-zip', 'email',
                   '-email', 'web', '-web')

    def get_queryset(self):
        queryset = User.objects.all().order_by('id')
        if self.request.query_params.get('name'):
            queryset = queryset.filter(
                Q(first_name__icontains=self.request.query_params.get('name')) |
                Q(last_name__icontains=self.request.query_params.get('name'))
            )
        if self.request.query_params.get('sort', '') in self.sort_fields:
            sort_param = self.request.query_params.get('sort')
            if sort_param == 'age':
                queryset = queryset.order_by('-dob')
            elif sort_param == '-age':
                queryset = queryset.order_by('dob')
            else:
                queryset = queryset.order_by(sort_param)
        return queryset

    @property
    def paginator(self):
        """
        The paginator instance associated with the view, or `None`.
        """
        if not hasattr(self, '_paginator'):
            if self.pagination_class is None:
                self._paginator = None
            else:
                self._paginator = self.pagination_class()
                self.paginator.page_size_query_param = self.paginate_by_param
        return self._paginator


class UserView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
