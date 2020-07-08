import codecs #lai nolasītu īpašos windows simbolus
import os #lai varētu notīrīt ekrānu

class TextHelpFunctions: #es visu sametu klasē, lai ir vieglāk importēt
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