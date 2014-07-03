set_nodes()
{
    > $TWISTER_HOME/bin/nodes
    
    l=0
    while read line
    do
    let x=$l%%%(ppn)s
    if (($x == 0))
    then
        echo $line >> $TWISTER_HOME/bin/nodes
    fi
    ((l++))
    done < $PBS_NODEFILE
	
    sed -i \"1d\" $TWISTER_HOME/bin/nodes
}
	
set_amq()
{
    read firstline < $PBS_NODEFILE
    sed -i \"53c\uri = failover:(tcp://$firstline:6161)\" $TWISTER_HOME/bin/amq.properties
}
set_nodes
set_amq

cp $TWISTER_HOME/bin/twister.properties

$AMQ_HOME/bin/activemq console &> ~/amq.out &
$TWISTER_HOME/bin/start_twister.sh &> ~/twister.out &

sleep 10

# NOW, RUN FUNCTIONS TO PROCESS DATA!
