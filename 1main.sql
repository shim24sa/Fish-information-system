drop database if exists fish_db;
create database if not exists fish_db;
use fish_db;
CREATE TABLE IF NOT EXISTS fishes_table (
  Species_Data_ID INT,
  Species VARCHAR(255),
  Number_Captured INT,
  Date DATETIME,
  Waterbody_Name VARCHAR(255),
  Waterbody_Type VARCHAR(255),
  Start_Latitude DOUBLE,
  Start_Longitude DOUBLE
);
insert into fish_species(Species_Data_ID,
  Species ,
  Number_Captured, 
  Date)
  select *
 from species;

insert into fish_waterbodies(id,
  Waterbody_Name , 
  Waterbody_Type ,
  Start_Latitude ,
  Start_Longitude)
 select *
 from waterbodies;