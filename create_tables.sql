/* RUN JUST THESE THREE LINES THEN RECONNECT TO THE agile DATABASE */
create role agile_admin with password 'password';
create database agile with owner agile_admin;
alter role agile_admin with login;

create table company (id serial primary key, name text, created timestamp without time zone default now(), last_modified timestamp without time zone default now());

create table sprint(id serial, company_id integer references company, name text, created timestamp without time zone default now(), last_modified timestamp without time zone default now());
