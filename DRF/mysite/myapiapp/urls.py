from django.urls import path
from .views import hello_world_view, GroupsListView, OrdersListView, ProductsListView

app_name = "myapiapp"

urlpatterns = [
    path("hello/", hello_world_view, name="hello"),
    path("groups/", GroupsListView.as_view(), name="groups"),
    path("orders/", OrdersListView.as_view(), name="orders"),
    path("products/", ProductsListView.as_view(), name="products"),
]