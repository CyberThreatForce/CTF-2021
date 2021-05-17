#!/bin/bash
#script de shlag

echo "Nb challs: $(find ./ | grep -v '.git'| cut -d '/' -f 3 | uniq  | grep -E '[a-A]' | wc -l)"
