#!/usr/bin/zsh

echo "Setting kafka variables and adding to PATH"

export KAFKA_HOME=kafka_2.13-2.8.0

export PATH=$PATH:$KAFKA_HOME/bin