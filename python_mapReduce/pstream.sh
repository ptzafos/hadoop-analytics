hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar -input $1 -output $2 -mapper $3 -reducer $4 -file $3 -file $4
