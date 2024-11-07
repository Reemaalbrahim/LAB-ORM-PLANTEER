from . import views
from django.urls import path 

app_name = "plants_app"

urlpatterns = [
    path("all/", views.all_plants_view, name="all_plants_view"),
    path("<plant_id>/detail/", views.plants_detail_view, name="plants_detail_view"),
    path("new/", views.new_plants_view, name="new_plants_view"),
    path("<plant_id>/update/", views.update_plants_view, name="update_plants_view"),
    path("<plant_id>/delete/", views.delete_plants_view, name="delete_plants_view"),
    path("search/", views.search_plants_view, name="search_plants_view"),
]
