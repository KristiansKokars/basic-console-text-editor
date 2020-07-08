# Izveidoju jaunu failu un klasi priekš funkcijām lai varētu importēt un galvenais kods izskatītos "tīrāks"
from texthelpfunctions import TextHelpFunctions
class TextFunctions: #es visu sametu klasē, lai ir vieglāk importēt
  openedFile = None #glabājam šeit mūsu atvērto faila vārdu kā global variable funkcijām
  ############################################################
  #################### GALVENĀS FUNKCIJAS ####################
  ############################################################
  # Mūsu galvenās funkcijas jeb opcijas priekš failu apstrādes

  def newFile(): #cenšās izveidot jaunu failu un automātiski to atver
    file_name = input("Creating a new file. Enter file name:") + ".txt" #izveido jaunu failu
    try: #cenšas izveidot failu, ja neizdodas tad programma nesalūzt bet paziņo problēmu un turpina darbību.
      current_file = codecs.open(file_name, "x", "utf-8") #cenšas uztaisīt programmu
      current_file.close() #aizver uzreiz, jo mums vienīgi vajadzēja uztaisīt
      TextFunctions.openedFile = file_name # atver jauno atvērto failu
      print("File succesfully created.")
      TextFunctions.newLine()
    except Exception as error: #ja ir kāda problēma, programma to noķer un arī pārādā specifisko kļūdu kas notika (priekš testēšanas)
      print("File couldn't be created. Does it already exist? Error:\n", error)
      TextFunctions.newLine()
  
  def readFile(): #izlasa atvērto failu
    TextFunctions.checkIfOpenFile() #pārbauda vai jau ir atvērts fails
    try: #cenšas izlasīt failu, ja neizdodas tad programma nesalūzt bet paziņo problēmu un turpina darbību.
      current_file = codecs.open(TextFunctions.openedFile, "r", "utf-8")
      print("\n", current_file.read(), sep ="") #izprintē izlasīto tekstu
      current_file.close()
      print("\nRead successful. Returning to main menu.")
    except Exception as error: #ja ir kāda problēma, programma to noķer un arī pārādā specifisko kļūdu kas notika (priekš testēšanas)
      print("File doesn't exist, or is unreadable. Error:\n", error)

  def writeFile(): #raksta atvertā failā jaunu tekstu
    TextFunctions.checkIfOpenFile() #pārbauda vai jau ir atvērts fails
    try: #cenšas rakstīt failā, ja neizdodas tad programma nesalūzt bet paziņo problēmu un turpina darbību.
      current_file = codecs.open(TextFunctions.openedFile, "w", "utf-8") #atver failu rakstīšanas modē
      write_text = input("Type Text, write !exit to exit this function: ") + "\n" #pievienojam jaunu rindu pēc ievadītā teksta
      while write_text != "!exit\n": #kamēr lietotājs nav izvēlejies iziet, tamēr turpinās rakstīšanas process. Un tā kā mēs pievienojaim input jaunu rindu, to arī jāpārbauda
        current_file.write(write_text) #raksta lietotāja ievadīto tekstu
        write_text = input("Type Text, write !exit to exit this function: ") + "\n"
      current_file.close()
      print("File writing finished. Returning to main menu.")
    
    except Exception as error: #ja ir kāda problēma, programma to noķer un arī pārādā specifisko kļūdu kas notika (priekš testēšanas)
      print("File doesn't exist or can't be wrote to. Error:\n", error)

  def appendFile(): #pievieno atvertā failā jaunu tekstu
    TextFunctions.checkIfOpenFile() #pārbauda vai jau ir atvērts fails
    try: #cenšas rakstīt failā, ja neizdodas tad programma necrasho bet paziņo problēmu un turpina darbību.
      current_file = codecs.open(TextFunctions.openedFile, "a", "utf-8")
      appended_text = input("Type Text, write !exit to exit this function: ") + "\n" #pievienojam jaunu rindu pēc ievadītā teksta
      while appended_text!= "!exit\n": #kamēr lietotājs nav izvēlejies iziet, tamēr turpinās rakstīšanas process.
        current_file.write(appended_text)
        appended_text = input("Type Text: ") + "\n"
      current_file.close()
      print("File writing finished. Returning to main menu.\n")
    except Exception as error: #ja ir kāda problēma, programma to noķer un arī pārādā specifisko kļūdu kas notika (priekš testēšanas)
      print("File doesn't exist, or can't be wrote to. Error:\n", error)

  def openFile(): #atver failu, paprasot lietotājam to vārdu, ja tāds neeksistē vai kaut kāda iemesla dēļ nevar atvērt- izmet kļūdu un turpina izvēlnes ciklu
    file_name = input("Enter file name to open:")

    if ".txt" not in file_name: #ja nav extension, pievieno extension
       file_name = file_name + ".txt"
    
    try: #cenšas atvērt failu, ja tāda nav, izmet kļūdu un turpina darbību
      current_file = codecs.open(file_name, "r", "UTF-8") #atver un aizver failu lai redzētu vai tas iet
      current_file.close()
      TextFunctions.openedFile = file_name
    except Exception as error: #ja ir kāda problēma, programma to noķer un arī pārādā specifisko kļūdu kas notika (priekš testēšanas)
      print("Could not open this file! The error received was:\n", error)