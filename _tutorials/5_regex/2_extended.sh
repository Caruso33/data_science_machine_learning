#!/usr/bin/env bash

data=./data/regex
print() {
    cat "${data}$1.txt"
}

#***************************
# a{m} - repeater - represents exacly m repetitions of preceding 'a'
# a{m,n} - repeater - represents between m and n repetitions of preceding 'a'

# grep '^[0-9][0-9][0-9]$' "${data}18.txt"
grep -E "^[0-9]{3}$" "${data}18.txt"
grep -E "^[a-z]{4,6}$" "${data}19.txt"
# print "19"

#***************************
# ha{m} - () group and treat as single entity
# {m,} - at least m repetitions
# {,n} - at most n repetitions

grep -E "(ha){4,}" "${data}20.txt"
grep -E "^(ha){,2}$" "${data}21.txt" # needs ^+$ as it would match substrings which match
# print "21"

#***************************
# a+ - one or more occurrences of preceding char

grep -E "fooa+bar" "${data}22.txt"
# print "22"

#***************************
# a? - zero or one occurrences of preceding char

grep -E "http(s?)://website" "${data}23.txt"
# print "23"

#***************************
# (a|b) - alternative choice of possible multi-chars

grep -E "(log|ply)wood" "${data}24.txt"
