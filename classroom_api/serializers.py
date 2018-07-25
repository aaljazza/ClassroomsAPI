from rest_framework import serializers
from classes.models import Classroom

class ListSerializer(serializers.ModelSerializer):
	class Meta:
		model= Classroom
		fields = ['subject','year','teacher']

class DetailSerializer(serializers.ModelSerializer):
	class Meta:
		model = Classroom
		fields = ['subject','year','name','teacher']

class CreateUpdateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Classroom
		fields = ['subject','year','name']
