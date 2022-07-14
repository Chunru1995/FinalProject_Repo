# MetaData
```yaml
name: Chunru Zheng 
project: Montecarlo
```

# Synopsis
* **Installing:**
  - cd /Users/Christine/Desktop/DS/DS5100/DS5100-2022-06-RA/FinalProject_Repo/
  - pip install .
* **Importing:**
  - from montecarlo import montecarlo
* **Creating dice:**
  - Die_class = montecarlo.Die(['H', 'T'])
  - enter an array of the dice you want to roll, and returns the results of rolling one time as initialized.
* **Playing games:**
  - Game_class = montecarlo.Game(['H', 'T'])
  - Game1 = Game_class.play(1000,3)
* **Analyzing games:**
  - Ana_class1 = montecarlo.Analyzer(Game1)
  
# API description
### Class1
- **Die**: 
This class is to draw a die with a list of ?faces?, and W weights, and can be rolled to select a face. 

  - __init__(self, arrays):
  This initialize the arrays of dice, and return the faces, weights, and die.
    
  - change_weight(self, face_id, new_weight): 
  Enter the new face_id and new_weight, and this returns the new dataframe of die and weights. 
  
  - roll_die(self, n_rolls=1):
  This returns the results of rolling a dice for n_rolls times. 
  
  - show_current(self):
  This displays the current weights for each face. 

### Class2
* **Game**: 
This class is to draw m dices with n times, and return the results of drawing.    
Here I change to setting to choose m dices as you want, which make it easier for the senarios to change the number of dices.  
  
  - __init__(self,arrays):
   This initialize the faces of dice you want to roll.
   
  - play(self, n_rolls, m_dices):
   This returns the results of rolling m dices n times. Here I set the m_dice attribute to assign how many dices you want to roll and it will make things easier. 
   
  - show(self, Form):
   This transforms the results of the method play. To use this method, 'play' has to run firstly.

### Class3
* **Analyzer**: 
This class returns the analysis of results, with drawing m dices in n rolls.

  - __init__(self,results):
  
  - jackpot(self):
  This returns the times that all dices have the same face, where only one unique face is obtained.
  
  - combo(self):
  This returns the times of each face_rolled.
  
  - faceper(self):
  This returns the times of each face in each roll.

# Files in this repo:
- FinalProjectSubmissionTemplate.ipynb
- LICENSE
- README.md
- montecarlo_demo.ipynb
- montecarlo_results.txt
- montecarlo_tests.py
- montecarlo.py
- setup.py
- montecarlo:
  - __init__.py
  * __pycache__/
      * __init__.cpython-39.pyc
      * montecarlo.cpython-39.pyc




