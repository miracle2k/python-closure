#!/usr/bin/env sh

curl http://closure-compiler.googlecode.com/files/compiler-latest.tar.gz -o - | tar xz compiler.jar
mv compiler.jar closure/closure.jar
