NUM_TEST_PINGS=2
DIVIDER='----------------------------------------'
echo $DIVIDER
echo $DIVIDER
ping -c $NUM_TEST_PINGS speakerbox.local
echo $DIVIDER 
echo $DIVIDER
ping -c $NUM_TEST_PINGS switchbox.local 
echo $DIVIDER
echo $DIVIDER
