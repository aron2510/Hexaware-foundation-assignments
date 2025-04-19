import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest
from dao.VirtualArtGalleryImpl import VirtualArtGalleryImpl
from entity.Artwork import Artwork
from exception.ArtWorkNotFoundException import ArtWorkNotFoundException

class TestArtworkManagement(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.service = VirtualArtGalleryImpl()

    def test_add_artwork(self):
        artwork = Artwork(title="UnitTest Piece", description="Painted for unit test",
                          creation_date="2025-04-01", medium="Watercolor",
                          image_url="http://example.com/unittest.jpg", artist_id=1)
        result = self.service.add_artwork(artwork)
        self.assertTrue(result)

    def test_search_artwork(self):
        results = self.service.search_artworks("UnitTest Piece")
        self.assertGreater(len(results), 0)

    def test_get_artwork_by_id(self):
        results = self.service.search_artworks("UnitTest Piece")
        if not results:
            self.skipTest("Artwork not available for ID fetch")
        art = results[0]
        fetched = self.service.get_artwork_by_id(art.artwork_id)
        self.assertEqual(fetched.title, "UnitTest Piece")

    def test_update_artwork(self):
        results = self.service.search_artworks("UnitTest Piece")
        if not results:
            self.skipTest("No artwork to update")
        art = results[0]
        art.title = "UnitTest Updated"
        updated = self.service.update_artwork(art)
        self.assertTrue(updated)

    def test_remove_artwork(self):
        results = self.service.search_artworks("UnitTest Updated")
        if not results:
            self.skipTest("No artwork to remove")
        art = results[0]
        deleted = self.service.remove_artwork(art.artwork_id)
        self.assertTrue(deleted)

    def test_get_invalid_artwork_raises_exception(self):
        with self.assertRaises(ArtWorkNotFoundException):
            self.service.get_artwork_by_id(-999)  

if __name__ == '__main__':
    unittest.main()
