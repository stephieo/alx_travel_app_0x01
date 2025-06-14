from django.shortcuts import render
from rest_framework import viewsets
from .models import User, Listing, Booking
from .serializers import ListingSerializer, BookingSerializer
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.

class ListingViewSet(viewsets.ModelViewSet):
    """This class contains all the varous views connected to the CRUD actions for this model.
    the basic setup is specifying the queryset to use for any returned data and the serializer handling any input/output"""
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['location', 'price_per_night', 'max_guests']



class BookingViewSet(viewsets.ModelViewSet):
    """This class contains all the varous views connected to the CRUD actions for this model.
    the basic setup is specifying the queryset to use for any returned data and the serializer handling any input/output"""
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['start_date', 'listing__title', 'status']

