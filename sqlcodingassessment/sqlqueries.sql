--1)
Create database Petpals;
use petpals;

--2)
create table pets(petid int primary key,name varchar(50), age int,breed varchar(50),
type varchar(50),availableforadoption bit,ownerid int null,
shelterID int foreign key references shelters(shelterid));

select * from pets;

create table shelters(shelterid int primary key,name varchar(50),location varchar(50));

--3)
create table donations(donationid int primary key,donorname varchar(50),
donartype varchar(50),donaramount decimal(10,2),donaritem varchar(50),
donationdate datetime,shelterid int foreign key references shelters(shelterid));

create table adoptionevents(eventid int primary key,eventname varchar(50),eventdate datetime,location varchar(50));

create table participants(participantid int primary key,participantname varchar(50),participanttype varchar(50),eventid int foreign key references adoptionevents(eventid));

insert into pets values(1,'hachi', 2, 'rotwieler', 'Dog', 1, NULL,1),(2,'murphy', 2, 'indo', 'Cat', 1, NULL,2),(3,'moger', 3, 'doberman', 'Dog', 0, 1,3),
(4,'max', 1, 'Persian', 'Cat', 1, NULL,4),(5,'timmy', 4, 'shitzu', 'Dog', 1, NULL,5);

insert into shelters values(1,'furr Shelter', 'San Francisco, CA'),(2,'Paw Haven', 'Seattle, WA'),(3,'Denver paws', 'Denver, CO'),
(4,'Meow paradise', 'Boston, MA'),(5,'Safe Haven for Pets', 'Miami, FL');

insert into donations values(1,'alex', 'Cash', 100.00, NULL, '2025-04-01 11:30:00', 1),(2,'beckham', 'Item', NULL, 'Dog Food', '2023-03-06 12:05:00', 2),(3,'ethan', 'Cash', 50.00, NULL, '2021-03-03 20:00:00', 3),
(4,'daniel', 'Item', NULL, 'Cat Toys', '2025-03-04 06:09:00', 4),(5,'larusso', 'Cash', 75.00, NULL, '2024-03-05 19:25:00', 5);

insert into adoptionevents values(1,'Pet Fair', '2020-03-15 15:10:00', 'Central Park, NY'),(2,'Adopt-Paws', '2022-04-11 11:00:00', 'Los Angeles Shelter'),
(3,'Rescue Day', '2024-05-15 10:30:00', 'Chicago Community Center'),(4,'Forever Home Event', '2023-06-25 12:00:00', 'Adoption Center'),
(5,'Furry Festival', '2022-07-24 15:00:00', 'Phoenix Pet Expo');

insert into participants values(1,'kingsley', 'Adopter', 1),(2,'Furr Shelter', 'Shelter', 2),(3,'John', 'Adopter', 3),
(4,'Roxy', 'Adopter', 4),(5,'Meow paradise', 'Shelter', 5);

--5)
select name,age,breed,type from pets where availableforadoption=1;

--6)
select p.participantname,p.participanttype from participants as p join adoptionevents as a on p.eventid=a.eventid where p.eventid=2;

--7)
create procedure updateshelterinfo @name varchar(50), @loc varchar(50),@id int
as
begin 
update shelters set name=@name, location=@loc where shelterid=@id;
end;
exec updateshelterinfo pawtails, chennai,1;
select * from shelters;

--8)
select s.name,d.donaramount from shelters as s join donations as d on s.shelterid=d.shelterid;

--9)
select name,age,breed,type from pets where ownerid is NULL;

--10)
select year(donationdate) as years,month(donationdate) as months,sum(donaramount) as totaldonations from donations group by year(donationdate) ,month(donationdate);

--11)
select distinct breed from pets where age between 1 and 3 or age>5;

--12)
select p.name,p.breed,s.name,s.location from pets as p join shelters as s on p.shelterid=s.shelterid where availableforadoption=1;

--13)
select sum(p.participantid) as totalparticipants from participants as p join adoptionevents as a on p.eventid=a.eventid where location='Central Park, NY';

--14)
select distinct breed from pets where age between 1 and 5;

--15)
select name,type,breed from pets where availableforadoption=1;

--16)
select p.name as Pet_Name, pt.participantname as Adopter_Name from participants pt join adoptionevents ae on pt.eventid = ae.eventid join pets p on p.petid = ae.eventid 
where pt.participanttype = 'Adopter'

--17)
select s.name,count(p.petid) as count from shelters s join pets p on s.shelterid=p.petid where p.availableforadoption=1 group by s.name;

--18)
insert into pets values(6,'mike', 3, 'rotwieler', 'Dog', 1, NULL,1);
select p1.petid as Pet1_ID, p1.name as Pet1_Name, p2.petid as Pet2_ID, p2.name as Pet2_Name, p1.breed, p1.shelterID from pets p1 join pets p2 on p1.shelterID = p2.shelterID 
and p1.breed = p2.breed and p1.petid < p2.petid;

--19)
select s.name, a.eventname from shelters as s cross join adoptionevents as a;

--20)
select top 1 s.shelterid, s.name as sheltername, count(pe.petid) as count from pets pe join shelters s on pe.ShelterID = s.ShelterID join participants p ON p.ParticipantID = pe.PetID
where p.ParticipantType = 'Adopter' group by s.shelterid, s.name order by count desc;
