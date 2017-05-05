SESSION=bots

tmux -2 new-session -d -s $SESSION
tmux send-keys "python insult_bot.py" C-m
tmux new-window -t $SESSION:1 
tmux send-keys "python plan_bot.py" C-m
tmux new-window -t $SESSION:2
tmux send-keys "python compliment_bot.py" C-m
tmux new-window -t $SESSION:3
tmux send-keys "python ilm_bot.py" C-m
tmux new-window -t $SESSION:4
tmux send-keys "python grammatikanatsibot.py" C-m
