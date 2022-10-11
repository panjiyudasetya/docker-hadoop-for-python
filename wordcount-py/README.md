# Quick Start

To run the Python `wordcount` project in Hadoop containers:
- Copy-paste the `docker-compose.yml.example` into the `docker-compose.yml`.
- Deploy the HDFS cluster, run `$ docker-compose up`.
- Executes the script `$ ./wordcount-py/scripts/install.sh`.
- Enter to the `namenode` container `$ docker exec -it namenode bash`, and executes the script `$ ./run_wordcount.sh`.
