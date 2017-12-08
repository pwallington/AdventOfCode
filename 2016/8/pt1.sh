INFILE=$1

cat $INFILE | tr -d '[[:space:]]' > $1.tmp1 
CODE=`wc $1.tmp1 | awk '{print $3}'`
echo "Code chars: $CODE"

cat $INFILE | sed -e 's/^\"//' -e 's/\"$//' -e 's/\\x[0-9a-f][0-9a-f]/./g' -e 's/\\\\/\\/g' -e 's/\\\"/\"/g' | tr -d '[[:space:]]' > $1.tmp2

DATA=`wc $1.tmp2 | awk '{print $3}'`
echo "Data chars: $DATA"

echo "Overhead: "$(($CODE-$DATA))
