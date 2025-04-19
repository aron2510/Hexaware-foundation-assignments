import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import unittest
from dao.VirtualArtGalleryImpl import VirtualArtGalleryImpl
from entity.Gallery import Gallery

class TestGalleryManagement(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.gallery_service = VirtualArtGalleryImpl()

    def test_add_gallery(self):
        gallery = Gallery(name="Test Gallery", description="Test Desc", location="Test Location", curator_id=1, opening_hours="9-5")
        result = self.gallery_service.add_gallery(gallery)
        self.assertTrue(result)
        
    def test_search_gallery(self):
        search_result = self.gallery_service.search_galleries("Test Gallery")
        self.assertGreater(len(search_result), 0)
        found = any(g.name == "Test Gallery" for g in search_result)
        self.assertTrue(found)

    def test_update_gallery(self):
        search_result = self.gallery_service.search_galleries("Test Gallery")
        if not search_result:
            self.skipTest("No gallery found to update.")
        g = search_result[0]
        g.name = "Updated Test Gallery"
        updated = self.gallery_service.update_gallery(g)
        self.assertTrue(updated)

    def test_remove_gallery(self):
        search_result = self.gallery_service.search_galleries("Updated Test Gallery")
        if not search_result:
            self.skipTest("No gallery found to delete.")
        g = search_result[0]
        deleted = self.gallery_service.remove_gallery(g.gallery_id)
        self.assertTrue(deleted)

if __name__ == '__main__':
    unittest.main()
