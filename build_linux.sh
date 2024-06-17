#!/bin/bash

# Variables
APP_NAME="AL Codon Counter"
VERSION="1.0"
INSTALL_DIR="/usr/local/$APP_NAME"
BUILD_DIR="build"
DIST_DIR="dist"

# Clean up previous builds
rm -rf $BUILD_DIR $DIST_DIR
mkdir -p $BUILD_DIR $DIST_DIR

# Create the application bundle
pyinstaller --onefile --name "AL_CODON_APP" interface_AL_Counter.py

# Create a makeself installer
makeself --bzip2 $DIST_DIR $BUILD_DIR/$APP_NAME.run "$APP_NAME Installer" ./install.sh

# Create an install script
cat <<EOL > $BUILD_DIR/install.sh
#!/bin/bash
echo "Installing $APP_NAME..."
mkdir -p $INSTALL_DIR
cp -r * $INSTALL_DIR
ln -s $INSTALL_DIR/AL_CODON_APP /usr/local/bin/AL_CODON_APP
echo "$APP_NAME installed successfully."
EOL

chmod +x $BUILD_DIR/install.sh
