from rest_framework import serializers
from .models import *

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Groups
        fields = "__all__"

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teams
        fields = "__all__"

class BusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Businesses 
        fields = "__all__"

class GManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupsManager 
        fields = "__all__"


class TManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamsManager
        fields = "__all__"


class BManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessesManager
        fields = "__all__"

class MessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Messages
        fields = "__all__"

class PunishmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Punishment
        fields = "__all__"