import requests
import csv

#inputFile = open('urls-in.csv')
#inputReader = csv.reader(inputFile)
schools = []
with open('urls-in.csv', 'r') as f:
	reader = csv.reader(f)
	schools = list(reader)
	print schools
writer = csv.writer(open('urls-out.csv', 'wb'))
schools = ["http://www.google.com/search?q=ACADEMY+OF+ST+BENEDICT+THE+AFRICAN+CHICAGO&btnI",
"http://www.google.com/search?q=ACADEMY+OF+ST+BENEDICT+THE+AFRICAN-STEWART+CAMPUS+CHICAGO&btnI",
"http://www.google.com/search?q=ALL+SAINTS+ACADEMY+BREESE&btnI",
"http://www.google.com/search?q=ALL+SAINTS+CATHOLIC+ACADEMY+NAPERVILLE&btnI",
"http://www.google.com/search?q=ALPHONSUS+ACADEMY+&+CENTER+FOR+THE+ARTS+CHICAGO&btnI",
"http://www.google.com/search?q=ALTHOFF+CATHOLIC+HIGH+SCHOOL+BELLEVILLE&btnI",
"http://www.google.com/search?q=ALTUS+ACADEMY+CHICAGO&btnI",
"http://www.google.com/search?q=ANNUNCIATA+SCHOOL+CHICAGO&btnI",
"http://www.google.com/search?q=AQUIN+CATHOLIC+JR+SR+HIGH+SCHOOL+FREEPORT&btnI",
"http://www.google.com/search?q=AQUIN+ELEMENTARY+SCHOOL+FREEPORT&btnI",
"http://www.google.com/search?q=AQUINAS+CATHOLIC+ACADEMY-HICKORY+KANKAKEE&btnI",
"http://www.google.com/search?q=ASCENSION+ELEMENTARY+SCHOOL+OAK PARK&btnI",
"http://www.google.com/search?q=AURORA+CENTRAL+CATHOLIC+HIGH+SCHOOL+AURORA&btnI",
"http://www.google.com/search?q=BENET+ACADEMY+LISLE&btnI",
"http://www.google.com/search?q=BISHOP+MCNAMARA+CATHOLIC+HIGH+SCHOOL+KANKAKEE&btnI",
"http://www.google.com/search?q=BLESSED+SACRAMENT+CATHOLIC+SCHOOL+QUINCY&btnI",
"http://www.google.com/search?q=BLESSED+SACRAMENT+ELEMENTARY+SCHOOL+BELLEVILLE&btnI",
"http://www.google.com/search?q=BLESSED+SACRAMENT+SCHOOL+MORTON&btnI",
"http://www.google.com/search?q=BOYLAN+CATHOLIC+HIGH+SCHOOL+ROCKFORD&btnI",
"http://www.google.com/search?q=BR+RICE+HIGH+SCHOOL+CHICAGO&btnI",
"http://www.google.com/search?q=BRIDGEPORT+CATHOLIC+-+S+CAMPUS+CHICAGO&btnI",
"http://www.google.com/search?q=CARDINAL+BERNARDIN+EARLY+CHILDHOOD+CENTER+CHICAGO&btnI",
"http://www.google.com/search?q=CARDINAL+JOSEPH+BERNARDIN+CATHOLIC+SCHOOL+ORLAND HILLS&btnI",
"http://www.google.com/search?q=CARMEL+CATHOLIC+HIGH+SCHOOL+MUNDELEIN&btnI",
"http://www.google.com/search?q=CATHEDRAL+GRADE+SCHOOL+BELLEVILLE&btnI",
"http://www.google.com/search?q=CATHEDRAL+SCHOOL+SPRINGFIELD&btnI",
"http://www.google.com/search?q=CATHOLIC+DAYCARE+CENTER+EAST SAINT LOUIS&btnI",
"http://www.google.com/search?q=CENTRAL+CATHOLIC+HIGH+SCHOOL+BLOOMINGTON&btnI",
"http://www.google.com/search?q=CHILDREN+OF+PEACE+SCHOOL+CHICAGO&btnI",
"http://www.google.com/search?q=CHRIST+OUR+SAVIOR+CATHOLIC+SCHOOL+SOUTH HOLLAND&btnI",
"http://www.google.com/search?q=CHRIST+THE+KING+EARLY+LEARNING+ACADEMY+LOMBARD&btnI",
"http://www.google.com/search?q=CHRIST+THE+KING+ELEMENTARY+SCHOOL+CHICAGO&btnI",
"http://www.google.com/search?q=CHRIST+THE+KING+ELEMENTARY+SCHOOL+SPRINGFIELD&btnI",
"http://www.google.com/search?q=CHRIST+THE+KING+JESUIT+COLLEGE+PREPARATORY+SCHOOL+CHICAGO&btnI",
"http://www.google.com/search?q=COSTA+CATHOLIC+SCHOOL+GALESBURG&btnI",
"http://www.google.com/search?q=CRISTO+REY+JESUIT+HIGH+SCHOOL+CHICAGO&btnI",
"http://www.google.com/search?q=CRISTOREY+ST.+MARTIN+WAUKEGAN&btnI",
"http://www.google.com/search?q=DE+LA+SALLE+INSTITUTE+-+INSTITUTE+CAMPUS+CHICAGO&btnI",
"http://www.google.com/search?q=DIVINE+INFANT+JESUS+SCHOOL+WESTCHESTER&btnI",
"http://www.google.com/search?q=DIVINE+PROVIDENCE+SCHOOL+WESTCHESTER&btnI",
"http://www.google.com/search?q=EAST+LAKE+ACADEMY+LAKE FOREST&btnI",
"http://www.google.com/search?q=EPIPHANY+CATHOLIC+SCHOOL+NORMAL&btnI",
"http://www.google.com/search?q=EVEREST+ACADEMY+LEMONT&btnI",
"http://www.google.com/search?q=FATHER+MCGIVNEY+CATHOLIC+HIGH+SCHOOL+MARYVILLE&btnI",
"http://www.google.com/search?q=FENWICK+HIGH+SCHOOL+OAK PARK&btnI",
"http://www.google.com/search?q=FRANCES+XAVIER+WARDE+SCHOOL+CHICAGO&btnI",
"http://www.google.com/search?q=FRANCISCAN+LEARNING+CENTER+JOLIET&btnI",
"http://www.google.com/search?q=GIBAULT+CATHOLIC+HIGH+SCHOOL+WATERLOO&btnI",
"http://www.google.com/search?q=GORDON+TECH+HIGH+SCHOOL+CHICAGO&btnI",
"http://www.google.com/search?q=GUERIN+PREP+HIGH+SCHOOL+RIVER GROVE&btnI",
"http://www.google.com/search?q=HALES+FRANCISCAN+HIGH+SCHOOL+CHICAGO&btnI",
"http://www.google.com/search?q=HENRYK+SIENKIEWICZ+SUMMIT&btnI",
"http://www.google.com/search?q=HOLY+ANGELS+CHICAGO&btnI",
"http://www.google.com/search?q=HOLY+CHILDHOOD+SCHOOL+MASCOUTAH&btnI",
"http://www.google.com/search?q=HOLY+CROSS+CATHOLIC+SCHOOL+BATAVIA&btnI",
"http://www.google.com/search?q=HOLY+CROSS+ELEMENTARY+SCHOOL+CHAMPAIGN&btnI",
"http://www.google.com/search?q=HOLY+CROSS+ELEMENTARY+SCHOOL+MENDOTA&btnI",
"http://www.google.com/search?q=HOLY+CROSS+SCHOOL+DEERFIELD&btnI",
"http://www.google.com/search?q=HOLY+FAMILY+CATHOLIC+ACADEMY+INVERNESS&btnI",
"http://www.google.com/search?q=HOLY+FAMILY+CATHOLIC+SCHOOL+BENSENVILLE&btnI",
"http://www.google.com/search?q=HOLY+FAMILY+CATHOLIC+SCHOOL+DECATUR&btnI",
"http://www.google.com/search?q=HOLY+FAMILY+CATHOLIC+SCHOOL+ROCKFORD&btnI",
"http://www.google.com/search?q=HOLY+FAMILY+ELEMENTARY+SCHOOL+OGLESBY&btnI",
"http://www.google.com/search?q=HOLY+FAMILY+PARISH+SCHOOL+PEORIA&btnI",
"http://www.google.com/search?q=HOLY+FAMILY+SCHOOL+SHOREWOOD&btnI",
"http://www.google.com/search?q=HOLY+GHOST+SCHOOL+WOOD DALE&btnI",
"http://www.google.com/search?q=HOLY+TRINITY+CATHOLIC+SCHOOL+FAIRVIEW HEIGHTS&btnI",
"http://www.google.com/search?q=HOLY+TRINITY+HIGH+SCHOOL+CHICAGO&btnI",
"http://www.google.com/search?q=HOLY+TRINITY+SCHOOL+WESTMONT&btnI",
"http://www.google.com/search?q=IC+CATHOLIC+PREP+ELMHURST&btnI",
"http://www.google.com/search?q=IMMACULATE+CONCEPTION+COLUMBIA&btnI",
"http://www.google.com/search?q=IMMACULATE+CONCEPTION+SCHOOL+MORRIS&btnI",
"http://www.google.com/search?q=IMMACULATE+CONCEPTION+SCHOOL+MONMOUTH&btnI",
"http://www.google.com/search?q=IMMACULATE+CONCEPTION+SCHOOL+CHICAGO&btnI",
"http://www.google.com/search?q=IMMACULATE+CONCEPTION+SCHOOL+-+EXCHANGE+CHICAGO&btnI",
"http://www.google.com/search?q=INCARNATION+ELEMENTARY+SCHOOL+PALOS HEIGHTS&btnI",
"http://www.google.com/search?q=INFANT+JESUS+OF+PRAGUE+SCHOOL+FLOSSMOOR&btnI",
"http://www.google.com/search?q=JOLIET+CATHOLIC+ACADEMY+JOLIET&btnI",
"http://www.google.com/search?q=JORDAN+CATHOLIC+SCHOOL+ROCK ISLAND&btnI",
"http://www.google.com/search?q=JOSEPHINUM+ACADEMY+CHICAGO&btnI",
"http://www.google.com/search?q=LEO+CATHOLIC+HIGH+SCHOOL+CHICAGO&btnI",
"http://www.google.com/search?q=LOYOLA+ACADEMY+WILMETTE&btnI",
"http://www.google.com/search?q=MARIAN+CATHOLIC+HIGH+SCHOOL+CHICAGO HEIGHTS&btnI",
"http://www.google.com/search?q=MARIAN+CENTRAL+CATHOLIC+HIGH+SCHOOL+WOODSTOCK&btnI",
"http://www.google.com/search?q=MARIST+HIGH+SCHOOL+CHICAGO&btnI",
"http://www.google.com/search?q=MARMION+ACADEMY+AURORA&btnI",
"http://www.google.com/search?q=MARQUETTE+ACADEMY+OTTAWA&btnI",
"http://www.google.com/search?q=MARQUETTE+CATHOLIC+HIGH+SCHOOL+ALTON&btnI",
"http://www.google.com/search?q=MARY+SEAT+OF+WISDOM+SCHOOL+PARK RIDGE&btnI",
"http://www.google.com/search?q=MATER+DEI+HIGH+SCHOOL+BREESE&btnI",
"http://www.google.com/search?q=MATERNITY+BVM+ELEMENTARY+SCHOOL+CHICAGO&btnI",
"http://www.google.com/search?q=MATERNITY+BVM+SCHOOL+BOURBONNAIS&btnI",
"http://www.google.com/search?q=MISERICORDIA+SCHOOL+CHICAGO&btnI",
"http://www.google.com/search?q=MONTINI+CATHOLIC+HIGH+SCHOOL+LOMBARD&btnI",
"http://www.google.com/search?q=MONTINI+CATHOLIC+SCHOOL+MCHENRY&btnI",
"http://www.google.com/search?q=MOST+BLESSED+TRINITY+ACADEMY+WAUKEGAN&btnI",
"http://www.google.com/search?q=MOTHER+MCAULEY+LIBERAL+ARTS+HIGH+SCHOOL+CHICAGO&btnI",
"http://www.google.com/search?q=MOTHER+TERESA+CATHOLIC+ACADEMY+CRETE&btnI",
"http://www.google.com/search?q=MOUNT+ASSISI+ACADEMY+SCHOOL+LEMONT&btnI",
"http://www.google.com/search?q=NAZARETH+ACADEMY+LA GRANGE PARK&btnI",
"http://www.google.com/search?q=NEWMAN+CENTRAL+CATHOLIC+HIGH+SCHOOL+STERLING&btnI",
"http://www.google.com/search?q=NOONAN+ELEMENTARY+ACADEMY+MOKENA&btnI",
"http://www.google.com/search?q=NORTHRIDGE+PREPARATORY+SCHOOL+NILES&btnI",
"http://www.google.com/search?q=NORTHSIDE+CATHOLIC+ACADEMY+CHICAGO&btnI",
"http://www.google.com/search?q=NOTRE+DAME+COLLEGE+PREP+NILES&btnI",
"http://www.google.com/search?q=NOTRE+DAME+SCHOOL+CLARENDON HILLS&btnI",
"http://www.google.com/search?q=OLD+ST+MARYS+SCHOOL+CHICAGO&btnI",
"http://www.google.com/search?q=OUR+LADY+IMMACULATE+ACADEMY+OAK PARK&btnI",
"http://www.google.com/search?q=OUR+LADY+OF+CHARITY+SCHOOL+CICERO&btnI",
"http://www.google.com/search?q=OUR+LADY+OF+DESTINY+SCHOOL+DES PLAINES&btnI",
"http://www.google.com/search?q=OUR+LADY+OF+GOOD+COUNSEL+SCHOOL+AURORA&btnI",
"http://www.google.com/search?q=OUR+LADY+OF+GRACE+EAST MOLINE&btnI",
"http://www.google.com/search?q=OUR+LADY+OF+GUADALUPE+SCHOOL+CHICAGO&btnI",
"http://www.google.com/search?q=OUR+LADY+OF+HUMILITY+SCHOOL+BEACH PARK&btnI",
"http://www.google.com/search?q=OUR+LADY+OF+LOURDES+SCHOOL+DECATUR&btnI",
"http://www.google.com/search?q=OUR+LADY+OF+MOUNT+CARMEL+ACADEMY+CHICAGO&btnI",
"http://www.google.com/search?q=OUR+LADY+OF+MT+CARMEL+SCHOOL+HERRIN&btnI",
"http://www.google.com/search?q=OUR+LADY+OF+PERPETUAL+HELP+GLENVIEW&btnI",
"http://www.google.com/search?q=OUR+LADY+OF+TEPAYAC+ELEMENTARY+SCHOOL+CHICAGO&btnI",
"http://www.google.com/search?q=OUR+LADY+OF+TEPEYAC+HIGH+SCHOOL+CHICAGO&btnI",
"http://www.google.com/search?q=OUR+LADY+OF+THE+RIDGE+SCHOOL+CHICAGO RIDGE&btnI",
"http://www.google.com/search?q=OUR+LADY+OF+THE+WAYSIDE+SCHOOL+ARLINGTON HEIGHTS&btnI",
"http://www.google.com/search?q=OUR+LADY+QUEEN+OF+PEACE+SCHOOL+BELLEVILLE&btnI",
"http://www.google.com/search?q=OUR+LADY+QUEEN+OF+PEACE+SCHOOL+BETHALTO&btnI",
"http://www.google.com/search?q=OUR+SAVIOUR+SCHOOL+JACKSONVILLE&btnI",
"http://www.google.com/search?q=PEORIA+NOTRE+DAME+HIGH+SCHOOL+PEORIA&btnI",
"http://www.google.com/search?q=PERU+CATHOLIC+SCHOOL+PERU&btnI",
"http://www.google.com/search?q=POPE+JOHN+PAUL+II+CATHOLIC+SCHOOL+CHICAGO&btnI",
"http://www.google.com/search?q=POPE+JOHN+XXIII+SCHOOL+EVANSTON&btnI",
"http://www.google.com/search?q=PRINCE+OF+PEACE+SCHOOL+LAKE VILLA&btnI",
"http://www.google.com/search?q=PROVIDENCE+CATHOLIC+CHILDRENS+ACADEMY+NEW LENOX&btnI",
"http://www.google.com/search?q=PROVIDENCE+CATHOLIC+HIGH+SCHOOL+NEW LENOX&btnI",
"http://www.google.com/search?q=QUEEN+OF+ALL+SAINTS+CHICAGO&btnI",
"http://www.google.com/search?q=QUEEN+OF+ANGELS+ELEMENTARY+SCHOOL+CHICAGO&btnI",
"http://www.google.com/search?q=QUEEN+OF+MARTYRS+ELEMENTARY+SCHOOL+EVERGREEN PARK&btnI",
"http://www.google.com/search?q=QUEEN+OF+PEACE+HIGH+SCHOOL+BURBANK&btnI",
"http://www.google.com/search?q=QUEEN+OF+THE+ROSARY+SCHOOL+ELK GROVE VILLAGE&btnI",
"http://www.google.com/search?q=QUEEN+OF+THE+UNIVERSE+SCHOOL+CHICAGO&btnI",
"http://www.google.com/search?q=QUINCY+NOTRE+DAME+HIGH+SCHOOL+QUINCY&btnI",
"http://www.google.com/search?q=REGINA+DOMINICAN+HIGH+SCHOOL+WILMETTE&btnI",
"http://www.google.com/search?q=RESURRECTION+COLLEGE+PREP+HIGH+SCHOOL+CHICAGO&btnI",
"http://www.google.com/search?q=ROSARY+HIGH+SCHOOL+AURORA&btnI",
"http://www.google.com/search?q=ROUTT+CATHOLIC+HIGH+SCHOOL+JACKSONVILLE&btnI",
"http://www.google.com/search?q=SACRED+HEART+ELEMENTARY+SCHOOL+EFFINGHAM&btnI",
"http://www.google.com/search?q=SACRED+HEART+GRIFFIN+HIGH+SCHOOL+SPRINGFIELD&btnI",
"http://www.google.com/search?q=SACRED+HEART+SCHOOL+WINNETKA&btnI",
"http://www.google.com/search?q=SACRED+HEART+SCHOOL+MELROSE PARK&btnI",
"http://www.google.com/search?q=SACRED+HEART+SCHOOL+LOMBARD&btnI",
"http://www.google.com/search?q=SACRED+HEART+SCHOOL+PANA&btnI",
"http://www.google.com/search?q=SACRED+HEART+SCHOOL-96TH+CHICAGO&btnI",
"http://www.google.com/search?q=SACRED+HEART+SCHOOLS+CHICAGO&btnI",
"http://www.google.com/search?q=SAINTS+PETER+&+PAUL+SCHOOL+NAPERVILLE&btnI",
"http://www.google.com/search?q=SAN+MIGUEL-BACK+OF+THE+YARDS+CHICAGO&btnI",
"http://www.google.com/search?q=SANDBOX+PRESCHOOL+&+CHILD+CARE+HOMER GLEN&btnI",
"http://www.google.com/search?q=SANTA+LUCIA+SCHOOL+CHICAGO&btnI",
"http://www.google.com/search?q=SANTA+MARIA+DEL+POPOLO+SCHOOL+MUNDELEIN&btnI",
"http://www.google.com/search?q=SCHLARMAN+ACADEMY+DANVILLE&btnI",
"http://www.google.com/search?q=SCHOOL+OF+ST+MARY+LAKE FOREST&btnI",
"http://www.google.com/search?q=SETON+ACADEMY+SOUTH HOLLAND&btnI",
"http://www.google.com/search?q=SETON+ACADEMY+VILLA PARK&btnI",
"http://www.google.com/search?q=SETON+CATHOLIC+SCHOOL+MOLINE&btnI",
"http://www.google.com/search?q=SS+CYRIL+&+METHODIUS+SCHOOL+LEMONT&btnI",
"http://www.google.com/search?q=SS+FAITH+HOPE+CHARITY+SCHOOL+WINNETKA&btnI",
"http://www.google.com/search?q=SS+PETER+&+PAUL+ELEMENTARY+SCHOOL+ALTON&btnI",
"http://www.google.com/search?q=SS+PETER+&+PAUL+SCHOOL+COLLINSVILLE&btnI",
"http://www.google.com/search?q=SS+PETER+&+PAUL+SCHOOL+CARY&btnI",
"http://www.google.com/search?q=ST+AGATHA+CATHOLIC+ACADEMY+CHICAGO&btnI",
"http://www.google.com/search?q=ST+AGATHA+ELEMENTARY+SCHOOL+NEW ATHENS&btnI",
"http://www.google.com/search?q=ST+AGNES+ELEMENTARY+SCHOOL+SPRINGFIELD&btnI",
"http://www.google.com/search?q=ST+AGNES+OF+BOHEMIA+SCHOOL+CHICAGO&btnI",
"http://www.google.com/search?q=ST+AGNES+SCHOOL+CHICAGO HEIGHTS&btnI",
"http://www.google.com/search?q=ST+AILBE+CATHOLIC+SCHOOL+CHICAGO&btnI",
"http://www.google.com/search?q=ST+ALBERT+THE+GREAT+SCHOOL+BURBANK&btnI",
"http://www.google.com/search?q=ST+ALEXANDER+SCHOOL+VILLA PARK&btnI",
"http://www.google.com/search?q=ST+ALEXANDER+SCHOOL+PALOS HEIGHTS&btnI",
"http://www.google.com/search?q=ST+ALOYSIUS+ELEMENTARY+SCHOOL+SPRINGFIELD&btnI",
"http://www.google.com/search?q=ST+ALPHONSUS+LIGUORI+SCHOOL+PROSPECT HEIGHTS&btnI",
"http://www.google.com/search?q=ST+ALPHONSUS/ST+PATRICK+SCHOOL+LEMONT&btnI",
"http://www.google.com/search?q=ST+AMBROSE+CATHOLIC+SCHOOL+GODFREY&btnI",
"http://www.google.com/search?q=ST+ANASTASIA+SCHOOL+WAUKEGAN&btnI",
"http://www.google.com/search?q=ST+ANDREW+CATHOLIC+SCHOOL+ROCK FALLS&btnI",
"http://www.google.com/search?q=ST+ANDREW+CATHOLIC+SCHOOL+MURPHYSBORO&btnI",
"http://www.google.com/search?q=ST+ANDREW+SCHOOL+CHICAGO&btnI",
"http://www.google.com/search?q=ST+ANDREW+THE+APOSTLE+ROMEOVILLE&btnI",
"http://www.google.com/search?q=ST+ANGELA+ELEMENTARY+SCHOOL+CHICAGO&btnI",
"http://www.google.com/search?q=ST+ANN+ELEMENTARY+SCHOOL+CHICAGO&btnI",
"http://www.google.com/search?q=ST+ANN+ELEMENTARY+SCHOOL+LANSING&btnI",
"http://www.google.com/search?q=ST+ANN+SCHOOL+NASHVILLE&btnI",
"http://www.google.com/search?q=ST+ANNE+ELEMENTARY+SCHOOL+DIXON&btnI",
"http://www.google.com/search?q=ST+ANNE+PARISH+SCHOOL+BARRINGTON&btnI",
"http://www.google.com/search?q=ST+ANNE'S+CHURCH+HAZEL CREST&btnI",
"http://www.google.com/search?q=ST+ANTHONY+GRADE+SCHOOL+EFFINGHAM&btnI",
"http://www.google.com/search?q=ST+ANTHONY+HIGH+SCHOOL+EFFINGHAM&btnI",
"http://www.google.com/search?q=ST+ATHANASIUS+ELEMENTARY+SCHOOL+EVANSTON&btnI",
"http://www.google.com/search?q=ST+BARBARA+ELEMENTARY+SCHOOL+CHICAGO&btnI",
"http://www.google.com/search?q=ST+BARBARA+SCHOOL+CHICAGO&btnI",
"http://www.google.com/search?q=ST+BARNABAS+ELEMENTARY+SCHOOL+CHICAGO&btnI",
"http://www.google.com/search?q=ST+BARTHOLOMEW+SCHOOL+CHICAGO&btnI",
"http://www.google.com/search?q=ST+BEDE+ACADEMY+PERU&btnI",
"http://www.google.com/search?q=ST+BEDE+ELEMENTARY+SCHOOL+INGLESIDE&btnI",
"http://www.google.com/search?q=ST+BEDE+THE+VENERABLE+CHICAGO&btnI",
"http://www.google.com/search?q=ST+BENEDICT+ELEMENTARY+SCHOOL+CHICAGO&btnI",
"http://www.google.com/search?q=ST+BENEDICT+PREPARATORY+SCHOOL+CHICAGO&btnI",
"http://www.google.com/search?q=ST+BERNADETTE+CATHOLIC+SCHOOL+ROCKFORD&btnI",
"http://www.google.com/search?q=ST+BLASE+POLISH+CATHOLIC+SCHOOL+SUMMIT ARGO&btnI",
"http://www.google.com/search?q=ST+BRIDGET+SCHOOL+LOVES PARK&btnI",
"http://www.google.com/search?q=ST+BRUNO+CATHOLIC+SCHOOL+PINCKNEYVILLE&btnI",
"http://www.google.com/search?q=ST+BRUNO+ELEMENTARY+SCHOOL+CHICAGO&btnI",
"http://www.google.com/search?q=ST+CATHERINE+OF+ALEXANDRIA+SCHOOL+OAK LAWN&btnI",
"http://www.google.com/search?q=ST+CATHERINE+OF+SIENA+ELEMENTARY+SCHOOL+WEST DUNDEE&btnI",
"http://www.google.com/search?q=ST+CATHERINE+SIENA-ST+LUCY+SCHOOL+OAK PARK&btnI",
"http://www.google.com/search?q=ST+CHARLES+BORROMEO+CATHOLIC+SCHOOL+HAMPSHIRE&btnI",
"http://www.google.com/search?q=ST+CHRISTINA+SCHOOL+CHICAGO&btnI",
"http://www.google.com/search?q=ST+CHRISTOPHER+SCHOOL+MIDLOTHIAN&btnI",
"http://www.google.com/search?q=ST+CLARE+CATHOLIC+SCHOOL+O FALLON&btnI",
"http://www.google.com/search?q=ST+CLEMENT+SCHOOL+CHICAGO&btnI",
"http://www.google.com/search?q=ST+CLETUS+ELEMENTARY+SCHOOL+LA GRANGE&btnI",
"http://www.google.com/search?q=ST+COLETTA'S+OF+ILLINOIS+TINLEY PARK&btnI",
"http://www.google.com/search?q=ST+COLETTE+SCHOOL+ROLLING MEADOWS&btnI",
"http://www.google.com/search?q=ST+COLUMBANUS+SCHOOL+CHICAGO&btnI",
"http://www.google.com/search?q=ST+CONSTANCE+SCHOOL+CHICAGO&btnI",
"http://www.google.com/search?q=ST+CORNELIUS+ELEMENTARY+SCHOOL+CHICAGO&btnI",
"http://www.google.com/search?q=ST+CYPRIAN+ELEMENTARY+SCHOOL+RIVER GROVE&btnI",
"http://www.google.com/search?q=ST+DAMIAN+SCHOOL+OAK FOREST&btnI",
"http://www.google.com/search?q=ST+DANIEL+THE+PROPHET+SCHOOL+CHICAGO&btnI",
"http://www.google.com/search?q=ST+DENNIS+SCHOOL+LOCKPORT&btnI",
"http://www.google.com/search?q=ST+DOMINIC+ELEMENTARY+SCHOOL+BOLINGBROOK&btnI",
"http://www.google.com/search?q=ST+DOMINIC+ELEMENTARY+SCHOOL+QUINCY&btnI",
"http://www.google.com/search?q=ST+DOROTHY+ELEMENTARY+SCHOOL+CHICAGO&btnI",
"http://www.google.com/search?q=ST+EDMUND+PARISH+SCHOOL+OAK PARK&btnI",
"http://www.google.com/search?q=ST+EDWARD+CENTRAL+CATHOLIC+HIGH+SCHOOL+ELGIN&btnI",
"http://www.google.com/search?q=ST+EDWARD+SCHOOL+ROCKFORD&btnI",
"http://www.google.com/search?q=ST+EDWARD+SCHOOL+CHILLICOTHE&btnI",
"http://www.google.com/search?q=ST+EDWARD+SCHOOL+CHICAGO&btnI",
"http://www.google.com/search?q=ST+ELIZABETH+CATHOLIC+SCHOOL+CHICAGO&btnI",
"http://www.google.com/search?q=ST+EMILY+ELEMENTARY+SCHOOL+MOUNT PROSPECT&btnI",
"http://www.google.com/search?q=ST+ETHELREDA+ELEMENTARY+SCHOOL+CHICAGO&btnI",
"http://www.google.com/search?q=ST+EUGENE+ELEMENTARY+SCHOOL+CHICAGO&btnI",
"http://www.google.com/search?q=ST+FLORIAN+SCHOOL+CHICAGO&btnI",
"http://www.google.com/search?q=ST+FRANCES+OF+ROME+SCHOOL+CICERO&btnI",
"http://www.google.com/search?q=ST+FRANCIS+BORGIA+SCHOOL+CHICAGO&btnI",
"http://www.google.com/search?q=ST+FRANCIS+DE+SALES+HIGH+SCHOOL+CHICAGO&btnI",
"http://www.google.com/search?q=ST+FRANCIS+DE+SALES+SCHOOL+LAKE ZURICH&btnI",
"http://www.google.com/search?q=ST+FRANCIS+HIGH+SCHOOL+WHEATON&btnI",
"http://www.google.com/search?q=ST+FRANCIS+XAVIER+SCHOOL+WILMETTE&btnI",
"http://www.google.com/search?q=ST+FRANCIS/HOLY+GHOST+CATHOLIC+SCHOOL+JERSEYVILLE&btnI",
"http://www.google.com/search?q=ST+GABRIEL+ELEMENTARY+SCHOOL+CHICAGO&btnI",
"http://www.google.com/search?q=ST+GALL+ELEMENTARY+SCHOOL+CHICAGO&btnI",
"http://www.google.com/search?q=ST+GENEVIEVE+SCHOOL+CHICAGO&btnI",
"http://www.google.com/search?q=ST+GEORGE+SCHOOL+TINLEY PARK&btnI",
"http://www.google.com/search?q=ST+GERALD+SCHOOL+OAK LAWN&btnI",
"http://www.google.com/search?q=ST+GERMAINE+SCHOOL+OAK LAWN&btnI",
"http://www.google.com/search?q=ST+GILBERT+ELEMENTARY+SCHOOL+GRAYSLAKE&btnI",
"http://www.google.com/search?q=ST+GILES+RELIGIOUS+EDUCATION+OAK PARK&btnI",
"http://www.google.com/search?q=ST+GILES+SCHOOL+OAK PARK&btnI",
"http://www.google.com/search?q=ST+HELEN+SCHOOL+CHICAGO&btnI",
"http://www.google.com/search?q=ST+HILARY+SCHOOL+CHICAGO&btnI",
"http://www.google.com/search?q=ST+HUBERT+SCHOOL+HOFFMAN ESTATES&btnI",
"http://www.google.com/search?q=ST+HYACINTH+BASILICA+SCHOOL+CHICAGO&btnI",
"http://www.google.com/search?q=ST+IGNATIUS+COLLEGE+PREP+CHICAGO&btnI",
"http://www.google.com/search?q=ST+IRENE+CATHOLIC+SCHOOL+WARRENVILLE&btnI",
"http://www.google.com/search?q=ST+ISAAC+JOGUES+ELEMENTARY+SCHOOL+HINSDALE&btnI",
"http://www.google.com/search?q=ST+JAMES+CATHOLIC+SCHOOL+ROCKFORD&btnI",
"http://www.google.com/search?q=ST+JAMES+CATHOLIC+SCHOOL+MILLSTADT&btnI",
"http://www.google.com/search?q=ST+JAMES+SCHOOL+BELVIDERE&btnI",
"http://www.google.com/search?q=ST+JAMES+SCHOOL+ARLINGTON HEIGHTS&btnI",
"http://www.google.com/search?q=ST+JAMES+SCHOOL+HIGHWOOD&btnI",
"http://www.google.com/search?q=ST+JAMES+THE+APOSTLE+SCHOOL+GLEN ELLYN&btnI",
"http://www.google.com/search?q=ST+JANE+DE+CHANTAL+SCHOOL+CHICAGO&btnI",
"http://www.google.com/search?q=ST+JEROME+SCHOOL+CHICAGO&btnI",
"http://www.google.com/search?q=ST+JOAN+OF+ARC+LISLE&btnI",
"http://www.google.com/search?q=ST+JOHN+BERCHMANS+SCHOOL+CHICAGO&btnI",
"http://www.google.com/search?q=ST+JOHN+BREBEUF+SCHOOL+NILES&btnI",
"http://www.google.com/search?q=ST+JOHN+DE+LA+SALLE+CATHOLIC+ACADEMY+CHICAGO&btnI",
"http://www.google.com/search?q=ST+JOHN+FISHER+ELEMENTARY+SCHOOL+CHICAGO&btnI",
"http://www.google.com/search?q=ST+JOHN+OF+THE+CROSS+PARISH+SCHOOL+WESTERN SPRINGS&btnI",
"http://www.google.com/search?q=ST+JOHN+THE+BAPTIST+CATHOLIC+ELEMENTARY+SCHOOL+WEST FRANKFORT&btnI",
"http://www.google.com/search?q=ST+JOHN+THE+BAPTIST+CATHOLIC+SCHOOL+RED BUD&btnI",
"http://www.google.com/search?q=ST+JOHN+THE+BAPTIST+SCHOOL+SMITHTON&btnI",
"http://www.google.com/search?q=ST+JOHN+THE+EVANGELIST+SCHOOL+STREAMWOOD&btnI",
"http://www.google.com/search?q=ST+JOHN+THE+EVANGELIST+SCHOOL+CARROLLTON&btnI",
"http://www.google.com/search?q=ST+JOHN+VIANNEY+SCHOOL+NORTHLAKE&btnI",
"http://www.google.com/search?q=ST+JOSAPHAT+SCHOOL+CHICAGO&btnI",
"http://www.google.com/search?q=ST+JOSEPH+ACADEMY+JOLIET&btnI",
"http://www.google.com/search?q=ST+JOSEPH+CATHOLIC+ELEMENTARY+SCHOOL+MANHATTAN&btnI",
"http://www.google.com/search?q=ST+JOSEPH+CATHOLIC+SCHOOL+ELGIN&btnI",
"http://www.google.com/search?q=ST+JOSEPH+CATHOLIC+SCHOOL+AURORA&btnI",
"http://www.google.com/search?q=ST+JOSEPH+CATHOLIC+SCHOOL+LIBERTYVILLE&btnI",
"http://www.google.com/search?q=ST+JOSEPH+ELEMENTARY+SCHOOL+SUMMIT&btnI",
"http://www.google.com/search?q=ST+JOSEPH+ELEMENTARY+SCHOOL+ROUND LAKE&btnI",
"http://www.google.com/search?q=ST+JOSEPH+ELEMENTARY+SCHOOL+PEKIN&btnI",
"http://www.google.com/search?q=ST+JOSEPH+ELEMENTARY+SCHOOL+OLNEY&btnI",
"http://www.google.com/search?q=ST+JOSEPH+ELEMENTARY+SCHOOL+LOCKPORT&btnI",
"http://www.google.com/search?q=ST+JOSEPH+SCHOOL+DOWNERS GROVE&btnI",
"http://www.google.com/search?q=ST+JOSEPH+SCHOOL+FREEBURG&btnI",
"http://www.google.com/search?q=ST+JOSEPH+SCHOOL+BRADLEY&btnI",
"http://www.google.com/search?q=ST+JOSEPH+SCHOOL+HOMEWOOD&btnI",
"http://www.google.com/search?q=ST+JOSEPH+SCHOOL+WILMETTE&btnI",
"http://www.google.com/search?q=ST+JOSEPHS+SCHOOL+HARVARD&btnI",
"http://www.google.com/search?q=ST+JUDE+CATHOLIC+SCHOOL+PEORIA&btnI",
"http://www.google.com/search?q=ST+JUDE+SCHOOL+JOLIET&btnI",
"http://www.google.com/search?q=ST+JUDE+SCHOOL+NEW LENOX&btnI",
"http://www.google.com/search?q=ST+JULIANA+SCHOOL+CHICAGO&btnI",
"http://www.google.com/search?q=ST+LADISLAUS+SCHOOL+CHICAGO&btnI",
"http://www.google.com/search?q=ST+LAURENCE+ELEMENTARY+SCHOOL+ELGIN&btnI",
"http://www.google.com/search?q=ST+LAURENCE+HIGH+SCHOOL+BURBANK&btnI",
"http://www.google.com/search?q=ST+LAWRENCE+O+TOOLE+SCHOOL+MATTESON&btnI",
"http://www.google.com/search?q=ST+LEONARD+SCHOOL+BERWYN&btnI",
"http://www.google.com/search?q=ST+LINUS+ELEMENTARY+SCHOOL+OAK LAWN&btnI",
"http://www.google.com/search?q=ST+LOUIS+CATHOLIC+SCHOOL+NOKOMIS&btnI",
"http://www.google.com/search?q=ST+LOUIS+SCHOOL+PRINCETON&btnI",
"http://www.google.com/search?q=ST+LUKE+PARISH+SCHOOL+RIVER FOREST&btnI",
"http://www.google.com/search?q=ST+MALACHY+GENESEO&btnI",
"http://www.google.com/search?q=ST+MALACHY+ELEMENTARY+SCHOOL+CHICAGO&btnI",
"http://www.google.com/search?q=ST+MALACHY+SCHOOL+RANTOUL&btnI",
"http://www.google.com/search?q=ST+MARGARET+MARY+CATHOLIC+SCHOOL+ALGONQUIN&btnI",
"http://www.google.com/search?q=ST+MARGARET+MARY+ELEMENTARY+SCHOOL+CHICAGO&btnI",
"http://www.google.com/search?q=ST+MARIA+GORETTI+SCHILLER PARK&btnI",
"http://www.google.com/search?q=ST+MARK+SCHOOL+PEORIA&btnI",
"http://www.google.com/search?q=ST+MARY+CATHOLIC+SCHOOL+PARIS&btnI",
"http://www.google.com/search?q=ST+MARY+CATHOLIC+SCHOOL+WOODSTOCK&btnI",
"http://www.google.com/search?q=ST+MARY+CATHOLIC+SCHOOL+MOUNT CARMEL&btnI",
"http://www.google.com/search?q=ST+MARY+ELEMENTARY+&+JR+HIGH+SCHOOL+DIXON&btnI",
"http://www.google.com/search?q=ST+MARY+ELEMENTARY+SCHOOL+EAST DUBUQUE&btnI",
"http://www.google.com/search?q=ST+MARY+ELEMENTARY+SCHOOL+BRUSSELS&btnI",
"http://www.google.com/search?q=ST+MARY+ELEMENTARY+SCHOOL+MOUNT STERLING&btnI",
"http://www.google.com/search?q=ST+MARY+ELEMENTARY+SCHOOL+MOKENA&btnI",
"http://www.google.com/search?q=ST+MARY+IMMACULATE+PARISH+SCHOOL+PLAINFIELD&btnI",
"http://www.google.com/search?q=ST+MARY+NATIVITY+SCHOOL+JOLIET&btnI",
"http://www.google.com/search?q=ST+MARY+OF+THE+ANGELS+SCHOOL+CHICAGO&btnI",
"http://www.google.com/search?q=ST+MARY+OF+THE+ANNUNCIATION+SCHOOL+MUNDELEIN&btnI",
"http://www.google.com/search?q=ST+MARY+OF+THE+WOODS+SCHOOL+CHICAGO&btnI",
"http://www.google.com/search?q=ST+MARY+SCHOOL+PLANO&btnI",
"http://www.google.com/search?q=ST+MARY+SCHOOL+BUFFALO GROVE&btnI",
"http://www.google.com/search?q=ST+MARY+SCHOOL+STERLING&btnI",
"http://www.google.com/search?q=ST+MARY+SCHOOL+CENTRALIA&btnI",
"http://www.google.com/search?q=ST+MARY+SCHOOL+MATTOON&btnI",
"http://www.google.com/search?q=ST+MARY+SCHOOL+ALTON&btnI",
"http://www.google.com/search?q=ST+MARY+SCHOOL+TAYLORVILLE&btnI",
"http://www.google.com/search?q=ST+MARY+SCHOOL+DEKALB&btnI",
"http://www.google.com/search?q=ST+MARY+SCHOOL+ELGIN&btnI",
"http://www.google.com/search?q=ST+MARY+ST+AUGUSTINE+SCHOOL+BELLEVILLE&btnI",
"http://www.google.com/search?q=ST+MARY+STAR+OF+THE+SEA+SCHOOL+CHICAGO&btnI",
"http://www.google.com/search?q=ST+MARY'S+CATHOLIC+SCHOOL+SYCAMORE&btnI",
"http://www.google.com/search?q=ST+MARYS+OF+KICKAPOO+EDWARDS&btnI",
"http://www.google.com/search?q=ST+MARYS+SCHOOL+EDWARDSVILLE&btnI",
"http://www.google.com/search?q=ST+MARYS+SCHOOL+BLOOMINGTON&btnI",
"http://www.google.com/search?q=ST+MARYS+SCHOOL+PONTIAC&btnI",
"http://www.google.com/search?q=ST+MARYS+SCHOOL+CHESTER&btnI",
"http://www.google.com/search?q=ST+MATTHEW+SCHOOL+GLENDALE HEIGHTS&btnI",
"http://www.google.com/search?q=ST+MATTHEW+SCHOOL+CHAMPAIGN&btnI",
"http://www.google.com/search?q=ST+MATTHIAS+SCHOOL+CHICAGO&btnI",
"http://www.google.com/search?q=ST+MICHAEL+CATHOLIC+SCHOOL+WHEATON&btnI",
"http://www.google.com/search?q=ST+MICHAEL+SCHOOL+STAUNTON&btnI",
"http://www.google.com/search?q=ST+MICHAEL+SCHOOL+ORLAND PARK&btnI",
"http://www.google.com/search?q=ST+MICHAEL+THE+ARCHANGEL+CATHOLIC+SCHOOL+STREATOR&btnI",
"http://www.google.com/search?q=ST+MICHAEL+THE+ARCHANGEL+SCHOOL+CHICAGO&btnI",
"http://www.google.com/search?q=ST+MICHAEL+THE+ARCHANGEL+SCHOOL+SIGEL&btnI",
"http://www.google.com/search?q=ST+MONICA+ACADEMY+CHICAGO&btnI",
"http://www.google.com/search?q=ST+NORBERT+SCHOOL+NORTHBROOK&btnI",
"http://www.google.com/search?q=ST+NORBERT+SCHOOL+HARDIN&btnI",
"http://www.google.com/search?q=ST+ODILO+ELEMENTARY+SCHOOL+BERWYN&btnI",
"http://www.google.com/search?q=ST+PATRICK+CATHOLIC+SCHOOL+SPRINGFIELD&btnI",
"http://www.google.com/search?q=ST+PATRICK+HIGH+SCHOOL+CHICAGO&btnI",
"http://www.google.com/search?q=ST+PATRICK+SCHOOL+WADSWORTH&btnI",
"http://www.google.com/search?q=ST+PATRICK+SCHOOL+WASHINGTON&btnI",
"http://www.google.com/search?q=ST+PATRICK+SCHOOL+DECATUR&btnI",
"http://www.google.com/search?q=ST+PATRICK+SCHOOL+SAINT CHARLES&btnI",
"http://www.google.com/search?q=ST+PATRICK'S+CATHOLIC+SCHOOL+SAINT CHARLES&btnI",
"http://www.google.com/search?q=ST+PAUL+CATHOLIC+SCHOOL+HIGHLAND&btnI",
"http://www.google.com/search?q=ST+PAUL+ELEMENTARY+SCHOOL+MACOMB&btnI",
"http://www.google.com/search?q=ST+PAUL+OF+THE+CROSS+SCHOOL+PARK RIDGE&btnI",
"http://www.google.com/search?q=ST+PAUL+SCHOOL+ODELL&btnI",
"http://www.google.com/search?q=ST+PAUL+THE+APOSTLE+SCHOOL+JOLIET&btnI",
"http://www.google.com/search?q=ST+PETER+CATHEDRAL+ROCKFORD&btnI",
"http://www.google.com/search?q=ST+PETER+CATHOLIC+SCHOOL+SOUTH BELOIT&btnI",
"http://www.google.com/search?q=ST+PETER+SCHOOL+AURORA&btnI",
"http://www.google.com/search?q=ST+PETER+SCHOOL+QUINCY&btnI",
"http://www.google.com/search?q=ST+PETRONILLE+SCHOOL+GLEN ELLYN&btnI",
"http://www.google.com/search?q=ST+PHILIP+NERI+ELEMENTARY+SCHOOL+CHICAGO&btnI",
"http://www.google.com/search?q=ST+PHILIP+THE+APOSTLE+SCHOOL+ADDISON&btnI",
"http://www.google.com/search?q=ST+PHILOMENA+SCHOOL+PEORIA&btnI",
"http://www.google.com/search?q=ST+PIUS+V+SCHOOL+CHICAGO&btnI",
"http://www.google.com/search?q=ST+PIUS+X+ELEMENTARY+SCHOOL+LOMBARD&btnI",
"http://www.google.com/search?q=ST+RAPHAEL+CATHOLIC+SCHOOL+NAPERVILLE&btnI",
"http://www.google.com/search?q=ST+RAYMOND+SCHOOL+MOUNT PROSPECT&btnI",
"http://www.google.com/search?q=ST+RENE+GOUPIL+ELEMENTARY+SCHOOL+CHICAGO&btnI",
"http://www.google.com/search?q=ST+RICHARD+ELEMENTARY+SCHOOL+CHICAGO&btnI",
"http://www.google.com/search?q=ST+RITA+OF+CASCIA+SCHOOL+AURORA&btnI",
"http://www.google.com/search?q=ST+RITA+SCHOOL+ROCKFORD&btnI",
"http://www.google.com/search?q=ST+ROBERT+BELLARMINE+SCHOOL+CHICAGO&btnI",
"http://www.google.com/search?q=ST+ROSE+SCHOOL+WILMINGTON&btnI",
"http://www.google.com/search?q=ST+SCHOLASTICA+ELEMENTARY+SCHOOL+WOODRIDGE&btnI",
"http://www.google.com/search?q=ST+STANISLAUS+KOSTKA+SCHOOL+CHICAGO&btnI",
"http://www.google.com/search?q=ST+SYLVESTER+ELEMENTARY+SCHOOL+CHICAGO&btnI",
"http://www.google.com/search?q=ST+TERESA+CATHOLIC+SCHOOL+BELLEVILLE&btnI",
"http://www.google.com/search?q=ST+THECLA+ELEMENTARY+SCHOOL+CHICAGO&btnI",
"http://www.google.com/search?q=ST+THERESA+OF+AVILA+SALEM&btnI",
"http://www.google.com/search?q=ST+THERESE+OF+JESUS+SCHOOL+AURORA&btnI",
"http://www.google.com/search?q=ST+THERESE+SCHOOL+CHICAGO&btnI",
"http://www.google.com/search?q=ST+THOMAS+CATHOLIC+ELEMENTARY+SCHOOL+PHILO&btnI",
"http://www.google.com/search?q=ST+THOMAS+ELEMENTARY+SCHOOL+PEORIA HEIGHTS&btnI",
"http://www.google.com/search?q=ST+THOMAS+MORE+ELEMENTARY+SCHOOL+ELGIN&btnI",
"http://www.google.com/search?q=ST+THOMAS+OF+VILLANOVA+SCHOOL+PALATINE&btnI",
"http://www.google.com/search?q=ST+THOMAS+THE+APOSTLE+CHICAGO&btnI",
"http://www.google.com/search?q=ST+THOMAS+THE+APOSTLE+ELEMENTARY+SCHOOL+NEWTON&btnI",
"http://www.google.com/search?q=ST+THOMAS+THE+APOSTLE+SCHOOL+CRYSTAL LAKE&btnI",
"http://www.google.com/search?q=ST+TURIBIUS+SCHOOL+CHICAGO&btnI",
"http://www.google.com/search?q=ST+VIATOR+ELEMENTARY+SCHOOL+CHICAGO&btnI",
"http://www.google.com/search?q=ST+VIATOR+HIGH+SCHOOL+ARLINGTON HEIGHTS&btnI",
"http://www.google.com/search?q=ST+VINCENT+DE+PAUL+PEORIA&btnI",
"http://www.google.com/search?q=ST+VINCENT+FERRER+ELEMENTARY+SCHOOL+RIVER FOREST&btnI",
"http://www.google.com/search?q=ST+WALTER+SCHOOL+ROSELLE&btnI",
"http://www.google.com/search?q=ST+WALTER+SCHOOL+CHICAGO&btnI",
"http://www.google.com/search?q=ST+WILLIAM+SCHOOL+CHICAGO&btnI",
"http://www.google.com/search?q=ST+ZACHARY+ELEMENTARY+SCHOOL+DES PLAINES&btnI",
"http://www.google.com/search?q=STS+PETER+&+PAUL+NAUVOO&btnI",
"http://www.google.com/search?q=STS+PETER+&+PAUL+SCHOOL+WATERLOO&btnI",
"http://www.google.com/search?q=THE+HIGH+SCHOOL+OF+ST+THOMAS+MORE+CHAMPAIGN&btnI",
"http://www.google.com/search?q=THE+WILLOWS+ACADEMY+DES PLAINES&btnI",
"http://www.google.com/search?q=TRANSFIGURATION+SCHOOL+WAUCONDA&btnI",
"http://www.google.com/search?q=TRINITY+CATHOLIC+ACADEMY+LA SALLE&btnI",
"http://www.google.com/search?q=VILASECA+JOSEPHINE+CENTER+JOLIET&btnI",
"http://www.google.com/search?q=VISITATION+CATHOLIC+SCHOOL+KEWANEE&btnI",
"http://www.google.com/search?q=VISITATION+CATHOLIC+SCHOOL+CHICAGO&btnI",
"http://www.google.com/search?q=VISITATION+SCHOOL+ELMHURST&btnI",
"http://www.google.com/search?q=WOODLANDS+ACADEMY+OF+THE+SACRED+HEART+LAKE FOREST&btnI"]
for s in schools:
	#print s	
	var = requests.get(s)
	#print var.url
	writer.writerow([var.url])