a
    �B$a�  �                   @   sB  d Z ddlZddlZdZee� ed�Ze�de� ��Ze�	ej
�ZejZedk�r.ede� d�� ed	� ed
ed  � edeed � d eed � � edeed � d eed � � edeed � � edeed � � edeed � d eed � � edeed � � ed	� nede� d�� dS )zZ
ingfo

http://ip-api.com/json/{query}
https://www.google.co.id/maps/@{lon},{lat},{zoom}z
�    Nz�
Tools IpLocation By        
--------------------------------
[+] Creator: Tn.Mouri
[+] Youtube: KUVIANTIINDONESIANET
---------------------------------
zMasukan IP Address : zhttp://ip-api.com/json/��   z
[+] berhasil, z alamat ip dijumpaiz------------------------------zaddress  : Zqueryzcountry  : Zcountry� ZcountryCodezregion   : Z
regionNameZregionzcity     : Zcityzzipcode  : �zipzlocation : Zlatz, Zlonztimezone : �timezonez[!] error, z alamat ip ini tidak ditemukan)�__doc__ZrequestsZjsonZbanner�print�inputZip�get�r�loads�textZresponse_jsonZstatus_codeZresponse_code�str� r   r   �lacak.py�<module>   s(   
$$$
