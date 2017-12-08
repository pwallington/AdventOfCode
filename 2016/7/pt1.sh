perl -p -e 's/(.+) -> (.+)/\2 = \1/; s/AND/&/; s/OR/|/; s/NOT/~/; s/RSHIFT/>>/; s/LSHIFT/<</; s/^(.) /0$+ /;' | sort | perl -p -e 's/^0//'

