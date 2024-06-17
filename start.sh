echo "Cloning Repo...."
if [ -z $BRANCH ]
then
  echo "Cloning main branch...."
  git clone https://github.com/Mr-SyD-OrG/For Mr-SyD-OrG/For
else
  echo "Cloning $BRANCH branch...."
  git clone https://github.com/Mr-SyD-OrG/For -b $BRANCH /For
fi
cd Mr-SyD-OrG/For
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 main.py
