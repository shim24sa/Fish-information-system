delimiter //
create PROCEDURE IF NOT EXISTS fish_db.findNearest(
    IN _Species_Data_ID int,
    IN _dist DOUBLE,
    IN _lim int
)
DETERMINISTIC
BEGIN
-- constats
DECLARE _deg2rad DOUBLE DEFAULT PI()/180;
DECLARE _dist2lat DOUBLE DEFAULT 111.1;
-- lat and lon for the rectangle 
DECLARE lon1  DOUBLE;
DECLARE lon2  DOUBLE;
DECLARE lat1  DOUBLE;
DECLARE lat2  DOUBLE;
DECLARE _lon DOUBLE;
DECLARE _lat DOUBLE;
SELECT Start_Longitude,Start_Latitude INTO _lon,_lat FROM fishes_table as ft WHERE _Species_Data_ID = ft.Species_Data_ID;

set lon1  = _lon*_deg2rad-_dist/ABS(COS(_lat*_deg2rad)*_dist2lat);
set lon2  = _lon*_deg2rad+_dist/ABS(COS(_lat*_deg2rad)*_dist2lat);
set lat1 = _lat-(dist/_dist2lat); set lat2 = _lat+(dist/_dist2lat);
-- main query
select destination.*,   GCDist(origin.Start_Latitude,origin.Start_Longitude,destination.Start_Latitude,destination.Start_Longitude) as distance
    FROM  fishes_table as destination ,fishes_table as  origin
    WHERE origin.Species_Data_ID = _Species_Data_ID
    AND destination.Start_Longitude between lon1 and lon2 
    and destination.Start_Latitude between lat1 and lat2 
having distance < _dist ORDER BY Distance limit _lim;
end //
delimiter ;
