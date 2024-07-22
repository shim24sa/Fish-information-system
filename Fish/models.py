from django.db import connection,models
from os import getenv
import requests

# Create your models here.
class species(models.Model):
        Species_Data_ID= models.IntegerField(primary_key=True)
        Species= models.CharField(max_length=255)
        Number_Captured=models.IntegerField()
        Date=models.DateField()
        class meta:
              ordering=["Date"]

class waterbodies(models.Model):
        id =             models.IntegerField(primary_key=True)
        Waterbody_Name = models.CharField(max_length=255)
        Waterbody_Type = models.CharField(max_length=255)
        Start_Latitude = models.FloatField()
        Start_Longitude= models.FloatField()

def  get_GCD(Species_Data_ID1,Species_Data_ID2):
    cursor = connection.cursor()
    params=list((Species_Data_ID1,Species_Data_ID2))
    cursor.execute("SELECT round(org.Start_Latitude,2) ,round(org.Start_Longitude,2),round(dest.Start_Longitude,2),round(dest.Start_Latitude,2),round(GCDist(org.Start_Latitude,org.Start_Longitude,dest.Start_Latitude,dest.Start_Longitude),2) from fishes_table org join fishes_table dest on org.Species_Data_ID=%s and dest.Species_Data_ID=%s;",params=params)
    rows = cursor.fetchone()
    if(rows):
        data = {
                "Start_Latitude_org":rows[0],
                "Start_Longitude_org":rows[1],
                "Start_Longitude_dest":rows[2],
                "Start_Latitude_dest":rows[3],
                "Distence":rows[4]
        }
        return  data
    else: 
         return {"error":"Species NotFound"}

def find_nearest(Species_Data_ID,dist=0.7,limit=10):
    cursor = connection.cursor()
    sql_param =[Species_Data_ID,dist,limit]
    cursor.execute("call findNearest(%s,%s,%s)",sql_param)
    rows = cursor.fetchall()

    return rows

def get_image(name):
    url ="https://api.serply.io/v1/image/q={query}".format(query=name)
    headers = {
        "x-api-key":getenv("serply"),
        "x-proxy-location":"US",
        "Content-type":'application/json'
    }
    res = requests.get(url=url,headers=headers)
    data = res.json()
    return {"url":data["image_results"][0]["image"]["src"]}