#!/usr/bin/python3

# You are given an array(list) strarr of strings and an integer k. Your task is to return the first longest string consisting of k consecutive strings taken in the array.
# 
# Examples:
# strarr = ["tree", "foling", "trashy", "blue", "abcdef", "uvwxyz"], k = 2
# 
# Concatenate the consecutive strings of strarr by 2, we get:
# 
# treefoling   (length 10)  concatenation of strarr[0] and strarr[1]
# folingtrashy ("      12)  concatenation of strarr[1] and strarr[2]
# trashyblue   ("      10)  concatenation of strarr[2] and strarr[3]
# blueabcdef   ("      10)  concatenation of strarr[3] and strarr[4]
# abcdefuvwxyz ("      12)  concatenation of strarr[4] and strarr[5]
# 
# Two strings are the longest: "folingtrashy" and "abcdefuvwxyz".
# The first that came is "folingtrashy" so 
# longest_consec(strarr, 2) should return "folingtrashy".
# 
# In the same way:
# longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2) --> "abigailtheta"
# n being the length of the string array, if n = 0 or k > n or k <= 0 return "".
# 
# Note
# consecutive strings : follow one after another without an interruption


from eval_time import eval_time



def longest_consec(strarr, k):
    current = ''
    best = ''
    print(strarr, k)
    if k not in range(len(strarr)):
        return ''
    for i in range(len(strarr)+k):
        current = ''.join(strarr[i:i+k])
        if len(current) > len(best): best = current
    return best


strarr = ['gggwlllvqqff', 'taeex', 'sslllccckffg', 'zzoobbaaah', 'sssso', 'apppxxxffwwwmmmtttamm', 'ooyyooopcccvvv', 'mmbbu', 'zzzmmucc', 'hyyxxzzejlcc', 'iiiffckss', 'dllprbb', 'wzzttfffhhw', 'nnccpppssxxx', 'bgkkcc', 'fffffcc', 'vvzwwwhoohyyyxx', 'lllsklccc', 'uuxxarrrooouu', 'ssbbbddvv', 'cccgggjjzzzff', 'uuuwwwlfffg', 'dddtrrr', 'wwddppaaccc', 'lggjjj', 'xxhhhwwwxxxhhhythhh', 'ppggsqqqdddr', 'irrrerdtt', 'rrxxxuusd', 'aysssppgggss', 'llttegggkhh', 'yyogggddhhh', 'qmmlvvvj', 'ooffezznn', 'eeeeevvodhh', 'uuuyyymmbbdddl', 'eeeiiiqu', 'ssssbbjjj', 'znnnppiiggg', 'tttttdhhuuu', 'myyyubaawwwnn', 'umvvvaakzz', 'rrrlluuxvv', 'zzwwwaaa', 'jjjyww', 'dddiiikggmm', 'fjjjocsyy', 'foooovvve', 'vvtbttiiimmm', 'xxxjaa', 'llkktttuu', 'pzzzpppkk', 'llaattt', 'vuuumxxccss', 'aaahppnncc', 'iioooaadddaaa', 'kgggjjsss', 'mmmgj', 'ggiizzztwww', 'llkeww', 'xxxznnrjuus', 'bbbqqqhhhpi', 'ddkfgiic', 'nnnjjjeeew', 'jjjyxxx', 'fffvwwwhhwx', 'nnnxxtttt', 'mmbkkkueee', 'xiii', 'mvvaaa', 'yyfuuuwww', 'dmkfffs', 'uuuheeeehhheehp', 'qrrbbbrrrdbbb', 'ggzzztttbbbkttmmm', 'ccceeenss', 'onirrj', 'uuuaaawwwbbiccc', 'tqqpppaaawwwfddd', 'noffdhhhm', 'zzzjjllzuuw', 'tcccc', 'yywwwjjjpmmmoot', 'pppwcccsssddd', 'iiieeiiaalllk', 'wsgggiibbb', 'ddmmjjvvtttqqqq', 'ddriiillvfff', 'tjjjvvdddnneee', 'ohhht', 'kkknnweekkxxjnnn', 'aahhhxjuhh', 'eewmltttjjxxx', 'sssurrrhtttcc', 'wwwccnvvrnneee', 'kkdddseeecc', 'bjjlllx', 'nnneeessshh', 'vxxggdddd', 'hhcccuuuuummccc', 'cccplldddvvv', 'dddxxxrrss', 'eeeqqoooqqppp', 'zzrrreeeqqql']
k = 39


eval_time(longest_consec(strarr, k))
