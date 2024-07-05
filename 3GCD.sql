delimiter //
create if not exists function fish_db.GCDist(
	_lat1 DOUBLE,
    _lon1 DOUBLE,
	_lat2 DOUBLE,
    _lon2 DOUBLE
    ) RETURNS DOUBLE
	DETERMINISTIC
    CONTAINS SQL  -- SQL but does not read or write
    SQL SECURITY INVOKER  -- No special privileges granted
    BEGIN
    DECLARE _radius_earth DOUBLE DEFAULT 6371;
    DECLARE _deg2rad DOUBLE DEFAULT PI() / 180;
    DECLARE _dlat  DOUBLE DEFAULT _deg2rad *( _lat2 - _lat1);
    DECLARE _dlon DOUBLE DEFAULT __deg2rad * (_lon2 - _lon1);
	DECLARE _haversin DOUBLE DEFAULT POWER(SIN(_dlat)/2,2)
                                           +COS(ABS(_lat1)*_deg2rad)
                                           *COS(ABS(_lat2)*_deg2rad)
                                           *POWER(SIN(_dlon)/2,2);
    RETURN 2*ASIN(SQRT(_haversin))*_radius_earth;--re
    END;
delimiter ;

