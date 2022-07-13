import numpy as np
import pandas as pd
import operator as op

class Die: 
    # This class is to draw a die with a list of “faces”, and W weights, and can be rolled to select a face.  
    n_rolls = 1
    
    def __init__(self, arrays):
        self.faces = arrays
        self.weights = [1]* len(self.faces)
        self.my_probs = [i/sum(self.weights) for i in self.weights]
        self.die = pd.DataFrame({
            'face': self.faces,
            'weights': self.my_probs
        })      
          
    #This returns the new frame of die and weights;
    def change_weight(self, face_id, new_weight): 
        if face_id in self.faces:
            if isinstance(new_weight,(int, float)) == True:
                face_index = self.faces.index(face_id)
                self.weights[face_index] = new_weight
                self.my_probs = [i/sum(self.weights) for i in self.weights]
                self.die = pd.DataFrame({
                     'face': self.faces,
                     'weights': self.my_probs
                 })
            else: 
                print("invalid weight")
        else:
            print("Out of the face range")
                      
    #This returns the results;
    def roll_die(self, n_rolls=1):
        results = []
        for i in range(n_rolls):
            result = self.die.face.sample(weights=self.die.weights).values[0]
            results.append(result)
        return pd.Series(results) 

    def show_current(self):
        return self.die

class Game: 
    # This class is to draw m dices with n times, and return the results of drawing.  
    n_rolls = 1
    m_dices = 3
    
    def __init__(self,arrays):
        self.dieobj = arrays
        
    def play(self, n_rolls, m_dices):
        # This returns the results of rolling m dices n times.
        self.n_rolls = n_rolls  
        self.m_dices = m_dices
        results_nm = []
        for i in range(self.m_dices):
            class1 = Die(self.dieobj)
            result_nm = class1.roll_die(n_rolls)
            results_nm.append(result_nm)
        self.results = pd.DataFrame(results_nm).unstack().to_frame()
        self.results = self.results.reset_index()
        self.results.columns = ['num_rolls', 'num_dices','Face_rolled']
        self.results.num_rolls += 1 
        self.results.num_dices += 1
        return self.results
  
    def show(self, Form):
        #This transforms the results of the method play. To use this method, 'play' has to run firstly.
        if Form == 'N':
            return self.results.set_index(['num_rolls', 'num_dices'])
        elif Form == 'W':       
            return self.results.set_index(['num_rolls'])
        else:
            print('Invalid Option')
           
        
class Analyzer: 
    # This class returns the analysis of results, with drawing m dices in n rolls.
    
    def __init__(self,results):
        self.dierus = results
        
    def jackpot(self):
        #This returns the times that all dices have the same face, where only one unique face is obtained.
        self.group_nvals = list(self.dierus.groupby('num_rolls')['Face_rolled'].nunique())
        return op.countOf(self.group_nvals,1)
    
    def combo(self):
        #This returns the times of each face_rolled.
        counts = pd.Series(self.dierus['Face_rolled']).value_counts()
        return pd.DataFrame(counts).sort_values(by=['Face_rolled'])
        
    def faceper(self):
        #This returns the times of each face in each roll.
        self.counts_faceroll = self.dierus.groupby(['num_rolls', 'Face_rolled']).count()
        self.counts_faceroll.columns = ['times_rolls']
        
if __name__ == '__main__':
    
    test_object = ([1,2, 3])