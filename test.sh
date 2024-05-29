pytest test_leap_year.py > status.txt
if [[  $(grep -i error status.txt) == "" ]]
then
  echo "les tests sont passés!"
  python leap_year.py
else
  echo "ERROR in TEST"
  cat status.txt
fi