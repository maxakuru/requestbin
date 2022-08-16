#!/bin/bash

COMMAND="/usr/local/bin/supervisord -c /etc/supervisord.conf"

if [ -n "$CLI" ] && [ $CLI = true ]; then
    COMMAND="$@"
fi

echo "starting with command: $COMMAND"

exec $COMMAND