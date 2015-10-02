#chipher.py
#Python module to encode/decode message, given a key
#By Zoe Peterson & Freddie Roenn Stensaeth
#01.29.14



#Defining encode function with parameters text and key
def encode(text, key):    
    
    #Finding length of text and key
    length_text = len(text)
    length_key = len(key)
    
    #Defining variables
    num_key = []
    num_text = []
    encoded_message = ''
    y = 0
    encoded = 0
    
    #Loop key to turn letters to numbers
    for x in key:
        num_key += [ord(x) - 96]
    
    #Loop text to turn letters to numbers
    for x in text:
        num_text += [ord(x) - 96]
    
    #Creating key long enough for text
    times = length_text / length_key + 1
    long_key = num_key * times
    
    #Loop num_text
    for x in num_text:
        #Add key-number to number in num_text
        encoded = x + long_key[y] + 96
        #If encoded value is after z, then start over at a
        if encoded > 122:
            encoded = encoded - 26
        #Change encoded value back to letter
        new_letter = chr(encoded)
        #Add letter to encoded message
        encoded_message += new_letter
        #Find position in long_key
        y += 1
    
    return encoded_message

#Defining decode function with parameters text and key
def decode(text, key):
    
    #Findinglength of text and key
    length_text = len(text)
    length_key = len(key)
    
    #Defining variables
    num_key = []
    num_text = []
    decoded_message = ''
    y = 0
    decoded = 0
    
    #Loop key to turn letters to numbers
    for x in key:
        num_key += [ord(x) - 96]
    
    #Loop text to turn letters to numbers
    for x in text:
        num_text += [ord(x) - 96]
    
    #Creating key long enough for text
    times = length_text / length_key + 1
    long_key = num_key * times
    
    #Loop num_text
    for x in num_text:
        #Add key-number to number in num_text
        decoded = x - long_key[y] + 96
        #If decoded value is before a, then start over at z
        if decoded < 97:
            decoded = decoded + 26
        #Change dedcoded value back to letter
        new_letter = chr(decoded)
        #Add letter to decoded message
        decoded_message += new_letter
        #Find position in long_key
        y += 1
    
    return decoded_message
    
        
#Defining main function with no parameters    
def main():
    #Ask user if they want to encode or decode a message
    choice = raw_input('Encode or decode? ')
    #If encode, ask for message and key
    if choice == 'encode' or choice == 'Encode':
        message = raw_input('Enter message to encode: ')
        key = raw_input('Enter encoding key: ')
        #Call encode function
        output = encode(message, key)
        #Print encoded message
        print output
    #If decode, ask for message and key
    elif choice == 'decode' or choice == 'Decode':
        message2 = raw_input('Enter message to decode: ')
        key2 = raw_input('Enter decoding key: ')
        #Call decode function
        output2 = decode(message2, key2)
        #Print decoded message
        print output2
    
if __name__ == '__main__':
    main()