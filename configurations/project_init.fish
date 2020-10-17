set SCRIPT_DIR (cd (dirname (status -f)); and pwd)

set PROJECT_DIR $SCRIPT_DIR/..

set RELATIVE_GITS_PATH "code/gits.py"

set GITS_EXEC_PATH "$PROJECT_DIR/$RELATIVE_GITS_PATH"

set FISHRC ~/.config/fish/conf.d/virtualfish-loader.fish

if [ -f "$FISHRC" ];
    echo "$FISHRC exists, appending gits commandline tool alias"
    echo "alias gits=\"python3 $GITS_EXEC_PATH\"" >> $FISHRC
else
    echo "$FISHRC does not exist, creating a new file and adding gits commandline tool alias"
    echo "alias gits=\"python3 $GITS_EXEC_PATH\"" >> $FISHRC
end

echo "Intializing gits directory in user home directory"

set GITS ~/.gits
set GITS_LOG ~/.gits/logs

mkdir -p $GITS $GITS_LOG
