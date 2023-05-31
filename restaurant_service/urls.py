from django.urls import path

from .views import (
    index,
    DishListView,
    DishDetailView,
    DishCreateView,
    DishUpdateView,
    DishDeleteView,
    CookListView,
    CookDetailView,
    CookCreateView,
    CookLicenseUpdateView,
    CookDeleteView,
    DishTypeListView,
    DishTypeCreateView,
    DishTypeUpdateView,
    DishTypeDeleteView,
    toggle_assign_to_dish,
)

app_name = "restaurant_service"

urlpatterns = [
    path("", index, name="index"),
    path(
        "dishtypes/",
        DishTypeListView.as_view(),
        name="dish_type-list"
    ),
    path(
        "dishtypes/create/",
        DishTypeCreateView.as_view(),
        name="dish_type-create"
    ),
    path(
        "dishtypes/<int:pk>/update/",
        DishTypeUpdateView.as_view(),
        name="dish_type-update"
    ),
    path(
        "dishtypes/<int:pk>/delete/",
        DishTypeDeleteView.as_view(),
        name="dish_type-delete"
    ),
    path(
        "dishes/",
        DishListView.as_view(),
        name="dish-list"
    ),
    path(
        "dishes/<int:pk>/",
        DishDetailView.as_view(),
        name="dish-detail"
    ),
    path(
        "dishes/create/",
        DishCreateView.as_view(),
        name="dish-create"
    ),
    path(
        "dishes/<int:pk>/update/",
        DishUpdateView.as_view(),
        name="dish-update"
    ),
    path(
        "dishes/<int:pk>/delete/",
        DishDeleteView.as_view(),
        name="dish-delete"
    ),
    path(
        "dishes/<int:pk>/toggle-assign/",
        toggle_assign_to_dish,
        name="toggle-dish-assign"
    ),
    path(
        "cooks/",
        CookListView.as_view(),
        name="cook-list"
    ),
    path(
        "cooks/create/",
        CookCreateView.as_view(),
        name="cook-create"
    ),
    path(
        "cooks/<int:pk>/",
        CookDetailView.as_view(),
        name="cook-detail"
    ),
    path(
        "cooks/<int:pk>/update/",
        CookLicenseUpdateView.as_view(),
        name="cook-update"
    ),
    path(
        "cooks/<int:pk>/delete/",
        CookDeleteView.as_view(),
        name="cook-delete"
    ),
]
