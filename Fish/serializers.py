from rest_framework import serializers
from .models import waterbodies,species

class Species_serializer(serializers.ModelSerializer):
        class Meta:
                model=species
                fields= "__all__"
class waterbodies_serializer(serializers.ModelSerializer):
        class Meta:
                model=waterbodies
                fields= "__all__"
class GCD_serializer(serializers.Serializer):
        Start_Latitude_org  =  serializers.DecimalField(decimal_places=2,max_digits=20)
        Start_Longitude_org =  serializers.DecimalField(decimal_places=2,max_digits=20)
        Start_Longitude_dest=  serializers.DecimalField(decimal_places=2,max_digits=20)
        Start_Latitude_dest =  serializers.DecimalField(decimal_places=2,max_digits=20)
        Distence = serializers.DecimalField(decimal_places=2,max_digits=20)
class NearestItem_serializer(serializers.Serializer) :
        Species_Data_ID=  serializers.IntegerField()
        Species=  serializers.CharField()
        Number_Captured= serializers.IntegerField()
        Date=serializers.DateField()
        Waterbody_Name= serializers.CharField()
        Waterbody_Type= serializers.CharField()
        Start_Latitude= serializers.DecimalField(decimal_places=2,max_digits=20)
        Start_Longitude=serializers.DecimalField(decimal_places=2,max_digits=20)
        distance=serializers.DecimalField(decimal_places=2,max_digits=20)
class NearestItems_serializer(serializers.Serializer):
        items=  serializers.ListField(child=NearestItem_serializer())
class GCD_IN_SERIALIZER(serializers.Serializer):
        species_id1=serializers.DecimalField(decimal_places=2,max_digits=20)
        species_id2=serializers.DecimalField(decimal_places=2,max_digits=20)