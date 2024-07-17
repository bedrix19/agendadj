from django.shortcuts import render

from django.views.generic import ListView, TemplateView

from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    DestroyAPIView, 
    UpdateAPIView, # RetrieveUpdateAPIView muestra los datos actuales
    RetrieveUpdateDestroyAPIView,
)

from .models import Person, Reunion, Hobby
from .serializers import (
    PersonSerializers,
    PersonSerializers2,
    PersonSerializers3,
    PersonaSerializers,
    ReunionSerializer,
    ReunionSerializer2,
    ReunionSerializerLink,
    PersonPagination,
    CountJobSerializers,
    )

class PersonListView(ListView):
    model = Person
    template_name = "persona/personas.html"
    context_object_name = 'personas'

    def get_queryset(self):
        return Person.objects.all()

class PersonListApiView(ListAPIView):
    serializer_class = PersonSerializers    

    def get_queryset(self):
        return Person.objects.all()

class PersonListView(TemplateView):
    template_name='persona/lista.html'

class PersonSearchApiView(ListAPIView):

    serializer_class = PersonSerializers    

    def get_queryset(self):
        kword = self.kwargs['kword']
        return Person.objects.filter(
            full_name__icontains=kword,
        )

class PersonCreateApiView(CreateAPIView):

    serializer_class = PersonSerializers

class PersonDetailApiView(RetrieveAPIView):

    serializer_class = PersonSerializers
    queryset = Person.objects.all()

class PersonDeleteApiView(DestroyAPIView):

    serializer_class = PersonSerializers
    queryset = Person.objects.all()

class PersonUpdateApiView(UpdateAPIView):

    serializer_class = PersonSerializers
    queryset = Person.objects.all()

class PersonUpDeApiView(RetrieveUpdateDestroyAPIView):

    serializer_class = PersonSerializers
    queryset = Person.objects.all()

class PersonApiLista(ListAPIView):

    serializer_class = PersonSerializers3

    def get_queryset(self):
        return Person.objects.all()

class ReunionApiLista(ListAPIView):

    serializer_class = ReunionSerializer2

    def get_queryset(self):
        return Reunion.objects.all()

class ReunionApiListaLink(ListAPIView):

    serializer_class = ReunionSerializerLink

    def get_queryset(self):
        return Reunion.objects.all()

class PersonPaginacionListApiView(ListAPIView): # PAGINACION

    serializer_class = PersonSerializers
    pagination_class = PersonPagination

    def get_queryset(self):
        return Person.objects.all()

class ReunionByPersonJob(ListAPIView):

    serializer_class = CountJobSerializers

    def get_queryset(self):
        return Reunion.objects.cantidad_reuniones_job()
    
