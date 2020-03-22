#!/usr/bin/env bash

data=./data/regex
print() {
    cat "${data}$1.txt"
}

#***************************
# () - capture group - helps capture pattern - ([0-9]+) < capture group \1
# sed -r 's/pattern/replacement/g' inputfile

# grep -E "([0-9]+)x([0-9]+)" "${data}25.txt"
sed -r "s/([0-9]+)x([0-9]+)/\1 pix by \2 pix/g" "${data}25.txt"