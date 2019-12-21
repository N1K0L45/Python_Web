from django.conf.urls import url, include
from login.views import *

urlpatterns = [
    url(r"^login/$",login),
    url(r"^home/$",vista_log),
    url(r"^todo/$",todo),
    url(r"^nuevo/$",nuevoItem),
    url(r"^nuevo-director/$",nuevoDirector),
    url(r"^nuevo-actor/$",nuevoActor),
    url(r"^actores/$",Actores),
    url(r"^directores/$",Directores)
]
