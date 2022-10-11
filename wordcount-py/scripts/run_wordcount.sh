#!/bin/bash


function purge_hadoop_io_dirs {
    # Purge the Hadoop Distributed File System (HDFS) I/O directories
    hdfs dfs -rm -r input/*
    hdfs dfs -rm -r output
}


function load_hadoop_input {
    # Create a new HDFS `input` directory and put all the associate input files
    # from `wordcount-py/input/` local directory into HDFS `input` directory
    hdfs dfs -mkdir input
    hdfs dfs -put input/* input
}


function run_hadoop_mapreducer {
    # Use Hadoop Streaming for running the Python MapReduce
    hadoop jar $HADOOP_STREAMING_HOME/hadoop-streaming-3.2.1.jar \
    -file mapper.py    -mapper "python3 mapper.py" \
    -file reducer.py   -reducer "python3 reducer.py" \
    -input input -output output
}


function print_hadoop_output {
    hdfs dfs -cat output/*
}


# Main - Run Hadoop MapReducer for Python `wordcount`
purge_hadoop_io_dirs
load_hadoop_input
run_hadoop_mapreducer
print_hadoop_output
