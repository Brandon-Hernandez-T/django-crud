from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        # Para traer campos en especifico, hacer uno por uno
        #fields = ('id', 'title', 'description', 'done')
        # Si se requiere todo, basta con esta linea
        fields = '__all__'