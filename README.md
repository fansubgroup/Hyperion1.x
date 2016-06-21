# Hyperion1.x

This is the core of the GUI.

### In order to better service interface for Hyperion2.x or Hyperion3.x

#### And better for subtitle Group Services, so we made this software

#### Enter the source language and target language in the program to use

#### This coeerspondence table is here

<table>
<tr>
      <td>Symbol</td>
      <td>Significance</td>
   </tr>
   <tr>
      <td>auto </td>
      <td>automatic detection</td>
   </tr>
   <tr>
      <td>zh </td>
      <td>Chinese</td>
   </tr>
   <tr>
      <td>en </td>
      <td>English</td>
   </tr>
   <tr>
      <td>yue </td>
      <td>Cantonese</td>
   </tr>
   <tr>
      <td>wyw </td>
      <td>Classical Chinese</td>
   </tr>
   <tr>
      <td>jp </td>
      <td>Japanese</td>
   </tr>
   <tr>
      <td>kor </td>
      <td>Korean</td>
   </tr>
   <tr>
      <td>fra </td>
      <td>French</td>
   </tr>
   <tr>
      <td>spa </td>
      <td>Spain</td>
   </tr>
   <tr>
      <td>th </td>
      <td>Thai</td>
   </tr>
   <tr>
      <td>ara </td>
      <td>Arabic</td>
   </tr>
   <tr>
      <td>ru </td>
      <td>Russian</td>
   </tr>
   <tr>
      <td>pt </td>
      <td>Portuguese</td>
   </tr>
   <tr>
      <td>de </td>
      <td>German</td>
   </tr>
   <tr>
      <td>it </td>
      <td>Italian</td>
   </tr>
   <tr>
      <td>el </td>
      <td>Greek</td>
   </tr>
   <tr>
      <td>nl </td>
      <td>Dutch</td>
   </tr>
   <tr>
      <td>pl </td>
      <td>Polish</td>
   </tr>
   <tr>
      <td>bul </td>
      <td>Bulgarian</td>
   </tr>
   <tr>
      <td>est </td>
      <td>Estonia Language</td>
   </tr>
   <tr>
      <td>dan </td>
      <td>Danish</td>
   </tr>
   <tr>
      <td>fin </td>
      <td>Finnish</td>
   </tr>
   <tr>
      <td>cs </td>
      <td>Czech</td>
   </tr>
   <tr>
      <td>rom </td>
      <td>Romanian</td>
   </tr>
   <tr>
      <td>slo </td>
      <td>Slovenia Language</td>
   </tr>
   <tr>
      <td>swe </td>
      <td>Swedish</td>
   </tr>
   <tr>
      <td>hu </td>
      <td>Hugarian language</td>
   </tr>
   <tr>
      <td>cht </td>
      <td>Traditional Chinese</td>
   </tr>
</table>



### So, how to use these language?

* In the file, we have a file name `hyn.py`.

* You can change it with you `text editor`.

* Source language is in the `216` line.

* Target language is in the `217` line.



#### However, please note that the use of the `text editor` to change this file should be the same as the original file format.



### Steps

* The first step you should enter the source file part of name.

* If you want to use the default configuration, that is, the English to Chinese translation, `press enter`.

* If not, you can refer to the `above steps` to modify the settings to achieve you intended purpose.


### hpy_plus.py useage

* with the file xhttp.so

* You can edit the xhttp.c to get more fuction

* do this with xhttp.c

```
gcc -shared -I/usr/include/python2.7 -fPIC xhttp.c -lcurl -lssl -pthread -o xhttp.so
```
