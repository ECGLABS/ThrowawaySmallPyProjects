#!/bin/bash

# Define bad websites (case-insensitive)
BLOCKED_SITES=("youtube.com" "reddit.com" "twitter.com")

# Set how long in seconds you’re allowed to linger on a bad site before action
MAX_TIME=60

# Loop every 5 seconds
INTERVAL=5

echo "🐶 Focus Guard activated. Watching your browsing habits..."

while true; do
    for site in "${BLOCKED_SITES[@]}"; do
        # Search for matching tabs
        tab_info=$(wmctrl -l -x | grep -i "$site")
        if [[ -n "$tab_info" ]]; then
            echo "⚠️  Detected $site – Stay focused!"
            count=0
            while [[ $count -lt $MAX_TIME ]]; do
                sleep $INTERVAL
                tab_info=$(wmctrl -l -x | grep -i "$site")
                if [[ -z "$tab_info" ]]; then
                    echo "✅ You left $site. Good job!"
                    break
                fi
                ((count+=INTERVAL))
            done
            if [[ $count -ge $MAX_TIME ]]; then
                echo "💣 You've been on $site too long. Closing it!"
                # Try to close browser window using wmctrl
                wmctrl -c "$(echo "$tab_info" | awk '{$1=$2=$3=""; print $0}' | xargs)"
            fi
        fi
    done
    sleep $INTERVAL
done
