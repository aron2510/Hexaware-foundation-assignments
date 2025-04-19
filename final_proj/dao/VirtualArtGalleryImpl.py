import pyodbc
from dao.IVirtualArtGallery import IVirtualArtGallery
from entity.Artwork import Artwork
from entity.Gallery import Gallery
from util.DBConnUtil import DBConnUtil
from exception.ArtWorkNotFoundException import ArtWorkNotFoundException
from exception.UserNotFoundException import UserNotFoundException

class VirtualArtGalleryImpl(IVirtualArtGallery):
    def __init__(self):
        self.conn = DBConnUtil.get_connection()
        self.cursor = self.conn.cursor()

    def add_artwork(self, artwork: Artwork) -> bool:
        try:
            query = """INSERT INTO Artwork (Title, Description, CreationDate, Medium, ImageURL, ArtistID)
                       VALUES (?, ?, ?, ?, ?, ?)"""
            self.cursor.execute(query, artwork.title, artwork.description, artwork.creation_date,
                                artwork.medium, artwork.image_url, artwork.artist_id)
            self.conn.commit()
            
            return True
        except Exception as e:
            print(f"Failed to add artwork: {e}")
            return False

    def get_artwork_by_id(self, artwork_id: int) -> Artwork:
        self.cursor.execute("SELECT * FROM Artwork WHERE ArtworkID = ?", artwork_id)
        row = self.cursor.fetchone()
        if row:
            return Artwork(*row)
        else:
            raise ArtWorkNotFoundException(f"Artwork with ID {artwork_id} not found.")

    def search_artworks(self, keyword: str) -> list[Artwork]:
        self.cursor.execute("SELECT * FROM Artwork WHERE Title LIKE ?", f"%{keyword}%")
        rows = self.cursor.fetchall()
        return [Artwork(*row) for row in rows]

    def update_artwork(self, artwork: Artwork) -> bool:
        try:
            query = """UPDATE Artwork
                       SET Title = ?, Description = ?, CreationDate = ?, Medium = ?, ImageURL = ?, ArtistID = ?
                       WHERE ArtworkID = ?"""
            self.cursor.execute(query, artwork.title, artwork.description, artwork.creation_date,
                                artwork.medium, artwork.image_url, artwork.artist_id, artwork.artwork_id)
            if self.cursor.rowcount == 0:
                raise ArtWorkNotFoundException(f"No artwork found with ID {artwork.artwork_id}")
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Failed to update artwork: {e}")
            return False

    def remove_artwork(self, artwork_id: int) -> bool:
        try:
            self.cursor.execute("DELETE FROM Artwork WHERE ArtworkID = ?", artwork_id)
            if self.cursor.rowcount == 0:
                raise ArtWorkNotFoundException(f"No artwork found with ID {artwork_id}")
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Failed to remove artwork: {e}")
            return False

    def add_artwork_to_favorite(self, user_id: int, artwork_id: int) -> bool:
        try:
            self.cursor.execute("SELECT * FROM Users WHERE UserID = ?", user_id)
            if not self.cursor.fetchone():
                raise UserNotFoundException(f"User with ID {user_id} does not exist.")
            self.cursor.execute("SELECT * FROM Artwork WHERE ArtworkID = ?", artwork_id)
            if not self.cursor.fetchone():
                raise ArtWorkNotFoundException(f"Artwork with ID {artwork_id} does not exist.")
            self.cursor.execute("INSERT INTO User_Favourite_Artwork (UserID, ArtworkID) VALUES (?, ?)",
                                user_id, artwork_id)
            self.conn.commit()
            return True
        except (UserNotFoundException, ArtWorkNotFoundException) as e:
            print(e)
            return False
        except Exception as e:
            print("Failed to add to favourites:", e)
            return False

    def remove_artwork_from_favorite(self, user_id: int, artwork_id: int) -> bool:
        try:
            self.cursor.execute("SELECT 1 FROM Users WHERE UserID = ?", user_id)
            if not self.cursor.fetchone():
                raise UserNotFoundException(f"User with ID {user_id} does not exist.")
            self.cursor.execute("SELECT 1 FROM Artwork WHERE ArtworkID = ?", artwork_id)
            if not self.cursor.fetchone():
                raise ArtWorkNotFoundException(f"Artwork with ID {artwork_id} does not exist.")
            self.cursor.execute("DELETE FROM User_Favourite_Artwork WHERE UserID = ? AND ArtworkID = ?", user_id, artwork_id)
            self.conn.commit()
            return True

        except (UserNotFoundException, ArtWorkNotFoundException) as e:
            print(e)
            return False

        except Exception as e:
            print("Failed to remove from favourites:", e)
            return False


    def get_user_favorite_artworks(self, user_id: int) -> list[Artwork]:
        try:
            self.cursor.execute("SELECT 1 FROM Users WHERE UserID = ?", user_id)
            if not self.cursor.fetchone():
                raise UserNotFoundException(f"User with ID {user_id} does not exist.")
            query = """SELECT a.* FROM Artwork a
                    JOIN User_Favourite_Artwork ufa ON a.ArtworkID = ufa.ArtworkID
                    WHERE ufa.UserID = ?"""
            self.cursor.execute(query, user_id)
            rows = self.cursor.fetchall()
            return [Artwork(*row) for row in rows]

        except UserNotFoundException as e:
            print(e)
            return []

        except Exception as e:
            print("Failed to retrieve favorite artworks:", e)
            return []


    def add_gallery(self, gallery: Gallery) -> bool:
        try:
            query = """INSERT INTO Gallery (Name, Description, Location, CuratorID, OpeningHours)
                       VALUES (?, ?, ?, ?, ?)"""
            self.cursor.execute(query, gallery.name, gallery.description, gallery.location,
                                gallery.curator_id, gallery.opening_hours)
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Failed to add gallery: {e}")
            return False

    def update_gallery(self, gallery: Gallery) -> bool:
        try:
            query = """UPDATE Gallery
                       SET Name = ?, Description = ?, Location = ?, CuratorID = ?, OpeningHours = ?
                       WHERE GalleryID = ?"""
            self.cursor.execute(query, gallery.name, gallery.description, gallery.location,
                                gallery.curator_id, gallery.opening_hours, gallery.gallery_id)
            self.conn.commit()
            return self.cursor.rowcount > 0
        except Exception as e:
            print(f"Failed to update gallery: {e}")
            return False

    def remove_gallery(self, gallery_id: int) -> bool:
        try:
            self.cursor.execute("DELETE FROM Gallery WHERE GalleryID = ?", gallery_id)
            self.conn.commit()
            return self.cursor.rowcount > 0
        except Exception as e:
            print(f"Failed to remove gallery: {e}")
            return False

    def search_galleries(self, keyword: str) -> list:
        try:
            self.cursor.execute("SELECT * FROM Gallery WHERE Name LIKE ?", f"%{keyword}%")
            rows = self.cursor.fetchall()
            return [Gallery(*row) for row in rows]
        except Exception as e:
            print(f"Failed to search galleries: {e}")
            return []
