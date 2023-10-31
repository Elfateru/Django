from django.contrib.auth.models import Group
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, ListCreateAPIView
# from rest_framework.mixins import ListModelMixin, CreateModelMixin

from .serializers import GroupSerialiser, OrderSerialiser, ProductSerialiser

from shopapp.models import Order, Product


@api_view()
def hello_world_view(request: Request) -> Response:
    return Response({"message": "hello world"})


class GroupsListView(ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerialiser


#
class OrdersListView(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerialiser


class ProductsListView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerialiser
