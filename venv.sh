echo "Installing venv..."
sudo apt install python3-venv

echo "Creating virtual env with name dvenv..."
python3 -m venv dvenv

echo "/dvenv"|cat - .gitignore > /tmp/out && mv /tmp/out .gitignore
echo "Done! Activate using: source dvenv/bin/activate"