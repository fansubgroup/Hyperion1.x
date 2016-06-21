# Hyperion1.x

This is the core component of 2.x and 3.x

But also supports the translation work under the command line

### We now have two version of the software in 1.0

One is `hpn.py`, and one is `hpn_plus.py`

So, what is the difference between them?

#### [1] First, `hpn_plus.py` is based on a completely new structure

For online translation, it is very important for the HTTP module has been use C language reconstruction and compliation, making this module the probability if error is very small

If you are going to deal with a large number of paragraphs, we recommend that you use `hpn_plus.py`

#### [2] Second, but this is not to say that `hpn.py` is not good

`hpn.py` is the oldest version, and the smallest package dependency, this means that your computer only needs to install the `Python` to run the program

But the `hpn.py` process a large number of data will appear whrn the network blocking and the collapse of the program 

### How to use these language(the usage of two version is same)?

* Download the entrie folder to your local directory

* Install the `Python`

* In the program directory, there is a configure file name `appkey`, Input you `appid` in the first line, and the `sercetKey` in second line 

* Use the `cmd` (Windows) or `shell` (Linux) switch to the place where you put the program

* Input the command in `cmd` (Windows) or `shell` (Linux) like this:
```
./hpn.py YOU_SOURCE_LANGUAGE YOU_TARGET_LANGUAGE
```
or
```
./hpn_plus.py YOU_SOURCE_LANGUAGE YOU_TARGET_LANGUAGE
```

## User attention using `hpn_plus.py`

We have been working to deal with errors that can occur in any program, but this will inevitably be an unexpected error in the program

In order to make the program not because of some unknown mistakes, stop halfway down, take some of the `necessary` measures

If you find that you would have to eb trnaslated into `Spanish` is `Japanses` appear, that is `not` a translation error, is we to remind you, this paragraph of word cannot transmitted via HTTP to the API to translate, so the display into `Japanses` to remind you from the text to find the corresponding words and translation by youself.

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

