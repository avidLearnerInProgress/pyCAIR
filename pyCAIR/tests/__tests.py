import os, cv2
import unittest as ut

import notdoneyet as ndy
import seam_carve as sc

base_path = os.path.dirname(os.path.abspath(__file__))

class Test1(ut.TestCase):

	def test_user_input(self):

		#check for all params
		result1 = ndy.user_input(1, 0.4, 1, './images/fig2.jpg', 0)

		#check for some or 0 params
		result2 = ndy.user_input(1, 0.4, 1)

		result3 = ndy.user_input()

		self.assertEqual(result1, 5) 
		self.assertEqual(result2, 5) 
		self.assertEqual(result3, 5)