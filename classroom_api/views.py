from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from classes.models import Classroom
from .serializers import ListSerializer, DetailSerializer, CreateUpdateSerializer 

# Create your views here.

class ListView(ListAPIView):
	queryset = Classroom.objects.all()
	serializer_class = ListSerializer

class DetailView(RetrieveAPIView):
	queryset = Classroom.objects.all()
	serializer_class = DetailSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'class_id'

class CreateView(CreateAPIView):
	serializer_class = CreateUpdateSerializer

	def perform_create(self, serializer):
		serializer.save(teacher=self.request.user)

class UpdateView(RetrieveUpdateAPIView):
	queryset = Classroom.objects.all()
	serializer_class = CreateUpdateSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'class_id'

class DeleteView(DestroyAPIView):
	queryset = Classroom.objects.all()
	serializer_class = ListSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'class_id'