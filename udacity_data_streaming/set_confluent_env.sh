#!/usr/bin/zsh

echo "Setting confluent variables and adding to PATH"

# confluent.io/installation/ -> unzip in references
# https://docs.confluent.io/confluent-cli/current/install.html

export CONFLUENT_HOME=confluent-6.2.0
export CONFLUENT_CURRENT=confluent-cli

export PATH=$PATH:$CONFLUENT_HOME/bin:$CONFLUENT_CURRENT/bin