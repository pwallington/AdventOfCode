egrep '(.)\1' | egrep -v '(ab|cd|pq|xy)' | egrep '(.*[aeiou].*){3,}'

