if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/Mr-SyD-OrG/For.git /For
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /For
fi
cd /For
pip3 install -U -r requirements.txt
echo "Starting maharaja-forward-bot...."
python3 main.py
