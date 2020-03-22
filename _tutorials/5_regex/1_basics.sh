#!/usr/bin/env bash

data=./data/regex
print() {
    cat "${data}$1.txt"
}

#***************************
# a* - zero or more occurrences of 'a' - the letter PRECEDING '*'

regex='fooa*bar'
# cat $data | grep 'fooa*bar'
grep $regex "${data}01.txt"

#***************************
# . - exactly one char - single WILDCARD for ANY ONE char

grep 'foo.bar' ./data/regex02.txt 

#***************************
# .* - zero or more occurrences of wildcard / any char

grep 'foo.*bar' ./data/regex03.txt 

#***************************
# \s - whitespace, \s* zero or more occurrences of whitespace

grep 'foo\s*bar' ./data/regex04.txt 

#***************************
# [abc] - character class - one of the chars inside the brackets, a OR b OR c
# [^abc] - character class - NOT one of the chars inside the brackets, NOT a AND b AND c

grep '[fcl]oo' ./data/regex05.txt 
grep '[^hm]oo' ./data/regex05.txt 

#***************************
# [a-c] - character range - one of the chars falling in the range given in the brackets, a until c
# [a-cx] - character range or char - one of the chars falling in the range given in the brackets OR given chars
# [a-cA-Cx] - 2 character ranges or char
# [^a-cx-z] - character range - NOT one of the chars falling in the range given in the brackets, NOT a until c, x until z

grep '[f-m]oo' ./data/regex06.txt 
grep '[^a-en-z]oo' ./data/regex06.txt 
grep '[^a-cA-Cx]oo' ./data/regex10.txt 

#***************************
# ^$*.[]()\ - special characters - need escaping

grep 'x*\.y*' ./data/regex11.txt 

#***************************
# . inside [] - it's NOT being escaped because has no meaning inside []
# ^ - \ - inside [] need to be escaped

grep 'x[:.#]y' ./data/regex12.txt 
grep 'x[#:\^\\]y' "${data}14.txt"

#***************************
# ^ - start anchor - placeholder that signifies beginning of line. 
# differs inside [] and outside - inside it means negation
# $ - end anchor - placeholder that signifies end of line

grep '^foo.*' "${data}15.txt"
grep '.*bar$' "${data}16.txt"

#***************************
# ^char$ - char only string in line

grep '^foo$' "${data}17.txt"