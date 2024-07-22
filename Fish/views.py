from drf_yasg.utils import swagger_auto_schema
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.decorators import action,api_view,permission_classes
from rest_framework.viewsets import ViewSet
from drf_yasg import openapi
from django.shortcuts import get_object_or_404
from .serializers import GCD_serializer,waterbodies_serializer,Species_serializer,GCD_IN_SERIALIZER
from .models import get_GCD,get_image,waterbodies,species,find_nearest
from rest_framework.permissions import IsAuthenticated

@swagger_auto_schema(method="GET",manual_parameters=[openapi.Parameter("name",openapi.IN_PATH,description="Name of the Image",type=openapi.TYPE_STRING)])
@api_view(["GET"])
def Image_view(request,name):
    person_details = get_image(name)
    if person_details:
        return Response(person_details)
    else:
        return Response({'error': f"Person with name '{name}' not found."}, status=404)

@swagger_auto_schema(method="GET",manual_parameters=[openapi.Parameter("id",openapi.IN_PATH,description="Spescies_id of the given Fish",type=openapi.TYPE_NUMBER)])
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def Nearest(request,pk=None):
    print(pk)
    res = find_nearest(pk)
    data= {"results":[]}
    for i in res:
        data["results"].append({
        "Species_Data_ID":i[0],
        "Species":i[1],
        "Number_Captured":i[2],
        "Date":i[3],
        "Waterbody_Name":i[4],
        "Waterbody_Type":i[5],
        "Start_Latitude":i[6],
        "Start_Longitude":i[7],
        "distance":i[8]
    })
    return Response(data)

Species_param1 = openapi.Parameter("species_id1",openapi.IN_BODY,description="Name of the Image",type=openapi.TYPE_STRING)
Species_param2 = openapi.Parameter("species_id2",openapi.IN_BODY,description="Name of the Image",type=openapi.TYPE_STRING)
@swagger_auto_schema(method="POST",operation_description="retrive  Distence between two fish species",
                     request_body=GCD_IN_SERIALIZER,
                      responses={201:openapi.Response('respspecies_id2onse description',GCD_serializer),404: 'Species not found'})
@api_view(["POST"])
def GCD_View(request):
    species_id1 = request.data['species_id1']
    species_id2 = request.data['species_id2']
    data = get_GCD(species_id1,species_id2) 
    print(data)
    serializer = GCD_serializer(data=data)
    if(serializer.is_valid()):
        return  Response(serializer.data)
    else:
        return Response(serializer.errors)
class waterBodies_View(ViewSet):
    def list(self,request):
        queryset = waterbodies.objects.all()
        serilizer =waterbodies_serializer(queryset,many=True)
        return Response(serilizer.data)
    @swagger_auto_schema(
        operation_description="Get Water_body",
        responses={200: waterbodies_serializer}
    )
    def retrive(self,request,pk=None):
        queryset = waterbodies.objects.all()[:10]
        water_body=get_object_or_404(queryset,pk=pk)
        serializer = waterbodies_serializer(water_body)
        return Response(serializer.data)

class Species_View(ViewSet):
    def list(self,request):
        queryset =species.objects.all()[:10]
        print(queryset)
        serilizer =Species_serializer(queryset,many=True)
        return Response(serilizer.data)
    def retrive(self,pk=None):
        queryset = waterbodies.objects.all()
        water_body=get_object_or_404(queryset,pk=pk)
        serializer = Species_serializer(water_body)
        return Response(serializer.data)