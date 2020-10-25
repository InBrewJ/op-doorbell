UPDATE_DIR='workshop/WizardMon'
ssh pi@speakerbox.local "mkdir -p ~/$UPDATE_DIR" && \
scp -r ./* pi@speakerbox.local:$UPDATE_DIR && \
ssh root@switchbox.local "mkdir -p ~/$UPDATE_DIR" && \
scp -r ./* root@switchbox.local:$UPDATE_DIR