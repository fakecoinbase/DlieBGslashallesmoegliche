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

<h4>Schwering Software DynDNS Service.</h4>
<br>

<?php
$files = scandir("/var/www/lokal/dynDNS");

foreach($files as $file)
{
if(strpos($file, ".ip"))
{
?>
<a href="index.php?<?php print(str_replace(".ip","",$file));?>">
<?php
print(str_replace(".ip","",$file));
?>
</a>
<br>
<?php
}
}
?>

