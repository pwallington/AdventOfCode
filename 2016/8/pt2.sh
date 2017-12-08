INFILE=$1

cat $INFILE | tr -d '[[:space:]]' | tee $1.tmp1 
echo
CODE=`wc $1.tmp1 | awk '{print $3}'`

cat $INFILE | sed -e 's/\\/\\\\/g' -e 's/\"/\\"/g' -e 's/^/"/' -e 's/$/"/' | tr -d '[[:space:]]' | tee $1.tmp2
echo
DATA=`wc $1.tmp2 | awk '{print $3}'`
echo "Code chars: $CODE"
echo "Data chars: $DATA"

echo "Overhead: "$(($CODE-$DATA))
