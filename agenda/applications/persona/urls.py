from django.urls import path, re_path, include

from . import views

app_name = 'persona_app'

urlpatterns = [
    path(
        'personas/',
        views.PersonListView.as_view(),
        name='personas'
    ),
    path(
        'api/persona/lista/',
        views.PersonListApiView.as_view(),
        name='personas-rest'
    ),
    path(
        'lista/',
        views.PersonListView.as_view(),
        name='personas-lista'
    ),
    path(
        'api/persona/search/<kword>',
        views.PersonSearchApiView.as_view(),
        name='personas-search'
    ),
    path(
        'api/persona/create',
        views.PersonCreateApiView.as_view(),
        name='personas-create'
    ),
    path(
        'api/persona/detail/<pk>',
        views.PersonDetailApiView.as_view(),
        name='personas-detail'
    ),
    path(
        'api/persona/delete/<pk>',
        views.PersonDeleteApiView.as_view(),
        name='personas-delete'
    ),
    path(
        'api/persona/update/<pk>',
        views.PersonUpdateApiView.as_view(),
        name='personas-update'
    ),
    path(
        'api/persona/up-de/<pk>',
        views.PersonUpDeApiView.as_view(),
    ),
    path(
        'api/personas',
        views.PersonApiLista.as_view(),
    ),
    path(
        'api/reuniones',
        views.ReunionApiLista.as_view(),
    ),
    path(
        'api/reuniones-link',
        views.ReunionApiListaLink.as_view(),
    ),
    path(
        'api/personas/paginacion',
        views.PersonPaginacionListApiView.as_view(),
    ),
    path(
        'api/reunion/by-job',
        views.ReunionByPersonJob.as_view(),
    ),
]