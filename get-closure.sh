#!/usr/bin/env sh

curl https://dl.google.com/closure-compiler/compiler-latest.tar.gz -o - | tar xz compiler.jar
mv compiler.jar closure/closure.jar

java -jar closure/closure.jar  --version
