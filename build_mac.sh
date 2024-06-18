#!/bin/bash

# Variables
APP_NAME="AL Codon Counter"
VERSION="1.0"
INSTALL_LOCATION="/Applications/$APP_NAME"
PKG_ID="com.yourdomain.$APP_NAME"
BUILD_DIR="build"
DIST_DIR="dist"
RESOURCES_DIR="resources"
PLIST_FILE="$APP_NAME.plist"
SHORTCUT_SCRIPT="create_shortcuts.sh"

# Clean up previous builds
rm -rf $BUILD_DIR $DIST_DIR
mkdir -p $BUILD_DIR $DIST_DIR $RESOURCES_DIR

# Create the application bundle
pyinstaller --onefile --windowed --name "AL_CODON_APP" interface_AL_Counter.py

# Create the .plist file
cat <<EOL > $RESOURCES_DIR/$PLIST_FILE
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>CFBundleName</key>
    <string>$APP_NAME</string>
    <key>CFBundleVersion</key>
    <string>$VERSION</string>
    <key>CFBundleIdentifier</key>
    <string>$PKG_ID</string>
    <key>CFBundleExecutable</key>
    <string>AL_CODON_APP</string>
    <key>CFBundleIconFile</key>
    <string>logo_ICON</string>
</dict>
</plist>
EOL

# Create the shortcut script
cat <<EOL > $RESOURCES_DIR/$SHORTCUT_SCRIPT
#!/bin/bash
# Create a desktop shortcut
ln -s $INSTALL_LOCATION/AL_CODON_APP ~/Desktop/AL_CODON_APP
# Add to Applications folder
cp -R $INSTALL_LOCATION /Applications/
EOL

chmod +x $RESOURCES_DIR/$SHORTCUT_SCRIPT

# Create the install script
cat <<EOL > $RESOURCES_DIR/install.sh
#!/bin/bash
echo "Installing $APP_NAME..."
mkdir -p $INSTALL_LOCATION
cp -r ./* $INSTALL_LOCATION
bash $INSTALL_LOCATION/$SHORTCUT_SCRIPT
echo "$APP_NAME installed successfully."
EOL

chmod +x $RESOURCES_DIR/install.sh

# Create the uninstall script
cat <<EOL > $RESOURCES_DIR/uninstall.sh
#!/bin/bash
echo "Uninstalling $APP_NAME..."
rm -rf $INSTALL_LOCATION
rm -f ~/Desktop/AL_CODON_APP
echo "$APP_NAME uninstalled successfully."
EOL

chmod +x $RESOURCES_DIR/uninstall.sh

# Create a component package
pkgbuild --root $DIST_DIR --identifier $PKG_ID --version $VERSION --install-location $INSTALL_LOCATION $BUILD_DIR/$APP_NAME.pkg

# Create a product archive
productbuild --distribution distribution.xml --resources $RESOURCES_DIR --package-path $BUILD_DIR --version $VERSION $DIST_DIR/$APP_NAME.pkg
