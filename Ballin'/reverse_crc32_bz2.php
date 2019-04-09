<?php

$i = 0;
while (true){
    if (hash('crc32', $i) == '0'){
        echo $i;
        echo '\n';
        break;
    }
    
       
    $i =$i+ 14;
}
