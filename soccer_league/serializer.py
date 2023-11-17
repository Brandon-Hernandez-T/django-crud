from rest_framework import serializers
from .models import Category, Player, Team


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        # Para traer campos en especifico, hacer uno por uno
        # fields = ('id', 'title', 'description', 'done')
        # Si se requiere todo, basta con esta linea
        fields = '__all__'


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        # Para traer campos en especifico, hacer uno por uno
        # fields = ('id', 'title', 'description', 'done')
        # Si se requiere todo, basta con esta linea
        fields = '__all__'


class PlayerSerializer(serializers.ModelSerializer):
    # Se agrega tambien lo que este en team
    team = TeamSerializer()

    class Meta:
        model = Player
        # Para traer campos en especifico, hacer uno por uno
        # fields = ('id', 'title', 'description', 'done')
        # Si se requiere todo, basta con esta linea
        fields = '__all__'
