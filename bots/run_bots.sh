SESSION=bots

tmux -2 new-session -d -s $SESSION
tmux send-keys "python3.6 insult_bot.py telegram" C-m
tmux new-window -t $SESSION:1 
tmux send-keys "python3.6 plan_bot.py telegram" C-m
tmux new-window -t $SESSION:2
tmux send-keys "python3.6 compliment_bot.py telegram" C-m
tmux new-window -t $SESSION:3
tmux send-keys "python3.6 ilm_bot.py telegram" C-m
tmux new-window -t $SESSION:4
tmux send-keys "python3.6 grammatikanatsibot.py telegram" C-m
tmux new-window -t $SESSION:5
tmux send-keys "python3.6 insult_bot.py discord" C-m
tmux new-window -t $SESSION:6
tmux send-keys "python3.6 plan_bot.py discord" C-m
tmux new-window -t $SESSION:7
tmux send-keys "python3.6 compliment_bot.py discord" C-m
tmux new-window -t $SESSION:8
tmux send-keys "python3.6 ilm_bot.py discord" C-m
tmux new-window -t $SESSION:9
tmux send-keys "python3.6 grammatikanatsibot.py discord" C-m
