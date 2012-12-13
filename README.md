HTSmission3
===========

Solution for hackthissite.org programming mission 3 written in python. This an explanation of the encryption function 
and an example of a solution to guide you on making your own solution if you are stuck.
Don't just copy and paste! That ruins the purpose of HTS...

Here's how the PHP encryption function with explanation on how it works:
The encryption algorithm written in php:
    <?php

    //------------------------------------------------------------------------------------
    function evalCrossTotal($strMD5) 
    {
    $intTotal = 0;
    $arrMD5Chars = str_split($strMD5, 1); //put characters into array
    foreach ($arrMD5Chars as $value) 
    {
      $intTotal += '0x0'.$value; //turn char to hexadecimal value and add it to $intTotal
    }
    return $intTotal;
    }//-----------------------------------------------------------------------------------


    //------------------------------------------------------------------------------------
    function encryptString($strString, $strPassword)
    {
    //$strString is the content of the entire file with serials, $strPassword is not known and this is what we brute force
    $strPasswordMD5 = md5($strPassword); //Encrypt password with md5
    $intMD5Total = evalCrossTotal($strPasswordMD5); //$intMD5Total is the hexadecimal sum of the MD5 Encrypted password
    $arrEncryptedValues = array();
    $intStrlen = strlen($strString);
    for ($i=0; $i<$intStrlen; $i++)
    {
      $arrEncryptedValues[] =  ord(substr($strString, $i, 1))                   
                                     +  ('0x0' . substr($strPasswordMD5, $i%32, 1))   
                                     -  $intMD5Total;                                 
      $intMD5Total = evalCrossTotal(substr(md5(substr($strString,0,$i+1)), 0, 16) 
                                                                               
                                     .  substr(md5($intMD5Total), 0, 16));            
    }
    return implode(' ' , $arrEncryptedValues);  
    }//-----------------------------------------------------------------------------------

    ?> 
info about encrypted string: 100 characters total. '\n' char every 20th char(except for last), 
'-' separates every 3 chars(excluding \n), 'OEM' is 9-11 chars and '1.1' is 17-19 chars

important: every 32 values, ('0x0' . subsrt($strPasswordMD5, $i%32,1)) repeats

first $intMD5Total = (ascii value of first char of unencrypted string) + 
(hexadecimal value of first character of MD5-encrypted pass) - arrEncryptedValues[0]

second $intMD5Total = sum of [(first 16 chars of (MD5 of (ascii value of first char))  concatenated with 
(first 16 characters of (MD5 of (first $intTotal)))]
