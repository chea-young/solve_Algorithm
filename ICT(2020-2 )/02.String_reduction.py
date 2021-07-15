#!/bin/python3

import math
import os
import random
import re
import sys


def getMinDeletions(s):
    s_length = len(s)
    exist_list = []
    for i in range(s_length-1, 0 , -1):
        start_index = 0
        end_index = i
        check_list = []
        index_list = {}
        exist_list = []
        for j in range(s_length-i+1):
            check_string = s[start_index:end_index]
            #print(i ,check_string, check_list)
            if(check_string in check_list):
                exist_list.append((check_string, start_index, end_index, index_list[check_string]))
            else:
                check_list.append(check_string)
                index_list[check_string] = (start_index, end_index)
            start_index += 1
            end_index += 1
        if(exist_list != []):
            print(exist_list)
            break
    del_index = []
    for i in exist_list:
        for j in range(i[1],i[2]):
            if(j not in del_index):
                del_index.append(j)
    return len(del_index)

            
#print(getMinDeletions("bbeadcebfp"))
print("=================================")
print(getMinDeletions("afcbdgigdrfacaafgbgeecadajadadebbofbdcaaidacacbdflbcfdbgaaidoaaaiccdafhkcgaeeffebchbbaebfhiciabeaaabbmaefbagaabcafccbbaqdefaggddnjdafdibbeahjcjgebeddbababdgaegcbdbfhccecdibdccchbhbaccaebcbadbcecefcefcbdildkebngadeekasbbgfcafcfhbcafaaibcbcbickaaedafiaedbbccgpdedaccccclbggcoccaepbdaadgdfdbdbdfacbcacdaaabafadceehbffagibbabbcagbccbdcdddccdcdeahaafamngadgbcaaceeheabfcbedcfbbcbfacdagdaboddagfbaeagcbbclbcibcibhejceabdacbejfcdfbebccaggbcalcceaagaacchddacicacacgcbdffbogafcaacigdgcafaccbabecacahcdcgbhbgdcdcedagbaibbdadbkhcahacbacagbaagbjcfaeadboakcaigfdgchacdjjpbalhadbbcfiaacdbeaidbeccebgajbifacblbbbcccebbemfancibbcdcdbbbadmlioqkccchcaiebacdaiddedgdbhifaccfaaaaebgdcbdefbhaabecdahfdjbfaffdghhlabbabeaqdflkfcbbaaeeaeamocagaadabcdheafihbbgjhameiagdcjaahkadcibaafbacaadodakkdacgbdbffdbjmbbbafgddebihcahhbhbbabhhdfdefcfbgagicbebcambebcdeaaakgnbafjagbbdeebgebdgbabdadgageachajedabcfekgaacbfbfddbhaafdgmachacgdadaebgbadlbacjddbcbjancdd"))
#print(getMinDeletions("abcabc"))
#print(getMinDeletions("abab"))