envD="venvl"

if [ -d "$envD" ]; then
	rm -rf $envD
fi

source $envD/bin/activate
python -m pip install --upgrade pip
python -m pip install -I -r requirements.txt
