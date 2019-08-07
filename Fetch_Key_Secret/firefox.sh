echo "Linux script, for Mac OS install geckodriver manually."
echo ""
echo "Checking latest version..."
wget -q https://github.com/mozilla/geckodriver/releases/latest
version=$(cat latest | sed -n -e 's!.*<title>Release \(.*\)</title>.*!\1!p')
version=$(echo $version | sed 's/ .*//')
echo $version

echo "Installing geckodriver..."
wget https://github.com/mozilla/geckodriver/releases/download/$version/geckodriver-$version-linux64.tar.gz
tar -xvzf geckodriver-$version-linux64.tar.gz
rm geckodriver-$version-linux64.tar.gz
chmod +x geckodriver
cp geckodriver /usr/local/bin/
