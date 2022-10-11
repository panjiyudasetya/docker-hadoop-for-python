# Description
This document explains the functionality of the `penjualan_motor/scripts`.
 
## `/install.sh`
- The script will copy all associated files of the Hadoop Python wordcount project to the `namenode` container.
- You need to execute this script once the `namenode` service is up from your command line.
  i.e. `$ penjualan_motor/scripts/install.sh`

## `/run_mapred.sh`
- The script will execute Hadoop command to run the Python `penjualan_motor` MapReducer via Hadoop Streaming library.
- You need to ensure all Hadoop services are up, and execute this script within the `namenode` container.
- Executes this command `$ docker exec -it namenode bash` to get into the `namenode` container.
- After that, execute the script through `$ ./run_mapred.sh`.
