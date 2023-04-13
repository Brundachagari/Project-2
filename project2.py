'''
Project 2 - NATO Alphabet - Spring 2023   
Author: Brunda Chagari 9065-61529

This program takes two files the alphabet and NATO alphabet it then
read and process all identifiers in the identifiers input file
and prints the identifier labelled with its category and,
if it's valid, prints the NATO spelling on a separate line.

I have neither given or received unauthorized assistance on this assignment.
Signed:  Brunda Chagari
'''

def get_dictionary():
    ''' reads the alphabet input file and creates a dictionary that
    maps a character to a code word
    Parameters: none
    Return: d the alphabet dictionary
    '''
    words = open("alphabet.txt", "r")  
    parsed = words.read().split("\n")
    keys = []
    for key in parsed:
        keys.append(key.rstrip())
    d = {}
    for key in keys:
        pair = key.split(" ")
        d[pair[0]] = pair[1]
    d[" "] = "Space"
    d["-"] = "Dash"
    return d

def categorize_identifier(iden):
    ''' accepts an identifier as an argument and validates it based on length
    Parameters: iden is an argument
    Return: invald if identifier is invalid
    '''
    if len(iden) == 17:
        return "VIN"
    elif len(iden) >= 5 and len(iden) <= 8:
        return "TAG"
    else:
        return "INVALID"
    
def get_spelling(d, iden):
    ''' returns a string representing the spelling of that identifier
    using the code word alphabet represented by the dictionary
    Parameters: d and iden
    Return: spelling, the alphabet in the NATO language
    '''
    spelling = ""
    for l in iden:
        spelling += d[l] + " "
    return spelling

def main():
    ''' Gets the dictionary to use,
    then processes all identifiers in the identifiers input file
    validates the identifier and prints the identifier labelled with its category
    if valid also prints the NATO spelling
    Parameters: none
    Return: none
    '''
    d = get_dictionary()
    words = open("identifiers.txt", "r").read()
    words = words.split("\n")

    for word in words:
        tag = categorize_identifier(word)
        if tag == "VIN" or tag == "TAG":
            print(tag + ":" + word.upper())
            print(get_spelling(d, word.upper()).rstrip())
        
# Call main like this to keep Web-CAT happy:
if __name__ == '__main__':
    main()