from rest_framework import serializers, pagination

from .models import Person, Reunion, Hobby

class PersonSerializers(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = (
            'id',
            'full_name',
            'job',
            'email',
        )

class PersonaSerializers(serializers.Serializer):
    id = serializers.IntegerField()
    full_name = serializers.CharField()
    job = serializers.CharField()
    email = serializers.EmailField()
    phone = serializers.CharField()
    activo = serializers.BooleanField(required=False)
    prueba = serializers.BooleanField(default=False)

class PersonSerializers2(serializers.ModelSerializer):
    
    activo = serializers.BooleanField(default=False)
    
    class Meta:
        model = Person
        fields = ('__all__')

class ReunionSerializer(serializers.ModelSerializer):
    
    persona = PersonSerializers()

    class Meta:
        model = Reunion
        fields = (
            'id',
            'fecha',
            'hora',
            'asunto',
            'persona',
        )

class HobbieSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Hobby
        fields = ('__all__')

class PersonSerializers3(serializers.ModelSerializer):
    
    hobbies = HobbieSerializers(many=True)

    class Meta:
        model = Person
        fields = (
            'id',
            'full_name',
            'job',
            'email',
            'phone',
            'hobbies',
            'created',
        )

class ReunionSerializer2(serializers.ModelSerializer):
    
    fecha_hora = serializers.SerializerMethodField()
    
    class Meta:
        model = Reunion
        fields = (
            'id',
            'fecha',
            'hora',
            'asunto',
            'persona',
            'fecha_hora',
        )

    def get_fecha_hora(self, obj): # el obj se refiere al item que estamos iterando ahora
        return str(obj.fecha) + ' | ' + str(obj.hora)

class ReunionSerializerLink(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Reunion
        fields = (
            'id',
            'fecha',
            'hora',
            'asunto',
            'persona',
        )
        extra_kwargs = {
            'persona':{
                'view_name':'persona_app:personas-detail',# La clase Hyperlink.. ya sabe que aqui referenciamos una clase RetrieveAPIView
                'lookup_field':'pk',
            } 
        }

class PersonPagination(pagination.PageNumberPagination):
    page_size = 5
    max_page_size = 50

class CountJobSerializers(serializers.Serializer):
    # los atributos se construyen dependiendo de los valores que pusismos en el Manager
    persona__job = serializers.CharField()
    cantidad = serializers.IntegerField()