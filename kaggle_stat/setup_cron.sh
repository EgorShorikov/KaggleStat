PROJECT_PATH="$HOME/KaggleStat/kaggle_stat"
PYTHON_PATH="/usr/bin/python3"

(crontab -l 2>/dev/null; echo "# Kaggle Tasks") | crontab -

(crontab -l 2>/dev/null; echo "5 3 * * * cd $PROJECT_PATH && $PYTHON_PATH manage.py load_competitions >> $PROJECT_PATH/cron.log 2>&1") | crontab -

(crontab -l 2>/dev/null; echo "5 */4 * * * cd $PROJECT_PATH && $PYTHON_PATH manage.py load_leaderboard >> $PROJECT_PATH/cron.log 2>&1") | crontab -

(crontab -l 2>/dev/null; echo "45 */4 * * * cd $PROJECT_PATH && $PYTHON_PATH manage.py load_teams >> $PROJECT_PATH/cron.log 2>&1") | crontab -

echo "Cron задачи настроены!"
crontab -l