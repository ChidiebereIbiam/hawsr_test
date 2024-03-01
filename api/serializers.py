from rest_framework import serializers
from .models import User, Worker, Building, Company, Office, UserOffice


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id','email', 'phone', 'first_name', 'last_name', 'role', 'password']
        
        
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class WorkerSerializer(serializers.ModelSerializer):
    user_details = UserSerializer(source='user', read_only=True)
    class Meta:
        model = Worker
        fields = ['id','user', 'user_details','worker_type', 'is_busy']
        
class CompanySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Company
        fields = ['id','name', 'phone']

class BuildingSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Building
        fields = ['id','company', 'name', 'floor_count']

class OfficeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Office
        fields = ['id','building', 'floor', 'number']

class UserOfficeSerializer(serializers.ModelSerializer):
    user_details = UserSerializer(source='user', read_only=True)
    office_details = OfficeSerializer(source="office", read_only=True)
    
    class Meta:
        model = UserOffice
        fields = ['id','office','office_details', 'user', 'user_details']
