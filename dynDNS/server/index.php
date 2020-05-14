<?php
if(isset($_GET['set']))
{
file_put_contents($_GET['set'].'.ip', $_SERVER['REMOTE_ADDR']);
}

foreach ($_GET as $key => $value)
{
$ip = file_get_contents($key.'.ip');
header('Location: http://'.$ip.'/');
}
?>

Schwering Software DynDNS Service.

