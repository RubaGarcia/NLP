"""
Code adapted from the NLP class by Daniel Jurafski & Christopher Manning
"""
import sys
import os
import re
import pprint

pat_1 = '(\w+)@(\w+)\.(?:edu|EDU)' 
pat_2 = '(\w+) @ (\w+)\.(?:edu|EDU)'
pat_3 = '((?:\w+)\.(?:\w+))@(\w+)\.(?:edu|EDU)' 
#email_pat = '(\w+)(?: ?@|\&\#x40\; ?)((?:\w+\.)*(?:\w+))\.(?:edu|EDU)'
email_pat = '(\w+(?:\.\w+)*)(?: ?@|\&\#x40\; ?)((?:\w+\.)*(?:\w+))\.(?:edu|EDU)' #prueba para quitar falsos positivos
dash_pat = '(.+)@(.+)\.(?:-e-d-u)'
engler_pat = '(\w+) WHERE (\w+) DOM edu'
pure_subh_serafim_text_pat = '(\w+) at ((?:\w+ dot )*(?:\w+)) dot edu' # Procesarlo quitando los "dot"
vladlen = '(\w+)(?:%20)(?:at)(?:%20)(\w+)(?:%20)(?:dot)(?:%20)(?:edu)' # NO AÑADE NADA
obfuscate_pat = '\'(\w+)\.edu\',\'(\w+)\'' #Caso especial: dar la vuelta a los grupos
text_and_symbols_pat = '(\w+(?<![Ss][eE][rR][vV][eE][rR])) at ((?:\w+\.)(?:\w+))\.edu'
support_ullman = '(\w+) (?:at) (\w+) (?:dt) (?:com)' #caso especial -> no .edu si .com
main_ullman = '(\w+(?:\.\w+)*) @ ((?:\w+\.)*\w+).edu'
#nick = '(\w+\.)\w+@(\w+\.)+edu' #caso de nick (nombre.apellido@pipi.pupu.edu)
mailto = '"mailto:([^@]*)@([^@]*)\.edu"' #casos con mailto # NO AÑADE NADA
followed_by = '(\w+(?:\.\w+)*)[^\(\n\>]+\(followed by[^@]+@((?:\w+.)*\w+)\.edu'
text_no_dots = '(\w+) at ((?:\w+ )*\w+)(?<!dot) edu' #caso especial: no hay puntos, hay que añadirlos en el proceso
#psyoung = '\<A[^\>]+\>(\w+(?:\.\w+)*)@((?:\w+\.)*\w+).edu' # Creo que ya estan en el nuevo email_pat
jks = '(\w+) at ((?:\w+\;)*\w+)\;edu'

phone_main_pat = '(\d{3})-(\d{3})-(\d{4})'
parenthesis_phone = '\((\d{3})\) ?(\d{3})-(\d{4})'
spaces_phone = '\+\d+ (\d{3})[ -](\d{3})[ -](\d{4})'

#TODO: Siguiente a revisar: pal
""" 
TODO
This function takes in a filename along with the file object and
scans its contents against regex patterns. It returns a list of
(filename, type, value) tuples where type is either an 'e' or a 'p'
for e-mail or phone, and value is the formatted phone number or e-mail.
The canonical formats are:
     (name, 'p', '###-###-#####')
     (name, 'e', 'someone@something')
If the numbers you submit are formatted differently they will not
match the gold answers
"""
def process_file(name, f):
    res = []
    for line in f:
        # MAILS
        main_matches = re.findall(email_pat,line)
        for m in main_matches:
            email = '%s@%s.edu' % m
            res.append((name,'e',email))

        dash_matches = re.findall(dash_pat,line)
        for m in dash_matches:
            str = []
            for i in range(len(m)):
                str.append(m[i].replace('-',''))
            email = '%s@%s.edu' % tuple(str)
            match_found = (name,'e',email)
            if match_found not in res:
                res.append(match_found)

        engler_matches = re.findall(engler_pat,line)
        for m in engler_matches:
            email = '%s@%s.edu' % m
            match_found = (name,'e',email)
            if match_found not in res:
                res.append(match_found)

        pure_subh_serafim_text_matches = re.findall(pure_subh_serafim_text_pat,line)
        for m in pure_subh_serafim_text_matches:
            str = []
            for i in range(len(m)):
                str.append(m[i].replace(' dot ','.'))
            email = '%s@%s.edu' % tuple(str)
            match_found = (name,'e',email)
            if match_found not in res:
                res.append(match_found)

        # NO AÑADE NADA
        vladlen_matches = re.findall(vladlen,line)
        for m in vladlen_matches:
            email = '%s@%s.edu' % m
            match_found = (name,'e',email)
            if match_found not in res:
                res.append(match_found)
                
        obfuscate_matches = re.findall(obfuscate_pat,line)
        for m in obfuscate_matches:
            email = '%s@%s.edu' % tuple(reversed(m))
            match_found = (name,'e',email)
            if match_found not in res:
                res.append(match_found)

        text_and_symbols_matches = re.findall(text_and_symbols_pat,line)
        for m in text_and_symbols_matches:
            email = '%s@%s.edu' % m
            match_found = (name,'e',email)
            if match_found not in res:
                res.append(match_found)

        support_ullman_matches = re.findall(support_ullman,line)
        for m in support_ullman_matches:
            email = '%s@%s.com' % m
            match_found = (name,'e',email)
            if match_found not in res:
                res.append(match_found)

        main_ullman_matches = re.findall(main_ullman,line)
        for m in main_ullman_matches:
            email = '%s@%s.edu' % m
            match_found = (name,'e',email)
            if match_found not in res:
                res.append(match_found)

        # NO AÑADE NADA
        mailto_matches = re.findall(mailto,line)
        for m in mailto_matches:
            email = '%s@%s.edu' % m
            match_found = (name,'e',email)
            if match_found not in res:
                res.append(match_found)

        followed_by_matches = re.findall(followed_by,line)
        for m in followed_by_matches:
            email = '%s@%s.edu' % m
            match_found = (name,'e',email)
            if match_found not in res:
                res.append(match_found)

        text_no_dots_matches = re.findall(text_no_dots,line)
        for m in text_no_dots_matches:
            str = []
            for i in range(len(m)):
                str.append(m[i].replace(' ','.'))
            email = '%s@%s.edu' % tuple(str)
            match_found = (name,'e',email)
            if match_found not in res:
                res.append(match_found)

        jks_matches = re.findall(jks,line)
        for m in jks_matches:
            str = []
            for i in range(len(m)):
                str.append(m[i].replace(';','.'))
            email = '%s@%s.edu' % tuple(str)
            match_found = (name,'e',email)
            if match_found not in res:
                res.append(match_found)

        # PHONES
        phone_matches = re.findall(phone_main_pat,line)
        for m in phone_matches:
            phone = '%s-%s-%s' % m
            res.append((name,'p',phone))

        parenthesis_phone_matches = re.findall(parenthesis_phone,line)
        for m in parenthesis_phone_matches:
            phone = '%s-%s-%s' % m
            match_found = (name,'p',phone)
            if match_found not in res:
                res.append(match_found)

        spaces_phone_matches = re.findall(spaces_phone,line)
        for m in spaces_phone_matches:
            phone = '%s-%s-%s' % m
            match_found = (name,'p',phone)
            if match_found not in res:
                res.append(match_found)
    return res

"""
You should not need to edit this function.
Given a path to a directory, it processes all files
in that directory using the method 'process_file',
and collects all results in a unique list of tuples 
"""
def process_dir(data_path):
    # get candidates
    guess_list = []
    for fname in os.listdir(data_path):
        path = os.path.join(data_path,fname)
        f = open(path,'r',encoding="utf-8",errors = "ignore")
        f_guesses = process_file(fname, f)
        guess_list.extend(f_guesses)
    return guess_list

"""
You should not need to edit this function.
Given a path to a file of gold e-mails and phone numbers
this function returns a list of tuples of the canonical form:
(filename, type, value)
"""
def get_gold(gold_path):
    # get gold answers
    gold_list = []
    f_gold = open(gold_path,'r')
    for line in f_gold:
        gold_list.append(tuple(line.strip().split('\t')))
    return gold_list

"""
You should not need to edit this function.
Given a list of guessed contacts and gold contacts, this function
computes the intersection and set differences, to compute the true
positives, false positives and false negatives.  Importantly, it
converts all of the values to lower case before comparing
"""
def score(guess_list, gold_list):
    guess_list = [(fname, _type, value.lower()) for (fname, _type, value) in guess_list]
    gold_list = [(fname, _type, value.lower()) for (fname, _type, value) in gold_list]
    guess_set = set(guess_list)
    gold_set = set(gold_list)

    tp = guess_set.intersection(gold_set)
    fp = guess_set - gold_set
    fn = gold_set - guess_set

    pp = pprint.PrettyPrinter()
    print('True Positives (%d): ' % len(tp))
    pp.pprint(tp)
    print('False Positives (%d): ' % len(fp))
    pp.pprint(fp)
    print('False Negatives (%d): ' % len(fn))
    pp.pprint(fn)
    print('Summary: tp=%d, fp=%d, fn=%d' % (len(tp),len(fp),len(fn)))



"""
The main program takes a directory name and gold file (you should not need to edit it).
It then processes each file within that directory and extracts any
matching e-mails or phone numbers and compares them to the gold file
"""
if __name__ == '__main__':
    guess_list = process_dir('./data/dev')
    gold_list =  get_gold('./data/devGOLD')
    score(guess_list, gold_list)
