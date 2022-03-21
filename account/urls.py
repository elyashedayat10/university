from django.urls import path
from .views import AdminCrateView, AdminUserUpdateView, AdminUserDeleteView, UserLoginView, UserLogoutView, \
    AdminListView

app_name = "account"

urlpatterns = [
    path('admin-create/', AdminCrateView.as_view(), name="admin_create"),
    path('admin-update/<int:id>/', AdminUserUpdateView.as_view(), name="admin_update"),
    path('admin-delete/<int:id>/', AdminUserDeleteView.as_view(), name="admin_delete"),
    path('admin-list/', AdminListView.as_view(), name="admin_list"),
    path('login/', UserLoginView.as_view(), name="login"),
    path('logout/', UserLogoutView.as_view(), name="logout"),
]
