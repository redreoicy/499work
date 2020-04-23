python3 nameSorter.py < Sort_Me.txt > output.txt
if diff output.txt Sorted.txt
then
  echo "Test Passed"
else
  echo "Test Failed"
  exit 1
fi
