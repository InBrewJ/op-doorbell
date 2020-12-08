# Husk = subsystem (like the part of the hazelnut, geddit?)
# Command = something defined in hazel.json

HUSK="$1"
COMMAND="$2"

echo Husk: $HUSK, Command: $COMMAND

if [ "$HUSK" = 'check' ]; then
    ./box_check.sh
else
    FULL_COMMAND=$(jq -r ".$COMMAND" ./"$HUSK"/hazel.json)
    eval "$FULL_COMMAND"
fi


