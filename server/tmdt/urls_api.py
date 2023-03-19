from django.urls import include, path

users_urlpatterns = [
    path("users/", include("users.api.urls_api")),
]

address_urlpatterns = [
    path("address/", include("address.api.urls_api")),
]

# profiles_urlpatterns = [
#     path("profiles/", include("apps.profiles.api.urls_api")),
# ]

orders_urlpatterns = [
     path("orders/", include("orders.api.urls_api")),
]

products_urlpatterns = [
     path("products/", include("products.api.urls_api")),
]

urlpatterns = [
    *users_urlpatterns,
    *address_urlpatterns,
    # *profiles_urlpatterns,
    *orders_urlpatterns,
    *products_urlpatterns,
]