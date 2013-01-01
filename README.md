IASAS Swimming 2013 Graphics Engine
=========


The graphics keying and overlay engine for the IASAS 2013 swimming broadcast. Runs with a custom external hardware serial decoder and HTML5 WebSockets.

The displayer is separated into two subsections: dynamic and static. The dynamic side handles all the timing console graphics including the running time and splits, and the static side handles the graphics for results and intros. 


Tech
-----------
The engine uses python 2.7 and a number of open source projects:

* [AutoBahn WebSockets] - serial to browser link
* [TKinter] - easy to use python gui package
* [jquery-csv] - csv to jquery object parser
* [LESS] - the dynamic css language
* [jQuery]


<!-- Installation
--------------
1. Clone the repo
2. `cd dillinger`
3. `npm i`
4. `mkdir -p public/files`
5. `mkdir -p public/files/md && mkdir -p public/files/html`
6. `sudo node app`
-->

License
-
<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/3.0/deed.en_US"><img alt="Creative Commons License" style="border-width:0;align:center;" src="http://i.creativecommons.org/l/by-nc-sa/3.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/3.0/deed.en_US">Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License</a>.

  [AutoBahn WebSockets]: http://autobahn.ws/
  [TKinter]: http://wiki.python.org/moin/TkInter
  [jquery-csv]: http://code.google.com/p/jquery-csv/
  [LESS]: https://github.com/cloudhead/less.js
  [jQuery]: http://jquery.com  
  
    