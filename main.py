import unittest
from tests.testHomePage import TestHomePage

if __name__ == '__main__':
    
    home_page = unittest.TestLoader().loadTestsFromTestCase(TestHomePage)
    
    test_suite = unittest.TestSuite([home_page])
    
    unittest.TextTestRunner().run(test_suite)