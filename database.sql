show databases;
create database movies;
use movies;
alter table movie add release_date char(13) default(00-00-0000);
select *from movie;
insert into movie values(JR17,JAILAVAKUSA,K.S.RAVINDRA,N.KALYAN RAM,N.T.R ARTS,DEVI SRI PRASAD,N.T.R,RAASHI KHANNA/NIVEDHA THOMAS,DRAMA,150CRS,21-09-2017);