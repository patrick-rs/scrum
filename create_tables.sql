/* RUN JUST THESE THREE LINES THEN RECONNECT TO THE scrum DATABASE */
create role scrum_admin with password 'password';
create database scrum with owner scrum_admin;
alter role scrum_admin with login;

jcreate table company (id serial primary key, name text not null, created timestamp without time zone default now(), last_modified timestamp without time zone default now());

create table sprint(id serial primary key, company_id integer references company(id) not null, name text not null, description text, created timestamp without time zone default now(), last_modified timestamp without time zone default now());

create table task(id serial, company_id integer not null references company(id), sprint_id integer references sprint(id), name text, description text, story_points integer, created timestamp without time zone default now(), last_modified timestamp without time zone default now());
