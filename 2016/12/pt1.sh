cat input.txt | tr 'a-z:"[]{},' ' ' | xargs | tr ' ' '+' | bc
