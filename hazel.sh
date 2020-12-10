# Husk = subsystem (like the part of the hazelnut, geddit?)
# Command = something defined in hazel.json
# Usage
# ./hazel.sh WizardMon update
# ./hazel.sh Switchbox update
# ./hazel.sh check

HUSK="$1"
COMMAND="$2"

echo Husk: $HUSK, Command: $COMMAND

if [ "$HUSK" = 'check' ]; then
    ./box_check.sh
elif [ "$COMMAND" = 'update' ]; then
    pushd "./$HUSK/"
    FULL_COMMAND=$(jq -r ".$COMMAND" ./hazel.json)
    eval "$FULL_COMMAND"
    popd
else
    FULL_COMMAND=$(jq -r ".$COMMAND" ./"$HUSK"/hazel.json)
    eval "$FULL_COMMAND"
fi


