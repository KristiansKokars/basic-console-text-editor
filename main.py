# Izveidoja: Kristiāns Kokars
from textfunctions import TextFunctions #importējam mūsu funkcijas

print("1: New File\n2: Open File\n3: Read File\n4: Write to File\n5: Append\n6: Editing Mode\n7: Exit") #izprintē opcijas
user_choice = input() #gaidam lietotāju input priekš izvēlnes

while user_choice != "7" and user_choice != "!exit": #programma mūžīgi atkārtosies līdz lietotājs ir izvēlējies opciju iziet
  
  if user_choice == "1": #1. opcija, izveidojam jaunu failu
    TextFunctions.clearScreen() #notīra ekrānu
    TextFunctions.newFile()

  elif user_choice == "2": #2. opcija, atveram failu
    TextFunctions.clearScreen() #notīra ekrānu
    TextFunctions.openFile() # atver failu, paprasot lietotājam to vārdu, ja tāds neeksistē vai kaut kāda iemesla dēļ nevar atvērt- izmet kļūdu un turpina izvēlnes ciklu
  
  elif user_choice == "3": #3. opcija, izlasam atvērto failu
    TextFunctions.clearScreen() #notīra ekrānu
    TextFunctions.readFile() # izlasa informāciju no atvērtā faila, ja fails nav atvērts - izmanto openFile() funkciju, lai vienu atvērtu
  
  elif user_choice == "4": #4. opcija, rakstam failā
    TextFunctions.clearScreen() #notīra ekrānu
    TextFunctions.showOpenFile() #parāda tikmēr atvērto failu
    TextFunctions.writeFile() # raksta atvērtajā failā informāciju no jauna, ja fails nav atvērts - izmanto openFile() funkciju, lai vienu atvērtu

  elif user_choice == "5": #5. opcija, appendojam failu
    TextFunctions.clearScreen() #notīra ekrānu
    TextFunctions.showOpenFile() #parāda tikmēr atvērto failu
    TextFunctions.appendFile()
  
  elif user_choice == "6": #6. opcija, rediģējam failu
    TextFunctions.clearScreen() #notīra ekrānu
    TextFunctions.showOpenFile() #parāda tikmēr atvērto failu
    TextFunctions.editingMode()

  else: #ja lietotājs ievadīja opciju kas mums nav, tad par to paziņo
    print("Such an option doesn't exist. Select from the existing options using it's number.\n")
  TextFunctions.showOpenFile() #pārāda atvērto failu izvēlnē
  print("\n1: New File\n2: Open File\n3: Read File\n4: Write to File\n5: Append\n6: Editing Mode\n7: Exit") #izprintē opcijas
  user_choice = input() #gaidam lietotāju input priekš izvēlnes