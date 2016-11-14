# katastar-ba-downloader

Kreira mape ogromne rezolucije sa katastar.ba geoportala

# Kako koristiti?

* -2. Napravi folder sarajevo na C:\
* -1. Instaliraš Python 2.7
* 0. Instaliraš ImageMagick 

http://www.imagemagick.org/script/binary-releases.php#windows

* 1. Make sure da se može pokrenuti (pokušaj ukucati "convert" u cmd, ako radi, super, ako ne, treba se ImageMagick dodati u PATH environment varijablu)
* 2. Odeš ovdje

http://www.katastar.ba/geoportal/preglednik/

* 3. Zumiraš gdje hoceš
* 4. Otvoriš Developer tools u Chrome, na tab Network
* 5. I sad vidiš da se poziva neki URL slican ovom:

http://katastar.ba:6080/arcgis/rest/services/ORTOFOTO_2012_URBAN/MapServer/tile/9/4742/5217

Klikneš na njega i na dnu, u Headers tabu, piše 

token:QGn_Opo2ISlWviI8bvzEa8FyrLfc5d7ngPiHbafD76thhPFh017Ga9cdY_l_hZAe

Uzmeš taj token, tj. QGn_Opo2ISlWviI8bvzEa8FyrLfc5d7ngPiHbafD76thhPFh017Ga9cdY_l_hZAe
 i vidiš je li vec identican stavljen u skriptu, ako nije, onda ga staviš.

* 6. U skripti na odredenim linijama piše
range(75923, 75933)

i range(83460, 83461)

To su x i y koordinate "tile"-ova od 256x256 pixela. Kako tacno skontati ove brojeve?

U developer tools kad gledaš na onom pregledniku, otvara se URL tipa

http://katastar.ba:6080/arcgis/rest/services/ORTOFOTO_2012_URBAN/MapServer/tile/13/75937/83461

(na najvecem zumu)

Tu su te koordinate, /tile/13/75937/83461, pa dakle u skriptu staviš otprilike odakle dokle hoceš.
13 oznacava zoom level.
