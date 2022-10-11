#!/bin/bash

function purge_input_mapred_on_namenode {
    docker exec -it namenode rm -rf input &> /dev/null
    docker exec -it namenode rm mapper.py &> /dev/null
    docker exec -it namenode rm reducer.py &> /dev/null
    docker exec -it namenode rm run_mapred.sh &> /dev/null
}


function copy_input_mapred_to_namenode {
    docker cp penjualan_motor/input namenode:input
    docker cp penjualan_motor/mapper.py namenode:mapper.py
    docker cp penjualan_motor/reducer.py namenode:reducer.py
    docker cp penjualan_motor/scripts/run_mapred.sh namenode:run_mapred.sh
}

# Main - Install Hadoop MapReducer for Python onto `namenode`
purge_input_mapred_on_namenode
copy_input_mapred_to_namenode
