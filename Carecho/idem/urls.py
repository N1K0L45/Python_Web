from django.conf.urls import url, include
from idem.views import *

urlpatterns = [
    url(r"^idem/$",idem)
]
