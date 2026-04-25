from django.urls import path
from .views import (ArticleListView, 
                    ArticleDetailView, 
                    ArticleCreateView,)

urlpatterns = [
    path('', ArticleListView.as_view(), name='article_list'),
    path('articulos/<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
    path('articulos/crear/', ArticleCreateView.as_view(), name='article-create'),
]

# <int:pk> es un parámetro que se pasará a la vista para identificar el artículo específico que se desea mostrar.
# int es de numero entero y pk es de primary key, es decir, el identificador único de cada artículo en la base de datos (clave primaria).