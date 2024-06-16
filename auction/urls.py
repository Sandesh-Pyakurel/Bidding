from django.urls import path
from .views import (
    user_signup, 
    login_view,
    home_view, 
    logout_view,
    auctioner_view,
    add_auction_view,
    )

urlpatterns = [
    path('signup/', user_signup, name='signup'),
    path('login/', login_view, name='login'),
    path('', home_view, name='home'),
    path('logout/', logout_view, name='logout'),
    path('auctioner/', auctioner_view, name='auctioner'),
    path('auctioner/add', add_auction_view, name='add-auction'),
]
