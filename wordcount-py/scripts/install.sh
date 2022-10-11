#!/bin/bash


function purge_wordcount_on_namenode {
    docker exec -it namenode rm -rf input &> /dev/null
    docker exec -it namenode rm mapper.py &> /dev/null
    docker exec -it namenode rm reducer.py &> /dev/null
    docker exec -it namenode rm run_wordcount.sh &> /dev/null
}


function copy_wordcount_to_namenode {
    docker cp wordcount-py/input namenode:input
    docker cp wordcount-py/mapper.py namenode:mapper.py
    docker cp wordcount-py/reducer.py namenode:reducer.py
    docker cp wordcount-py/scripts/run_wordcount.sh namenode:run_wordcount.sh
}

# Main - Install Hadoop MapReducer for Python `wordcount` onto `namenode`
purge_wordcount_on_namenode
copy_wordcount_to_namenode
