###########################################
# RUN KAFKA
###########################################
# there are 4 ways to start a kafka broker
# please refer to the README.md
# easiest version is to start confluent docker

# following commands start binary kafka from the reference folder
# first run the following command
# source set_kafka_vars.sh
# to set the env - please check that the path is correct

###########################################
# BINARY
###########################################

clear_kafka:
	make load_env
	# the directories can be set at kafka_2.13.2.8.0/config/server.properties and zookeeper.properties
	@rm -rf $$KAFKA_HOME/kafka-logs $$KAFKA_HOME/logs $$KAFKA_HOME/zookeeper-data

kafka_up:
	@echo "starting zookeeper..."
	@bash $$KAFKA_HOME/bin/zookeeper-server-start.sh -daemon $$KAFKA_HOME/config/zookeeper.properties
	@echo "starting kafka..."
	@bash $$KAFKA_HOME/bin/kafka-server-start.sh -daemon $KAFKA_HOME/config/server.properties

kafka_down:
	@echo "stopping zookeeper..."
	@bash $$KAFKA_HOME/bin/zookeeper-server-stop.sh
	@echo "stopping kafka..."
	@bash $$KAFKA_HOME/bin/kafka-server-stop.sh

# following commands start binary confluent kafka from the reference folder
# first run the following command

# source set_confluent_vars.sh
# to set the env - please check that the path is correct

clear_confluent:
	make load_env
	# the directories can be set at confluent-6.2.0/config/server.properties and zookeeper.properties
	@rm -rf $$CONFLUENT_HOME/kafka-logs $$CONFLUENT_HOME/logs $$CONFLUENT_HOME/zookeeper-data

confluent_up:
	@echo "starting zookeeper..."
	@bash $$CONFLUENT_HOME/bin/zookeeper-server-start -daemon $$CONFLUENT_HOME/config/zookeeper.properties
	@echo "starting kafka..."
	@bash $$CONFLUENT_HOME/bin/kafka-server-start -daemon $CONFLUENT_HOME/config/server.properties

confluent_down:
	@echo "stopping zookeeper..."
	@bash $$CONFLUENT_HOME/bin/zookeeper-server-stop
	@echo "stopping kafka..."
	@bash $$CONFLUENT_HOME/bin/kafka-server-stop

confluent_up:

###########################################
# docker
###########################################

# following commands start kafka with docker
kafka_list = zookeeper kafka

dev_kafka:
	@cd references
	@echo "start kafka in dev mode"
	@docker-compose up -f docker-compose.wurst.yaml -d $(kafka_list)

log_kafka:
	@cd references
	@echo "log kafka"
	@docker-compose logs -f $(kafka_list)

# following commands start confluents' kafka with docker
confluent_list = zookeeper broker schema-registry connect control-center ksqldb-server ksqldb-cli ksql-datagen rest-proxy 

dev_confluent:
	@echo "start confluent in dev mode"
	@docker-compose up -d $(confluent_list)

log_confluent:
	@echo "log confluent"
	@docker-compose logs -f $(confluent_list)