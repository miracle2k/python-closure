#!/usr/bin/env sh

set -e

rm -f closure/closure.jar


DOWNLOAD_DIR="$(pwd)/download"
mkdir -p "$DOWNLOAD_DIR"
curl https://dl.google.com/closure-compiler/compiler-latest.tar.gz -o - | tar xz -C "$DOWNLOAD_DIR"
mv $DOWNLOAD_DIR/*.jar closure/closure.jar
rm -rf "$DOWNLOAD_DIR"

java -jar closure/closure.jar  --version
