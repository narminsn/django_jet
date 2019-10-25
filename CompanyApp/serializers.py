from rest_framework import serializers
from .models import PersonsModel, AccountsModel, ProjectsModel

class PersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = PersonsModel
        fields = ["full_name", 'id']


class AccountsSerializer(serializers.ModelSerializer):

    class Meta:
        model = AccountsModel
        fields = ["name", 'id']



class ProjectsSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProjectsModel
        fields = ["name", 'id']