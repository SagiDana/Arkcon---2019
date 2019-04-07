<?php

function x0r($string, $magic_key) {
     #https://stackoverflow.com/questions/14673551/encrypt-decrypt-with-xor-in-php 
} 

$flag = "ArkCon{?}"; 
$list = array('crc32', 'md5', 'sha1'); 
$algo = $list[array_rand($list)]; 


if (!empty($_POST['key']) || !empty($_POST['harame'])){ 
    $basket = hash($algo, x0r($flag, $_POST['key'])); 
    $harame = hash($algo, strrev($_POST['harame'])); 
} else{ 
    echo ("Please closed the door behind you\n"); 
    exit; 
} 
$code = "20190429_71070_e7707_1312_3_14159265359"; 


if (!empty($_POST['coach']) || !empty($_POST['jersey'])) 
    $basket = str_replace("_", $_POST['coach'], substr($code, $_POST['jersey']).substr($code, 0, $_POST['jersey'])); 

echo ("HARAME!\n"); 
$ball = hash('md5', $basket); 

if (isset($_POST['ball']) && isset($_POST['jersey'])){
    $ball = substr(x0r(pack("H*", $_POST['ball']), $ball), -8) * $_POST['jersey']; 
    $harame = hash($algo, x0r($harame, $basket)); 
} 

if( $basket != hash($algo, $ball)) exit;

$key = hash($algo, $harame); 
echo ("A hint:" . str_shuffle($key . $flag) . "\n");
if ($key == $_POST['key']) echo ("You are the GOAT: " . $flag); 
exit;

?>