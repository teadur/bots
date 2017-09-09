SESSION=bots

tmux -2 new-session -d -s $SESSION
tmux send-keys "python insult_bot.py telegram" C-m
tmux new-window -t $SESSION:1 
tmux send-keys "python plan_bot.py telegram" C-m
tmux new-window -t $SESSION:2
tmux send-keys "python compliment_bot.py telegram" C-m
tmux new-window -t $SESSION:3
tmux send-keys "python ilm_bot.py telegram" C-m
tmux new-window -t $SESSION:4
tmux send-keys "python grammatikanatsibot.py telegram" C-m
tmux new-window -t $SESSION:5
tmux send-keys "python insult_bot.py discord" C-m
tmux new-window -t $SESSION:6
tmux send-keys "python plan_bot.py discord" C-m
tmux new-window -t $SESSION:7
tmux send-keys "python compliment_bot.py discord" C-m
tmux new-window -t $SESSION:8
tmux send-keys "python ilm_bot.py discord" C-m
tmux new-window -t $SESSION:9
tmux send-keys "python grammatikanatsibot.py discord" C-m
