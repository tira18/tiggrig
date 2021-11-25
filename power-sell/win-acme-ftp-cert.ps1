Import-Module -Name webadministration
$FTPsite = 'IIS:\Sites\ExportsFTP'
$Thumbprint = (Get-ChildItem -path cert:\LocalMachine\WebHosting | Where-Object -Property Subject -eq "CN=exports.kofile.com").Thumbprint
$Current = (Get-ItemProperty -Path $FTPsite -Name ftpServer.security.ssl.serverCertHash).Value

if($Thumbprint -eq $Current) {
   
}else {
   
   Set-ItemProperty -Path $FTPsite -Name ftpServer.security.ssl.serverCertHash -Value $Thumbprint
   Set-ItemProperty -Path $FTPsite -Name ftpServer.security.ssl.serverCertStoreName -Value WebHosting
   echo "NewCert: "$Thumbprint "OldCert"$Current >> c:\log.txt
}

##################################################################
if($Thumbprint -ne $Current) { 

   Set-ItemProperty -Path $FTPsite -Name ftpServer.security.ssl.serverCertHash -Value $Thumbprint
   Set-ItemProperty -Path $FTPsite -Name ftpServer.security.ssl.serverCertStoreName -Value WebHosting
   echo "NewCert: "$Thumbprint "OldCert"$Current >> c:\log.txt
