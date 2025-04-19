from abc import ABC, abstractmethod
from entity.Artwork import Artwork
from entity.Gallery import Gallery

class IVirtualArtGallery(ABC):
    @abstractmethod
    def add_artwork(self, artwork: Artwork) -> bool:
        pass

    @abstractmethod
    def update_artwork(self, artwork: Artwork) -> bool:
        pass

    @abstractmethod
    def remove_artwork(self, artwork_id: int) -> bool:
        pass

    @abstractmethod
    def get_artwork_by_id(self, artwork_id: int) -> Artwork:
        pass

    @abstractmethod
    def search_artworks(self, keyword: str) -> list[Artwork]:
        pass

    @abstractmethod
    def add_artwork_to_favorite(self, user_id: int, artwork_id: int) -> bool:
        pass

    @abstractmethod
    def remove_artwork_from_favorite(self, user_id: int, artwork_id: int) -> bool:
        pass

    @abstractmethod
    def get_user_favorite_artworks(self, user_id: int) -> list[Artwork]:
        pass

    @abstractmethod
    def add_gallery(self, gallery: Gallery) -> bool:
        pass

    @abstractmethod
    def update_gallery(self, gallery: Gallery) -> bool:
        pass

    @abstractmethod
    def remove_gallery(self, gallery_id: int) -> bool:
        pass

    @abstractmethod
    def search_galleries(self, keyword: str) -> list:
        pass
