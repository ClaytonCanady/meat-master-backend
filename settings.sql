-- settings.sql
CREATE DATABASE bbq_api;
CREATE USER bbq_apiuser
WITH PASSWORD 'bbq_api';
GRANT ALL PRIVILEGES ON DATABASE bbq_api TO bbq_apiuser;