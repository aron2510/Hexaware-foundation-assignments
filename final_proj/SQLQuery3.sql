create database Virtualartgallery1;
drop database Virtualartgallery1;
use Virtualartgallery1;
select * from sys.tables;
drop table Artist;
-- Artist Table
Create Table Artist (
    ArtistID Int Identity(1,1) Primary Key,
    Name Nvarchar(255) Not Null,
    Biography Text,
    BirthDate Date,
    Nationality Nvarchar(100),
    Website Nvarchar(255),
    ContactInfo Nvarchar(255)
);

-- Artwork Table
Create Table Artwork (
    ArtworkID Int Identity(1,1) Primary Key,
    Title Nvarchar(255) Not Null,
    Description Text,
    CreationDate Date,
    Medium Nvarchar(100),
    ImageURL Nvarchar(255),
    ArtistID Int Not Null,
    Foreign Key (ArtistID) References Artist(ArtistID) On Delete Cascade
);

-- User Table
Create Table Users (
    UserID Int Identity(1,1) Primary Key,
    Username Nvarchar(100) Unique Not Null,
    Password Nvarchar(255) Not Null,  
    Email Nvarchar(255) Unique Not Null,
    FirstName Nvarchar(100),
    LastName Nvarchar(100),
    DateOfBirth Date,
    ProfilePicture Nvarchar(255)
);

-- Gallery Table
Create Table Gallery (
    GalleryID Int Identity(1,1) Primary Key,
    Name Nvarchar(255) Not Null,
    Description Text,
    Location Nvarchar(255),
    CuratorID Int Null, 
    OpeningHours Nvarchar(255),
    Foreign Key (CuratorID) References Artist(ArtistID) On Delete Set Null
);


-- User Favorite Artworks (Many-to-Many)
Create Table User_Favourite_Artwork (
    UserID Int Not Null,
    ArtworkID Int Not Null,
    Primary Key (UserID, ArtworkID),
    Foreign Key (UserID) References Users(UserID) On Delete Cascade,
    Foreign Key (ArtworkID) References Artwork(ArtworkID) On Delete Cascade
);

-- Artwork in Gallery (Many-to-Many)
Create Table Artwork_Gallery (
    ArtworkID Int Not Null,
    GalleryID Int Not Null,
    Primary Key (ArtworkID, GalleryID),
    Foreign Key (ArtworkID) References Artwork(ArtworkID) On Delete Cascade,
    Foreign Key (GalleryID) References Gallery(GalleryID) On Delete Cascade
);

Insert Into Artist Values ('Leonardo da Vinci', 'Renaissance artist and inventor', '1452-04-15', 'Italian', 'https://davinci.com', 'leonardo@email.com'),
('Vincent van Gogh', 'Post-impressionist painter', '1853-03-30', 'Dutch', 'https://vangogh.com', 'vincent@email.com'),
('Pablo Picasso', 'Cubism pioneer', '1881-10-25', 'Spanish', 'https://picasso.com', 'picasso@email.com');

Insert Into Artwork Values ('Mona Lisa', 'Famous portrait painting', '1503-01-01', 'Oil on poplar panel', 'https://example.com/monalisa.jpg', 1),
('Starry Night', 'Depiction of a swirling night sky', '1889-06-01', 'Oil on canvas', 'https://example.com/starrynight.jpg', 2),
('Guernica', 'Political anti-war painting', '1937-04-26', 'Oil on canvas', 'https://example.com/guernica.jpg', 3);

Insert Into Users Values ('artlover1', 'P@ssw0rd!XyZ123', 'artlover1@email.com', 'Alice', 'Johnson', '1995-07-12', 'https://example.com/alice.jpg'),
('artfan2', 'S3cur3P@ss789$', 'artfan2@email.com', 'Bob', 'Smith', '1998-02-21', 'https://example.com/bob.jpg');

Insert Into Gallery Values('Renaissance Wonders', 'Showcasing famous Renaissance artworks', 'Florence, Italy', 1, '10 AM - 6 PM'),
('Modern Art Hub', 'Contemporary and modern art pieces', 'Paris, France', 3, '9 AM - 5 PM');

Insert Into Artwork_Gallery Values (1, 1),(2, 2),(3, 2);

Insert Into User_Favourite_Artwork Values (1, 1),(1, 2),(2, 3); 

ALTER TABLE User_Favorite_Artwork
ADD CONSTRAINT FK_User FOREIGN KEY (UserID) REFERENCES Users(UserID),
    CONSTRAINT FK_Artwork FOREIGN KEY (ArtworkID) REFERENCES Artwork(ArtworkID);
select * from Gallery;

select * from User_Favourite_Artwork;