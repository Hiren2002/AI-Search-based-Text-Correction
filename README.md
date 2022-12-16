# AI-Search-based-Text-Correction
Automated Correction of Incorrectly Recognised Text


Local Beam Search Algorithm is implemented to Search thorugh different sentences to find correct text of given incorrect text .

Conda Installation : https://docs.conda.io/en/latest/miniconda.html

Following command should create the required conda environment using environment.yml file provide with the code :

```conda env create -f environment.yml```

Command to Run the program :

```python run.py -src data/input.txt -tar data/pred.txt -tm 2```

It will run your solution for each string in the data/input.txt file and write the solutions to data/pred.txt. For each input sentence, your program is allowed to run for at most 2 seconds (as specified by the -tm option). 
