NUM_TEST_PINGS=2
TEST_DELAY=5
DIVIDER='----------------------------------------'

function print_divider {
    echo $DIVIDER
    echo $DIVIDER
}

function check {
    print_divider
    ping -c $NUM_TEST_PINGS speakerbox.local
    print_divider
    ping -c $NUM_TEST_PINGS switchbox.local 
    print_divider
}

while true; do 
    check
    sleep $TEST_DELAY
    clear
done

