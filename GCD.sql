delimiter //
create if not exists function   fish_db.GCDist(
	_lat1 DOUBLE,
    _lon1 DOUBLE,
	_lat2 DOUBLE,
    _lon2 DOUBLE
    ) RETURNS DOUBLE
	DETERMINISTIC
    CONTAINS SQL  -- SQL but does not read or write
    SQL SECURITY INVOKER  -- No special privileges granted
    BEGIN
    DECLARE _deg2rad DOUBLE DEFAULT PI() / 180000;-- For scaled by 1e4 to MEDIUMINT
    DECLARE _rlat1 DOUBLE DEFAULT _deg2rad * _lat1;
    DECLARE _rlat2 DOUBLE DEFAULT _deg2rad * _lat2;
	DECLARE _rlon1 DOUBLE DEFAULT _deg2rad * _lon1;
    DECLARE _rlon2 DOUBLE DEFAULT _deg2rad * _lon2;
    -- compute as if earth's radius = 1.0
    -- x1,x2 = lat y1,y2 = lon
    -- cos(x2)*cos(y2)-cos(x1)cos(y1)=x
    -- cos(x2)*sin(y2)-cos(x1)sin(y1)=y
    -- sin(x2)-sin(x1)=z
    -- angle_c = sqrt(x^2+y^2+z^2)
    DECLARE _x     DOUBLE DEFAULT COS(_rlat2)*COS(_rlon2) - COS(_rlat1)* COS(_rlon1);
    DECLARE _y     DOUBLE DEFAULT COS(_rlat2)*SIN(_rlon2)- COS(_rlat1)* sin(_rlon1);
    DECLARE _z     DOUBLE DEFAULT SIN(_rlat2) - SIN(_rlat1);
    DECLARE _n     DOUBLE DEFAULT SQRT(
                        _x * _x +
                        _y * _y +
                        _z * _z    );
    RETURN _n;
    END;
delimiter ;

