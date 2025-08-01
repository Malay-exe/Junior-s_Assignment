def rhyming_word_checker(t1,t2):
   
    pair = (t1[-2:], t2[-2:])
    match pair:
        case (s1, s2) if s1 == s2:
            print("Perfect rhyme!")
        case (s1, s2) if s1[1:] == s2[1:]:
            print("Near rhyme!")
        case _:
            print("No rhyme.")

s1=input("Enter the first word: ").strip().lower()
s2=input("Enter the second word: ").strip().lower()
rhyming_word_checker(s1,s2)
