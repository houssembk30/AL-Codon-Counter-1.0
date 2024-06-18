#!/bin/bash

# Variables
APP_NAME="AL Codon Counter"
VERSION="1.0"
INSTALL_DIR="/usr/local/$APP_NAME"
BUILD_DIR="build"
DIST_DIR="dist"
DESKTOP_FILE="AL_CODON_APP.desktop"
DESKTOP_DIR="$HOME/.local/share/applications"

# Clean up previous builds
rm -rf $BUILD_DIR $DIST_DIR
mkdir -p $BUILD_DIR $DIST_DIR

# Create the application bundle
pyinstaller --onefile --name "AL_CODON_APP" interface_AL_Counter.py

# Create the .desktop file
cat <<EOL > $BUILD_DIR/$DESKTOP_FILE
[Desktop Entry]
Version=$VERSION
Name=$APP_NAME
Comment=Run $APP_NAME
Exec=$INSTALL_DIR/AL_CODON_APP
Icon=$INSTALL_DIR/logo_ICON.png
Terminal=false
Type=Application
Categories=Utility;
EOL

# Create the install script
cat <<EOL > $BUILD_DIR/install.sh
#!/bin/bash
echo "Installing $APP_NAME..."
mkdir -p $INSTALL_DIR
cp -r * $INSTALL_DIR
ln -s $INSTALL_DIR/AL_CODON_APP /usr/local/bin/AL_CODON_APP
cp $INSTALL_DIR/$DESKTOP_FILE $DESKTOP_DIR/$DESKTOP_FILE
chmod +x $DESKTOP_DIR/$DESKTOP_FILE
echo "$APP_NAME installed successfully."
EOL

chmod +x $BUILD_DIR/install.sh

# Create the uninstall script
cat <<EOL > $BUILD_DIR/uninstall.sh
#!/bin/bash
echo "Uninstalling $APP_NAME..."
rm -rf $INSTALL_DIR
rm -f /usr/local/bin/AL_CODON_APP
rm -f $DESKTOP_DIR/$DESKTOP_FILE
echo "$APP_NAME uninstalled successfully."
EOL

chmod +x $BUILD_DIR/uninstall.sh

# Create a makeself installer
makeself --bzip2 $DIST_DIR $BUILD_DIR/$APP_NAME.run "$APP_NAME Installer" ./install.sh
