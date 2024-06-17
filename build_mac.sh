#!/bin/bash

# Variables
APP_NAME="AL Codon Counter"
VERSION="1.0"
INSTALL_LOCATION="/Applications/$APP_NAME"
PKG_ID="com.yourdomain.$APP_NAME"
BUILD_DIR="build"
DIST_DIR="dist"

# Clean up previous builds
rm -rf $BUILD_DIR $DIST_DIR
mkdir -p $BUILD_DIR $DIST_DIR

# Create the application bundle
pyinstaller --onefile --windowed --name "AL_CODON_APP" interface_AL_Counter.py

# Create a component package
pkgbuild --root $DIST_DIR --identifier $PKG_ID --version $VERSION --install-location $INSTALL_LOCATION $BUILD_DIR/$APP_NAME.pkg

# Create a product archive
productbuild --distribution distribution.xml --resources resources --package-path $BUILD_DIR --version $VERSION $DIST_DIR/$APP_NAME.pkg
