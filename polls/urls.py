from django.urls import path
from . import views

app_name = 'polls' #How does one make it so that Django knows \
                   #which app view to create for a url when using the {% url %} template tag?
urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
# The path() function is passed four arguments, two required: route and view, and two optional: kwargs, and name.