def is_pangram(word) :

    
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    

    for ch in alphabets :

        
        if ch not in word.lower() :

            
            return False

    
    return True

print(is_pangram("the quick Brown fox jumps over lazy dog"))