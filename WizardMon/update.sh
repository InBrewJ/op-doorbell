UPDATE_DIR='workshop/WizardMon'
HOST_DEPENDENCY_A='pi@speakerbox.local'
HOST_DEPENDENCY_B='root@switchbox.local'
HOST_DEPENDENCIES=( "$HOST_DEPENDENCY_A"  "$HOST_DEPENDENCY_B" )

for host in "${HOST_DEPENDENCIES[@]}"
do
   : 
   ssh $host "mkdir -p ~/$UPDATE_DIR" && \
   scp -r ./* $host:$UPDATE_DIR
done
