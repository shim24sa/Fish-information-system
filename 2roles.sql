CREATE USER IF NOT EXISTS 'mahya'@'%' IDENTIFIED BY '201828Bar';
CREATE USER IF NOT EXISTS 'shima'@'%' IDENTIFIED BY 'Shima2024';
CREATE USER IF NOT EXISTS 'app'@'%' IDENTIFIED BY 'CT4WzxeLhHOwxTdoU1TThQzMpD3TwWp4';
CREATE ROLE IF NOT EXISTS 'Auth_developer','fish_admin','app';
REVOKE  ALL PRIVILEGES ON *.* FROM 'Auth_developer','fish_admin','app_role';
GRANT ALL PRIVILEGES ON fish_db.* TO  'app_role' ;

SELECT CONCAT("GRANT all PRIVILEGES ON db.", table_name, " TO Auth_developer;")
FROM information_schema.TABLES
WHERE table_schema = "fish_db" AND table_name <> "fish_table";

REVOKE ALL PRIVILEGES ON  fish_db.fishes_table TO 'Auth_developer';
GRANT ALL PRIVILEGES ON  fish_db.fishes_table TO 'fish_admin';
GRANT 'fish_admin' to  'mahya'@'%';
GRANT 'app_role' to 'app'@'%';
FLUSH PRIVILEGES;