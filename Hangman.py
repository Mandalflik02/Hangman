def print_opening_screen():
  HANGMAN_ASCII_ART="""  _    _  \n | |  | |\n | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  \n |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ \n | |  | | (_| | | | | (_| | | | | | | (_| | | | |\n |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|\n                      __/ |                      \n                     |___/     \n"""       
  print(HANGMAN_ASCII_ART)#Prints the opening screen of the game
def choose_word(file_path, index):
  """This function selects a word from a file, the location of the word is according to the index.  
  :param file_path: file_path
  :param index: number
  :type file_path: string
  :type index: int
  :return:the word in index of 'index'
  :rtype: string """
  words_file=open(file_path,'r')#Opens the file of words for read-only mode
  file_text=words_file.read()#Saves all the text from the file into a string
  last_line=0
  words_str=""
  for w in range(len(file_text)):
    #Saves the words in new string(words_str) without line breaks 
    if file_text[w] == '\n':
      words_str += file_text[last_line:w]
      last_line = w +1
  words_str += file_text[last_line:] #Inserts the last word in the file into the new string(words_str)
  words_list=[]  
  last_space=0      
  for word in range(len(words_str)):
    #Moves the words in the list 
    if words_str[word] == ' ':#Finds the end of a word
      words_list.append(words_str[last_space:word])
      last_space = word + 1
  words_list.append(words_str[last_space:])#Inserts the last word in the string into the list
  the_word=""
  while index > len(words_list):
    #If a position is selected that exists outside the boundaries of the list (greater than the number of words)
    #Then subtract from it the size of the list (number of words) until it reaches a position that exists within the boundaries of the list
    index -= len(words_list)
  the_word=words_list[index-1]#The user refers to the first word in position 1,And in the list the first position is 0 so must subtract 1
  return the_word
def show_hidden_word(secret_word, old_letters_guessed):
  """This function displays the word in a status that the player is familiar with .
  :param secret_word: the word that should be guessed .
  :param old_letters_guessed: the letters guessed in the air
  :type secret_word: string
  :type old letters_guessed: list
  :return: the secret word with  The hidden letters
  :rtype: string """
  str=" "
  for i in secret_word:
    if i in old_letters_guessed:#If a letter in a word exists in the list of letters that the user has guessed so far adds it to the hidden word
      str+=i+" "
    else:#If a letter in a word does not exist in the list of letters that the user has guessed so far adds an underscore to the hidden word
      str+="_ "
  return str
def check_win(secret_word, old_letters_guessed):
  """This function checks if the user has guessed all the letters of the secret word and won.
  :param secret_word: the word that should be guessed .
  :param old_letters_guessed: the letters guessed in the air
  :type secret_word: string
  :type old letters_guessed: list
  :return: Did the user win
  :rtype: bool """
  check_word=True
  for i in secret_word:
    #Goes over the secret word and checks if all its letters are in the array of letters that the player guessed before
    if i not in old_letters_guessed:
      check_word =False
  if check_word == True:
    print("W I N")
    return True
  return False
def check_valid_input(letter_guessed,old_letters_guessed):
  """This function checks whether the guess is correct or not.  
  :param letter_guessed: the player guess 
  :param old_letters_guessed: the letters that were guessed aerly
  :type letter_guessed: string
  :type old_letters_guessed: list 
  :return: the checking result 
  :rtype: bool """
  if(len(letter_guessed)==1 and letter_guessed.isalpha() and (letter_guessed.lower() not in old_letters_guessed)):
    #If the input is correct, returns true.
    return True
  elif (len(letter_guessed) > 1 and letter_guessed.isalpha()) or (len(letter_guessed)==1 and letter_guessed.isalpha()==False) or (len(letter_guessed) > 1 and letter_guessed.isalpha()==False and (letter_guessed.islower() or letter_guessed.isupper())or (letter_guessed.lower() in old_letters_guessed)):
    #If the input is incorrect, returns False.
    return False
  else:
    return False
def try_update_letter_guessed(letter_guessed,old_letters_guessed):
  """This function saves the user's guess into the list of his previous guesses provided it is valid.  
  :param letter_guessed: the player guess 
  :param old_letters_guessed: the letters that were guessed aerly
  :type letter_guessed: string
  :type old_letters_guessed: list 
  :return: Is it possible to keep the guess within the list, The updated list
  :rtype: bool, list """
  if check_valid_input(letter_guessed,old_letters_guessed) == True :
    #If the input is correct, add it to the list of guessed letters. 
    #Returns truth and updated list of guessed letters
    old_letters_guessed.append(letter_guessed.lower())
    return True, old_letters_guessed
  elif check_valid_input(letter_guessed,old_letters_guessed) == False and letter_guessed not in old_letters_guessed:
    #If the input is incorrect but is incorrect because it is in the list of guessed letters, prints an error.
    # Returns False and the list of guessed letters.
    print('X')
    return False,old_letters_guessed
  #If the input is incorrect, prints an error and the list of letters. 
  #Returns a lie and the list of guessed letters.
  print('X\n',"-> ".join(old_letters_guessed))
  return False,old_letters_guessed


def main():
  secret_word = ""
  old_letters_guessed = []
  MAX_TRIES = 6
  num_of_tries = 0
  HANGMAN_PHOTOS={'0': """ x-------x\n""", '1': """ x-------x\n |        \n |\n |\n |\n |""", '2': """ x-------x\n |       |\n |       0\n |\n |\n |""",
    '3': """ x-------x\n |       |\n |       0\n |       |\n |\n |""", '4': """ x-------x\n |       |\n |       0\n |      /|\\\n |\n |""",
    '5': """ x-------x\n |       |\n |       0\n |      /|\\\n |      /\n |\n""", '6': """ x-------x\n |       |\n |       0\n |      /|\\\n |      / \\\n |"""}
  
  print_opening_screen()
  file_path=str(input(" Enter file path: "))#Gets the path to the file from the user
  word_index=int(input(" Enter index: "))#Gets the index of the secret word from the user
  secret_word=choose_word(file_path,word_index)#The secret word selected from the file
  print("\n Let’s start!\n")
  print(HANGMAN_PHOTOS[str(num_of_tries)])
  print(show_hidden_word(secret_word,old_letters_guessed))


  while check_win(secret_word,old_letters_guessed) == False or num_of_tries == MAX_TRIES:
    #Continues to play as long as the player has not won or lost
    letter_guessed=str(input("Guess a letter: "))
    input_valid,old_letters_guessed=try_update_letter_guessed(letter_guessed,old_letters_guessed)
    if input_valid == False:
      continue
    if letter_guessed not in secret_word:
      print(":(\n")
      num_of_tries += 1
      if num_of_tries == MAX_TRIES:#If the player loses, prints the last position of the hangman and exits the loop
        print(HANGMAN_PHOTOS[str(num_of_tries)])
        break
      print(HANGMAN_PHOTOS[str(num_of_tries)])
      
    print(show_hidden_word(secret_word,old_letters_guessed))


  if num_of_tries == MAX_TRIES:
    print("\nL O S E")

if __name__ == "__main__":
  main()