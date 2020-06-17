# Izveidoju jaunu failu un klasi priekš funkcijām lai varētu importēt un galvenais kods izskatītos "tīrāks"
import codecs #lai nolasītu īpašos windows simbolus
import os #lai varētu notīrīt ekrānu

class TextFunctions: #es visu sametu klasē, lai ir vieglāk importēt
  openedFile = None #glabājam šeit mūsu atvērto faila vārdu kā global variable funkcijām

  ################################################################
  ######################## PALĪGFUNKCIJAS ######################## 
  ################################################################
  # Funkcijas, kas nav mūsu opcijas, bet palīdz ar citām lietām ko visulaiku atkārto

  def newLine(): #ievieto svītru rindu kad izmantota
    print("--------------------------------------")
  
  def clearScreen(): #notīrā ekrānu
    if os.name == "nt": #pārbauda vai ir Windows OS un izmanto tam atbilstošo clear komandu
      os.system('cls')
    else: #ja ir cits OS, kā Linux vai MacOS, izmanto šo clear komandu
      os.system('clear')
  
  def numberedRead(teksts): #pārlasa tekstu un pievieno atsevišķām rindām nummurus (prieks rediģēšanas modes)
    display_numbered_text = teksts.split("\n") #sadala tekstu sarakstā, kur katra rinda ir sava vērtība
    i = 0 #i izmantosim kā iterable priekš rindas nr.
    for line in display_numbered_text: #izejam caur katru rindu mūsu sarakstā
      i+=1 #rindas nr.
      print(i, ": ", line, sep = "") #izprintē rindu ar to numuru
  
  def showOpenFile(): #parāda tikmērējo atvērto failu
    TextFunctions.newLine()
    print("File currently open:", TextFunctions.openedFile)
    TextFunctions.newLine()

  def checkIfOpenFile(): #pārbauda, vai ir atvērts fails un notīrā ekrānu pēc tam
    if TextFunctions.openedFile == None:
      TextFunctions.openFile()
    TextFunctions.clearScreen()
  
  def saveFile(text_to_save): #saglabā atvērto failu (prieks rediģēšanas modes)
    with codecs.open(TextFunctions.openedFile, "w+", "utf-8") as main_file:
          main_file.write(text_to_save) #saglabā izmaiņas failā
          print("File saved successfully\n")
  
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
  
  def editingMode(): #atver rediģēšanas modi
    command_text = "\nCommands:\n!edit [line]- edit a line in the file\n!read - Read the current contents of the file\n!help- show all available commands\n!del [line] - delete a specific line\n!exit - exit file\n!save - saves the edited changes to the file\n!save_as - saves the edited changes to a new file and opens it in the editor" #mūsu visas komandas, ko lietotājs var lietot

    print("\nEDITING MODE ACTIVATED")
    TextFunctions.checkIfOpenFile() #Pārbauda vai jau ir atvērts kāds fails, ar kuru strādās

    try: #cenšas atvērt failu, ja neizdodas, izmet kļūdu un beidz funkciju
      current_file = codecs.open(TextFunctions.openedFile, "r", "utf-8") #atveram sākotnējo failu un nolasam to datus
      file_text = current_file.read() #saglabājam tekstu variable, ar ko turpmāk strādāsim
      print("---------READING FILE-------------\n")
      TextFunctions.numberedRead(file_text)
      print("\n-------------COMMANDS-------\nFile successfully read, you can begin writing:", command_text,"\n--------------------------------", sep = "")
      current_file.close() #lai nomainītu modi

    except Exception as error:  #ja ir kāda problēma, programma to noķer un arī pārādā specifisko kļūdu kas notika, un beidz funkciju dēļ kļūmes
      print("File couldn't be opened, error:\n", error)
      return #beidz funkciju, neko neatgriežot

    user_input = input() #gaida lietotāja input
    while user_input != "!exit": #mūžīgi atkārtojas līdz lietotājs ievada !exit
      
      if user_input == "!save": #saglabā tajā pašā failā
        TextFunctions.saveFile(file_text) #saglabā failu

      elif user_input == "!save_as": #izveido jaunu failu, kur saglabā tekstu
        TextFunctions.newFile() #izveidots jauns fails un tiek atvērts
        TextFunctions.saveFile(file_text) #saglabā jauno failu ar tekstu
      
      elif user_input.startswith("!edit"): #atļauj lietotājam rediģēt specifisku rindu vai vārdu, un tā kā var pieminēt tieši kuru rindu tekstā, pārbauda vai ar to sākas
        file_editing_text = file_text.split("\n") #sadala tekstu sarakstā, kur katra ir rinda ir atsevišķš value
        TextFunctions.numberedRead(file_text) #nolasa tekstu ar rindas nr

        try: #ķer kļūdu ja ir iedota neeksistējoša rinda
          if user_input != "!edit":
          #user_input.split(" ")[1] ir tā līnija ko mums iedeva ko rediģēt
            editing_line = int(user_input.split(" ")[1])
            line_to_edit = file_editing_text[editing_line-1] #definē rediģējamo rindu kā izvēlēto nr. -1 jo masīvi sākas no 0, nevis 1
          else: #ja lietotājs neievadīja skaitli pēc komandas, jautā kādu rindu vēlās rediģēt šeit
            editing_line = int(input("Enter line you wish to edit:"))
            line_to_edit = file_editing_text[editing_line-1] #definē rediģējamo rindu kā izvēlēto nr. -1 jo masīvi sākas no 0, nevis 1
        except Exception as error:
          print("This line does not exist! Cancelling editing function.\nError:", error)
        else:
          print("Editing", editing_line ,"line:", line_to_edit) #izprintē rediģējamo rindu
          editing_text = input("Type line to replace this one with or type !edit to replace a specific word: ") #pievieno vārdus vēl

          if editing_text == "!edit": #ja lietotājs nolemj atkal rediģēt kādu garu rindu vārdos
            line_to_edit = line_to_edit.split(" ")

            i = 0 #iterable, sākām no 0
            for word in line_to_edit: #priekš katra vārda rindā, to parādi ar to nr.
              i+=1
              print(i, ":", word, sep = "")

            editing_word = int(input("Enter word you wish to edit:"))
            word_to_edit = line_to_edit[editing_word-1] #tā kā listi sākas no 0 bet mums skaitīšana lietotājam sākās no 1
            print("Editing this word:", word_to_edit) #parāda kuru vārdu tikmēr rediģējam
            edited_word = input("Type a word to replace this word with:") #pievieno vārdus ar ko aizvieto to
            line_to_edit[editing_word-1] = edited_word #vārds tiek aizvietots
            editing_text = " ".join(line_to_edit) #rindas sarakstu apkopo atkal vienā variable
        
          file_editing_text[editing_line-1] = editing_text #sarakstā pievieno jauno rindu
          file_text = "\n".join(file_editing_text) #savieno sarakstu atpakaļ vienā value
          TextFunctions.clearScreen() #notīra ekrānu
          TextFunctions.numberedRead(file_text) #nolasa atkal tekstu
          TextFunctions.newLine()
          print(command_text) #izprintē komandas tekstu atkal
          TextFunctions.newLine()

      elif user_input == "!read":
        TextFunctions.newLine() #jauna svītriņu rinda
        TextFunctions.numberedRead(file_text) #izlasa numurēti teksta datus
        TextFunctions.newLine() #jauna svītriņu rinda

      elif user_input == "!help": #pārāda visas komandas
        TextFunctions.newLine() #jauna svītriņu rinda
        print(command_text) #parāda komandas tekstu
        TextFunctions.newLine() #jauna svītriņu rinda

      elif user_input.startswith("!del"): #komanda atļauj lietotājam izdzēst kādu rindu, un tā kā var pieminēt skaitu, pārbaudam vai tieši sākas ar to

        try: #tāpāt kā ar rediģēšanu šeit pārbauda
          file_delete_text = file_text.split("\n")
          if user_input.split(" ")[1] != None: #placeholder
          #user_input.split(" ")[1] ir tā līnija ko mums iedeva ko izdzēst
            deleting_line = int(user_input.split(" ")[1])
          else:
            deleting_line = int(input("Enter line you wish to delete:"))
          line_to_del = file_delete_text[deleting_line-1] #lietotāja rindas pārāda ar +1 rindas nr., tāpēc šeit mēs to atņemam
        except Exception as error:
          print("This line does not exist! Cancelling editing function.\nError:", error)


        file_delete_text.remove(line_to_del) #noņemam to rindu
        file_text = "\n".join(file_delete_text) #saliekam tekstu atpakaļ vienā variable
        TextFunctions.clearScreen() #notīra ekrānu
        TextFunctions.numberedRead(file_text) #nolasa tekstu ar rindas nr
        TextFunctions.newLine() #jauna svītriņu rinda
        print(command_text) #pārādam atkal komandas tekstu
        TextFunctions.newLine() #jauna svītriņu rinda
      
      else:
        file_text = file_text + "\n" + user_input #izveido jauna rinda pēc ievadītā
      user_input = input() #gaida lietotāja input
    TextFunctions.saveFile(file_text) #saglabā failu pēc cikla
    print("Exiting Editing Mode.\n") #paziņo ka beidz rediģēšanas funkciju