How to Use:

Using Python 3.9.12
Using Java XX.XX.XX

In windows open CMD and navigate to the download directory

for Taxes:
	Type in 'python MainUi.py 'Tax <Status> <Year> <Amount>' ' ie: python MainUi.py Tax S 2020 100000
	
	Status:
		S = single
		J = Join	
		H = Head
		
	Year: 
		2020
		2021
		
	Amount:
		Amount of money rounded to the nearest dollar


For Translation:
	Type in 'python MainUi.py Translate <Language> <Word>'
	ie python MainUi.py Translate Fr cat
	
	Language:
		Fr - French
		De - German
		Es - Spanish
		
	Word:
		Word to Translate
		
To Change error Message language:
	Go to Service.txt
	Edit the Line that looks like -> Error,'msgEng.txt'
	To use English -> Error,'msgEng.txt'
	To use German -> Error,'msgGer.txt'