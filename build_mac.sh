#!/bin/bash

# Variables
APP_NAME="AL Codon Counter"
VERSION="1.0"
INSTALL_LOCATION="/Applications/$APP_NAME"
PKG_ID="com.yourdomain.alcodonapp"
BUILD_DIR="build"
DIST_DIR="dist"
RESOURCES_DIR="resources"

# Clean up previous builds
rm -rf $BUILD_DIR $DIST_DIR
mkdir -p $BUILD_DIR $DIST_DIR

# Create the application bundle
pyinstaller --onefile --windowed --name "AL_CODON_APP" interface_AL_Counter.py

# Create a postinstall script
POSTINSTALL_SCRIPT=$RESOURCES_DIR/postinstall
mkdir -p $RESOURCES_DIR
cat << 'EOF' > $POSTINSTALL_SCRIPT
#!/bin/bash
ln -sf /Applications/AL\ Codon\ Counter/AL_CODON_APP /usr/local/bin/alcodonapp
osascript -e 'tell application "Finder" to make alias file to POSIX file "/Applications/AL Codon Counter/AL_CODON_APP" at POSIX file "/Users/$USER/Desktop"'
EOF
chmod +x $POSTINSTALL_SCRIPT

# Create a component package
pkgbuild --root $DIST_DIR --identifier $PKG_ID --version $VERSION --install-location $INSTALL_LOCATION --scripts $RESOURCES_DIR $BUILD_DIR/$APP_NAME.pkg

# Create a product archive
productbuild --distribution distribution.xml --resources $RESOURCES_DIR --package-path $BUILD_DIR --version $VERSION $DIST_DIR/$APP_NAME.pkg
