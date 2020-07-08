from texthelpfunctions import TextHelpFunctions
class TextEditingMode:
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