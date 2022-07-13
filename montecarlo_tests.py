import unittest
import numpy as np
import pandas as pd
import operator as op
from montecarlo import Die
from montecarlo import Game
from montecarlo import Analyzer


class MontecarloTestSuite(unittest.TestCase):
    
    def test_1_Die_initial(self): 
        # add an array and test the initial inputs.  
        class1 = Die(["a","b","c"])
        self.assertTrue(isinstance(class1.die,pd.DataFrame))
    
    def test_2_Die_changeweight(self): 
        # change the specific face_id and test the new weight.  
        class1 = Die(["a","b","c"])
        class1.change_weight("a", 3)
        expected = 3
        self.assertEqual(class1.weights[0], expected)  
        
    def test_3_Die_rolldie(self):
        # roll the dice for one time and check the length of the result.
        class1 = Die(['a', 'b', 'c'])
        expected = 3 
        self.assertEqual(len(class1.roll_die(3)), expected)
        
    def test_4_Game_initial(self): 
        # add an array and test the initial inputs.  
        class2 = Game([1,2,3,4])
        self.assertTrue(isinstance(class2.dieobj, list))
        
    def test_5_Game_play(self): 
        # roll the dice for three time and check the size of the result.
        class2 = Game([1,2,3,4])
        expected = 12
        self.assertEqual(len(class2.play(3, 4)), expected)

    def test_6_Game_show(self): 
        # check whether the result is a dataframe
        class2 = Game([1,2,3,4])
        class2.play(3,4)
        self.assertTrue(isinstance(class2.show('N'), pd.DataFrame))
        
    def test_7_Analyzer_jackpot(self):
        class2 = Game([1,2,3,4])
        class3 = Analyzer(class2.play(3,4))
        self.assertFalse(isinstance(class3.jackpot(), float))
        
    def test_7_Analyzer_combo(self):
        class2 = Game([1, 2, 3, 4, 5, 6])
        class3 = Analyzer(class2.play(3,4))
        self.assertTrue(isinstance(class3.combo(), pd.DataFrame))
      
        
    def test_8_Analyzer_faceper(self):
        class2 = Game([1, 2, 3, 4, 5, 6])
        class3 = Analyzer(class2.play(3,4))
        r = class3.faceper()
        self.assertTrue(isinstance(class3.counts_faceroll, pd.DataFrame))
            
if __name__ == '__main__':  
    unittest.main(verbosity=3)