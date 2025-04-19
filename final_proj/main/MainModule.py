import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from dao.VirtualArtGalleryImpl import VirtualArtGalleryImpl
from entity.Artwork import Artwork
from entity.Gallery import Gallery
from exception.ArtWorkNotFoundException import ArtWorkNotFoundException

def print_menu():
    print("\n=== Virtual Art Gallery Menu ===")
    print("1. Add Artwork")
    print("2. Get Artwork by ID")
    print("3. Update Artwork")
    print("4. Delete Artwork")
    print("5. Search Artworks")
    print("6. Add to Favorites")
    print("7. Remove from Favorites")
    print("8. View Favorite Artworks")
    print("9. Add Gallery")
    print("10. Update Gallery")
    print("11. Remove Gallery")
    print("12. Search Galleries")
    print("13. Exit")

def main():
    gallery = VirtualArtGalleryImpl()

    def print_artworks_table():
        cursor = gallery.conn.cursor()
        cursor.execute("select * from Artwork")
        rows = cursor.fetchall()
        print("\n Updated Artwork Table:")
        for row in rows:
            print(row)

    def print_galleries_table():
        cursor = gallery.conn.cursor()
        cursor.execute("select * from Gallery")
        rows = cursor.fetchall()
        print("\n Updated Gallery Table:")
        for row in rows:
            print(row)

    def print_favourites_tables():
        cursor=gallery.conn.cursor()
        cursor.execute("select * from User_favourite_artwork")
        rows=cursor.fetchall()
        print("\n Updated Gallery Table:")
        for row in rows:
            print(row)

    while True:
        print_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Title: ")
            description = input("Description: ")
            date = input("Creation Date (YYYY-MM-DD): ")
            medium = input("Medium: ")
            image_url = input("Image URL: ")
            artist_id = int(input("Artist ID: "))

            artwork = Artwork(title=title, description=description, creation_date=date,
                              medium=medium, image_url=image_url, artist_id=artist_id)
            if gallery.add_artwork(artwork):
                print("Artwork added successfully.")
                print_artworks_table()
            else:
                print("Failed to add artwork.")

        elif choice == '2':
            try:
                aid = int(input("Enter Artwork ID: "))
                artwork = gallery.get_artwork_by_id(aid)
                print(vars(artwork))
            except ArtWorkNotFoundException as e:
                print(e)

        elif choice == '3':
            try:
                aid = int(input("Enter Artwork ID to update: "))
                title = input("New Title: ")
                description = input("New Description: ")
                date = input("New Creation Date (YYYY-MM-DD): ")
                medium = input("New Medium: ")
                image_url = input("New Image URL: ")
                artist_id = int(input("New Artist ID: "))

                artwork = Artwork(artwork_id=aid, title=title, description=description,
                                  creation_date=date, medium=medium, image_url=image_url, artist_id=artist_id)
                if gallery.update_artwork(artwork):
                    print("Artwork updated successfully.")
                    print_artworks_table()
                else:
                    print("Failed to update artwork.")
            except ArtWorkNotFoundException as e:
                print(e)

        elif choice == '4':
            aid = int(input("Enter Artwork ID to delete: "))
            if gallery.remove_artwork(aid):
                print("Artwork deleted.")
                print_artworks_table()
            else:
                print("Failed to delete artwork.")

        elif choice == '5':
            keyword = input("Enter keyword to search: ")
            results = gallery.search_artworks(keyword)
            for art in results:
                print(vars(art))

        elif choice == '6':
            uid = int(input("Enter User ID: "))
            aid = int(input("Enter Artwork ID: "))
            if gallery.add_artwork_to_favorite(uid, aid):
                print("Artwork added to favorites.")
                print_favourites_tables()
            else:
                print("Failed to add favorite.")

        elif choice == '7':
            uid = int(input("Enter User ID: "))
            aid = int(input("Enter Artwork ID: "))
            if gallery.remove_artwork_from_favorite(uid, aid):
                print("Removed from favorites.")
                print_favourites_tables()
            else:
                print("Failed to remove.")

        elif choice == '8':
            uid = int(input("Enter User ID: "))
            favs = gallery.get_user_favorite_artworks(uid)
            for art in favs:
                print(vars(art))
        
        elif choice == '9':
            name = input("Gallery Name: ")
            desc = input("Description: ")
            loc = input("Location: ")
            curator_id = int(input("Curator (Artist ID): "))
            hours = input("Opening Hours: ")
            gallery_obj = Gallery(name=name, description=desc, location=loc, curator_id=curator_id, opening_hours=hours)
            if gallery.add_gallery(gallery_obj):
                print("Gallery added.")
                print_galleries_table()
            else:
                print("Failed to add Gallery.")

        elif choice == '10':
            gid = int(input("Gallery ID to update: "))
            name = input("New Name: ")
            desc = input("New Description: ")
            loc = input("New Location: ")
            curator_id = int(input("New Curator ID: "))
            hours = input("New Hours: ")
            gallery_obj = Gallery(gallery_id=gid, name=name, description=desc, location=loc, curator_id=curator_id, opening_hours=hours)
            if gallery.update_gallery(gallery_obj):
                print("Gallery updated.")
                print_galleries_table()
            else:
                print("Failed to update Gallery.")

        elif choice == '11':
            gid = int(input("Gallery ID to delete: "))
            if gallery.remove_gallery(gid):
                print("Gallery deleted.")
                print_galleries_table()
            else:
                print("Failed to delete Gallery.")

        elif choice == '12':
            keyword = input("Search Gallery Keyword: ")
            galleries = gallery.search_galleries(keyword)
            for g in galleries:
                print(vars(g))

        elif choice == '13':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
