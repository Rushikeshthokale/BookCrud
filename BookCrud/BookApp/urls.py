
from django.urls import path
from BookApp import views
from django.conf.urls.static import static,settings
urlpatterns = [
   path('home',views.homePage),
   path('register',views.register),
   path('delete/<bookid>',views.deleteBook),
   path('update/<bookid>',views.updateBook),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)