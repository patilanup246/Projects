import sqlite3

conn = sqlite3.connect('Jim.db')
names = ['Zy-Cheng-phone','Ziqi-Gui-phone','Zille-Hasnain-phone','Zellipah-Githui-phone','Zak-Robinson-phone','Young-G-S.-phone','Wyatt-Jones-phone','Wolfgang-Schmidt-phone','Wody-Edji-phone','Willie-Crowder-phone','William-Walls-phone','William-Waas-phone','William-Vogelgesang-phone','William-Ross-phone','William-Earp-phone','Westly-Verner-phone','Wayne-Jensen-phone','Warren-Schatz-phone','Warren-Hinds-phone','Walt-Niziolek-phone','Vinay-Kumar-phone','Vijai-Rahul-V-phone','Victoria-Fowler-phone','Veronica-Donner-phone','Vernon-Smith-phone','Veasna-Mao-phone','Varun-Garg-phone','Varghese-(Vic)-Geevarghese-phone','Vandana-Setty-phone','Vance-Crowe-phone','Van-Meador-phone','Ursula-Edwards-phone','Ulysses-"Uly"-Labilles,DMD,PhD.PH(c)-phone','Tyler-Stearns-phone','Tyler-Craig-phone','Twinkle-VanFleet-phone','Trudie-Pleiss-phone','Troy-Gonzales-phone','Travis-Jewell-phone','Tony-Morris-phone','Tony-Chirico-phone','Tony-Calabrese-phone','Tom-Walton-phone','Tom-Smith-phone','Tom-Kelly-phone','Todd-Slininger-phone','Todd-Shail-phone','Todd-Kammerer-phone','Todd-Cordell-phone','Tino-Rodriguez-phone','Timothy-Fullerton-phone','Tim-Ross-phone','Tim-Gellerson-phone','Tim-Baumgartner-phone','Tiffany-Lee-phone','Thomas-Woelfel-phone','Thomas-Veltri-phone','Thomas-Pawlowski-phone','Thomas-Niehaus-phone','Thomas-Lewicki-phone','Thomas-Lee-phone','Thomas-Joseph-phone','Thomas-Britton-phone','Thom-Hoge-phone','Thom-Hansen-phone','Theresa-Rufus-phone','Theresa-A.-Rowland-phone','Terry-Murphy-phone','Terry-McKenzie-phone','Terry-Cornell-phone','Terry-Cornell-phone','Terry-Bilas-phone','Teresa-Kelley-phone','Ted-Stilgenbauer-phone','Ted-Sivalon-phone','Tayo-Adesanya-phone','Taylor-A-Reynolds-phone','Tarrah-Ledoux-phone','Tamara-Croes-phone','Tahir-Amin-phone','Sylvia-Dunn-phone','Syed-Haider-phone','Syed-Asadullah-phone','Susan-Schumacher-phone','Stuart-Maples-phone','Stuart-Karas-phone','Steven-Stefanik-phone','Steven-Moss-phone','Steven-Morgan-phone','Steve-Norton-phone','Steve-Lallensack-phone','Steve-Julson-phone','Steve-Hsia-phone','Steve-Haynal-phone','Steve-Hawthorne-phone','Steve-Hanna-phone','Sterling-Stokes-phone','Stephen-Taylor-phone','Stephen-Miller-phone','Stephen-Karr-phone','Stephen-Karlsgodt-phone','Stephanie-Milk-phone','Stanton-Knight-phone','Stan-Foster-phone','Sri-Purisai-phone','Silvia-Gao-phone','Shooter-Loch-phone','Shay-Benchorin-phone','Shawn-Mowlai-phone','Shashank-Rajagopalan-phone','Sharletta-Evans-phone','Shari-Blaz-phone','Shanki-P.-phone','Shankar-Pal-phone','Shanie-Matthews-phone','Shane-Hill-phone','Sean-Smith-phone','Sean-Paul-Hopkins-phone','Sean-LeCave-phone','Sean-Kilgus-phone','Sean-Griswold-phone','Sean-Crowley-phone','Scott-Teson-phone','scott-miller-phone','Scott-Mertens-phone','Scott-Law-phone','Scott-Karlo-phone','Scott-Goldman-phone','Scott-B.-phone','Scott-B.-phone','Scot-Bernstein-phone','Saurabh-Ghei-phone','Sarah-Dearbonne-phone','Santi-Condorelli-phone','Sandra-Ficke-Bradford-phone','Sander-Arts-phone','Sal-Scott-phone','Ryan-Morris-phone','Rusty-Sattar-phone','Russell-Golemba-phone','Russell-Golemba-phone','Russ-Argadine-phone','Roy-Ingold-phone','Roy-Ilagan-phone','Roy-Carew-phone','Ronnell-Shaw-phone','Romel-Rodriguez,-MBA-phone','Rohit-Gaur-phone','Rod-Stallings-phone','Rocky-Lee-phone','Robert-Werner-phone','Robert-Ware-phone','Robert-Johnstun-phone','Robert-Jaegly-phone','Robert-Harrison-phone','Robert-Ertel-phone','Robert-DePalma-phone','Robert-Campbell-phone','Robert-Brassell,-Jr.,-N.Y.S.N.P.-phone','Robert-Bisaillon-phone','Robert-Bilger-phone','Robb-Fujioka-phone','Rob-Kratzer-phone','Rob-Anderson-phone','Rick-Rodarte-phone','Rick-Kinder-phone','Rick-Hartman-phone','Rick-Elias-phone','RICK-ELIAS-phone','Rick-Beal-phone','Richard-Shine-phone','Richard-Matthews-phone','Richard-Hays-phone','Richard-Balano-phone','Richard-(Rick)-Heede-phone','Rich-Randall-phone','Ricardo-Sebastian-phone','Reza-Dabir-phone','Rebecca-Richeson-phone','Ray-Hughes-phone','Raul-Irizarry-phone','Randy-Uhl-phone','Randy-Smith-phone','Randy-Murray-phone','Randy-Guillem-phone','Ramona-Beverley-Courtney-phone','Ralph-Pena-phone','Rajshree-Chauhan-(Raja)-phone','Raj-Penn-phone','Rahim-Bagheri-phone','Rafe-McBride-phone','Rafael-Saavedra-phone','Rafael-Mendez-phone','Quentin-Hall-phone','Puja-Gupta-phone','Phillip-Carbaugh-phone','Phil-Taylor-phone','Phil-Goatley-phone','Phil-Farrar-phone','Peter-Lynch-phone','Peter-E.-Murphy-phone','Pete-Lassen-phone','Paul-Sura-phone','Paul-Rignel-phone','Paul-Liss-phone','Paul-Gaeta-phone','Paul-Frendo-phone','Paul-Frendo-phone','Paul-Dorr,-DVM,-PhD,-MACE-phone','Patrick-Mahon-phone','Patrick-Ferland-phone','Patrick-Cassner-phone','Patricia-Mura-phone','papa-mbow-phone','Pankaj-Shukla-phone','Omar-Mohammed-phone','Oliver-Griengl-Schott-phone','Obi-Iwobi-phone','Norma-Anderson-phone','Norm-Buggele-phone','Norm-Buggele-phone','Nolan-Olivier-phone','Nikita-Sethi-phone','Niels-Kronborg-Andersen-phone','Nicole-N.O.E-Morris-phone','Nick-Poetsch-phone','Nick-Pavao-phone','Nick-Caputo,-build-ideas-phone','Nicholas-Stieg-phone','Nicholas-H.-Cruz-phone','Nevada-Winrow,-Ph.D-phone','Nelson-Erickson-phone','Nels-Benda,-PE-phone','Nellys-Flores-phone','Neil-Frank-phone','Ned-McDonnell-phone','Nate-Eisner-phone','Nakeia-Staley-phone','Moss-Tod-phone','Monty-McCurry-LION-phone','monte-young-phone','Mitchie-Rich-phone','Mitchell-Phillips-phone','Mitch-Staskiewicz-phone','Mimi-Watson-phone','Mike-Wilder-phone','Mike-Wilder-phone','Mike-Whitlatch-phone','Mike-Roma-phone','Mike-Price-phone','Mike-Phillips-phone','Mike-Phillips-phone','Mike-Morse-phone','Mike-Livingston-phone','Mike-George-phone','Mike-Denton-phone','Mike-Davis-phone','Mike-Bouthillet-phone','Mieka-Puzniak-phone','Michele-Miller-phone','Michael-Whalen-phone','Michael-Viscido-phone','Michael-Page-phone','Michael-Mercier-phone','Michael-Lau,-PMP,-CIM-phone','Michael-James-phone','Michael-Hosier-phone','Michael-Goetzman-phone','Michael-Glick-phone','Michael-Fitzpatrick-phone','Michael-Curtiss-phone','Michael-Brahm-phone','Micah-Laughmiller-phone','Melissa-Morris-phone','Melissa-Imes-phone','Melissa-Arps-phone','Melanie-Menard,-ACC,-CPCC-phone','Megan-Conyers-phone','Mayank-Prasad-phone','Matthias-Helbig-phone','Matthias-Helbig-phone','Matthew-Weisner-phone','Matthew-Mendelson-phone','Matthew-Colbert-Blocha-phone','Matthew-B.Louis-Morano-phone','Matt-White-phone','MARY-WOLFF-phone','Mary-McCall-phone','Mary-Ackley-phone','Mary-(Gower)-Palmieri-phone','Martin-Gonzalez-phone','Martin-Deprey-phone','Marshall-P.-phone','Mark-Reinsmith-phone','Mark-Prausnitz-phone','Mark-Morse-phone','Mark-McLemore-phone','Mark-Jacobs-phone','Mark-G.-phone','Mark-Cohen-phone','Mark-A.-Otero-phone','Marisol-V-Garcia-de-los-Salmones-phone','Mariela-Callaway-phone','Maria-Rafferty-phone','Margaret-Menard-phone','Marcus-Guy-phone','Marcio-Soza-phone','Marcela-Rios-Vessell-phone','Marc-Katz-phone','Marc-Henderson-phone','Lynwood-Hamilton-phone','Lynn-Vera-(lrvera@gmail.com)-phone','Lyle-Silverman-phone','Lucian-Greco-phone','Lucas-Nguyen-phone','Lorin-Pierson-phone','Liza-Leal-phone','Lisa-Hawkins-phone','Linda-J.-Hansen-phone','Lillian-Shaw-phone','leslie-bacharach-phone','Leon-Lamphear-phone','Lee-Hammond-phone','Lawrence-"Larry"-Cutting-phone','Lavada-Travillian-phone','Laura-Milliken-Gray-phone','Laura-Ling-phone','Laura-Jane-Smith-phone','Laura-Anderson-phone','Larry-Walters-phone','Lankhorst,-Dietz-phone','Kyle-Amaker-phone','Kurt-Butler-phone','Kristina-Simpson-phone','Kory-Angstadt-phone','Kirtida-Rana,-M.D.-phone','Kirsten-(Kirsten-Wood)-Milliken,-PhD-phone','Kirk-Gary-phone','Kiran-Eduri-phone','Kip-Bennett-phone','Kimberly-Denson-phone','Kim-Kelley-phone','Kieran-Cox-phone','Kevin-Wiedeman-phone','Kevin-Sroka-phone','Kevin-Schleusner-phone','Kevin-Palmer-phone','Kevin-Mitchum-phone','Kevin-Mackey-phone','Kevin-Lynch-phone','Kevin-Lynch-phone','Kevin-Lange-phone','Kerry-Anne-Ducey-phone','Kent-Nash-phone','Kent-Nash-phone','Ken-Lucas-phone','Kelvin-Cornell-Ritman-phone','Kelly-L.-Derricks-phone','Kelley-Edwards-phone','Keith-Wundrow-phone','Keith-Payne-phone','Keith-Espelien-phone','Keith-Bridgford-phone','Kavitha-Krishnan-phone','Kathy-Boyler-phone','Karsten-Zieger-phone','Karry-Dayton-phone','Karen-Palasek-phone','Justin-Zimmerman-phone','Justin-M.-Bibb-phone','Justin-Fortinberry,-MBA-phone','Justin-Engles-phone','Justin-Boyd-phone','Jurgen-Lau-phone','Julie-Harris-phone','Julie-Ford-phone','Julia-Hurley-phone','Judy-R.-Walton,-Ph.D.-phone','Juan-Carrares-phone','Joyce-Bellefeuille-phone','Josue-Fuentes-phone','Josue-Fuentes-phone','Joshua-Taylor-phone','Josh-Perkins-phone','Josh-Daulton-phone','Joseph-Thompson-phone','Joseph-S.-Redmon-Jr.-phone','Joseph-Ruggiero-phone','Joseph-Pinion-III-phone','Joseph-Bianchi-phone','Jose-Pepe-phone','Jordan-Sneathen-phone','Jonathan-Maylott-phone','Jon-Templeman-phone','Jon-Liddle-phone','Jon-Gamble-phone','Johnathan-Lewis-phone','John-Weisz-phone','John-Stokely-phone','John-Rochford-phone','John-Murray-phone','John-Murray-phone','John-Michael-phone','John-Michael-phone','John-Merx-phone','John-M.-Morris-phone','John-Lillard-phone','John-Celona-phone','John-Bolton-phone','John-and-Tanya-Bratz-phone','Joe-Zuiker-phone','Joe-Rutte-phone','Joe-Petrillo,-P.-Eng-phone','Joe-Moen-phone','Jin-Wei-Tioh-phone','Jin-Wei-Tioh-phone','Jimi-Beach-phone','Jim-Truett-phone','Jim-Quayhackx-phone','Jim-Quayhackx-phone','Jim-Monahan-phone','Jim-Kennedy-phone','Jim-Hoy-phone','Jim-Handzo-phone','Jim-Fournier-phone','Jim-Dody-phone','Jim-Dickie-phone','Jim-DeVuono-phone','Jim-Corrigan-phone','Jim-Companik-phone','Jim-Cheng-phone','Jill-Donahue-phone','Jessie-Whisney-phone','Jessica-Blair-phone','Jesse-Taff-phone','Jerry-Shepherd-phone','Jerry-Chao-phone','Jeremy-Korn-phone','Jeremy-Hoffman-phone','Jeremy-Cortez-phone','Jeremy-Burnham-phone','Jennifer-Troiano-phone','Jennifer-Betz-phone','Jenna-Bollard,-MA,-MT-BC,-CCLS-phone','Jejuan-Toney-phone','Jeffrey-Stickles-phone','Jeffrey-Jones-phone','Jeffrey-Jones-phone','Jeffrey-Jackman-MBA-phone','Jeffrey-D.-Lovell-phone','Jeff-Womack-phone','Jeff-Wiegers-phone','Jeff-Thompson-phone','Jeff-Schaaf-phone','Jeff-Rega-phone','Jeff-Krause-phone','Jeff-Heck-phone','Jeff-Edwards-phone','Jeff-Campbell-phone','Jeff-Burket-phone','Jeff-Bullard-phone','Jeannette-Cole-phone','Jean-Patrick-Lucien-phone','Jay-Ballard-RT(R)(CT),RN-phone','Jay-Anderson-phone','Jason-Vance-phone','Jason-Reber-phone','Jason-Owen-phone','Jason-Myers-phone','Jason-Mattingly-phone','Jason-Kolecki-phone','Janet-Stieg-RN,-MS,-CPHQ-phone','Jan-McAlpin-phone','Jamie-Ethier-phone','James-Warren-phone','James-Tucci-phone','James-Kendrick-phone','James-J.-OConnor-phone','James-Holsem-phone','James-Hai-Zeng-phone','James-Craig-phone','James-Coombes-phone','James-Balman,-PMP-phone','James-Allen-Regenor-phone','Jamal-R.-Brown-B.S.,-M.B.A.-phone','Jair-Morselli-phone','Jai-Prakash-phone','Jacqueline-McFerren-phone','Jack-Springer-phone','Jack-Garda-phone','Ivar-Chhina-phone','Ivan-M.-Bermudez-phone','Ivan-Hovey-phone','Ivan-Hovey-phone','Ivan-Hernandez-phone','Israel-Conder-phone','Ishan-Taparia-phone','Irene-Szeto-phone','Irene-C-phone','Ilya-Golubovich-phone','Igor-Polivanyi-phone','Igor-Naroditsky-phone','IC-Woods-phone','Hugh-Michael-Quinlan-phone','Huaiying-Kang-phone','http://www.morbark.com/-phone','Howard-Kosel-phone','Hinrich-Schmidt-phone','Hilary-Morris-phone','Henry-Febles-phone','Henry-(Hong)-Zhao-phone','Hector-Guizar-phone','Harry-Gaulke-phone','Harold-Mullican-phone','Harold-Mullican-phone','Harold-Mullican-phone','Guy-Laurie-phone','Guy-Kawasaki-phone','Guy-Guzman-phone','Guillermo-Zambrano-phone','Gregory-Topel-phone','Gregory-S-Jones-phone','Gregory-Hartmann-phone','Greg-Ward-phone','Greg-St.clair-phone','Greg-Geers-phone','Greg-Casteel-phone','Green-Leaf-Conservation-and-Mitigation-Services-phone','Gordon-Sturm-phone','Gordon-Russell-phone','Gopal-Khaitan-phone','Golsa-Naderi-phone','George-Kramer-phone','George-A.-Laguros-phone','Geoffrey-Gaier-phone','Geoff-Maffett-phone','Gary-Shadick-phone','Gary-Pecor-phone','Gary-Olson-phone','Gary-Hill-phone','Galia-Frez-phone','Gabriel-Alfageme-phone','Gabe-Isham-phone','Fred-Zander-phone','FRED-BECK-phone','Frank-Williams-phone','Frank-Uttaro-phone','Frank-Rasco-phone','Frank-Gazzano-phone','Frank-Bernardo-phone','Franck-Onambele-phone','Eugene-Fernandez-phone','Etienne-Perin-phone','Ernie-Thomas-Jr.-phone','Ernest-M.-Ervin-phone','Erin-Scheller-phone','Erik-R.-Peebles-phone','Eric-Welak-phone','Eric-V.-Straumins,-MBA-phone','Eric-Schwartz-phone','Eric-S-Snyder-phone','Eric-Leopardi-phone','Eric-Frazer-phone','Eric-Faccenda-phone','Eric-Curtis-phone','Eric-Bondy-phone','Enrique.-Cabrera-phone','Elizabeth-Parker-phone','Eddie-Lazzari-phone','Ed-Morris-phone','Ed-Fisher-phone','Ed-Bonnema-phone','Earl-Wiggins-phone','Dusty-Rhoades-phone','Drew-Whitney-phone','Drew-Ammons-phone','Dr.PANNEER-R-phone','Dr.-Reginald-Hicks-phone','Dr.-David-E.-Wade,-DC-phone','Dr.-Andreas-Erich-Geiger-phone','Doug-Miller-phone','Doug-Gibbs-phone','Doug-Cook-phone','Doug-Beckemeyer-phone','Doug-Bartman-phone','Doug-Allen-phone','Donna-Tallent-phone','Donna-Boner-phone','Donna-Baxter-Porcher-phone','Donald-Lavin-phone','Don-Vandegrift-phone','Don-Matheson-phone','Don-Hale-phone','Don-Hale-phone','Dinesh-Katariya-phone','Devin-McAllister-phone','Derrick-Bavol-phone','Dennis-Fuge-phone','Dennis-Benbow-phone','Denise-Schmidt-phone','Denise-Caruzzi-phone','Demond-Shawn-Lee-phone','Demetria-Hickson-phone','Deborah-S.-Kent,-SPHR,-SHRM-SCP-phone','Dean-Howard-phone','Dayne-Barrow-phone','David-Watton-phone','David-Shank-phone','David-Sawyer-phone','David-Prahl-phone','David-Michaelson-phone','David-Mast,-PE,-PMP-phone','David-Jarrow-phone','David-Hung,-M.D.-phone','David-Heppner-phone','David-Hauser-phone','David-Harbert-phone','David-H.-Bush---PhD,-CQE-phone','David-Frey-phone','David-Crate-phone','David-Abramowitz-phone','Dave-Voy-phone','Dave-Verkler-phone','Dave-Sitt-phone','Dave-Pearce-phone','Dave-DeBolt-phone','Dave-Bruhn-phone','Daryl-Sinclair-phone','Darren-Moye-phone','Darrel-Morris-phone','Danny-Gasper-phone','Daniel-Thome-phone','Daniel-Sunday,-MBA,-CPIM-phone','Daniel-Shepard-phone','Daniel-Pieralisi-phone','Daniel-Ourada-phone','Daniel-Hunt-phone','Daniel-Cadotte-phone','Daniel-Buckmaster-phone','Daniel-Abate-phone','Dan-Schiro-phone','Dan-OShea-phone','Dalton-Hirst-phone','Dale-Johnson-phone','Dahl-Winters-phone','D.-Joycea-"DJ"-Martin-phone','Curry-Russell-phone','Cristie-Vollmar-phone','Craig-Hickman-phone','Craig-A.-White-phone','Cory-Dugger-phone','Connor-Cureton-phone','Concussion-Mitigation-Technologies-phone','Cole-O.-Harris-phone','Cody-Wilson,-CSP-phone','Cody-Wilson,-CSP-phone','Cody-Lott-phone','Cody-Gough-phone','Clinton-Pearce-phone','CLINT-REED-phone','CLINT-REED-phone','Clint-DeLozier-phone','Clifton-Morris-phone','Cliff-Kodama-phone','Clayton-Creamer-phone','Clark-Leffert-phone','Clark-Leffert-phone','Claire-Nordstrom-phone','Cindy-Brendel-MA,-CPC,-SPHR-phone','Cindy-Bell-phone','Cindi-Ashbeck-phone','Chuck-Morris-phone','Christopher-Roche-phone','Christopher-Morin-phone','Christopher-Madaras-phone','Christopher-Greene,-BA-phone','Christopher-Craig-phone','Christopher-Cklamovski-phone','Chris-Tichenor-phone','Chris-Sextro-phone','Chris-Sextro-phone','Chris-Scalisi,-CSP,-CHMM,-REM,-COSS-phone','Chris-Newton-phone','Chris-Newton-phone','Chris-Misztur,-CSM-phone','Chris-Hornung-phone','Chris-Goodenough-phone','Chris-Brooks-phone','Cheryl-Hirschlein-phone','Chemin-Lambert-phone','Chayse-Roth,-MBA-phone','Charles-Smith-phone','Charles-R-Newberry-phone','Charles-Pollock-phone','Charles-Moog-phone','Chad-Wilson-phone','Chad-S.-Brown,-CPA-phone','Chad-Douglas-phone','Chad-Brister-phone','Cedrick-Richardson-phone','Cathy-Penrod-phone','Cathy-Fernandez-phone','Casper-Badenhorst-phone','Casey-Simpson-phone','Carrie-Angelico-phone','Carol-McCauslin-phone','Carlotta-(Hall-Bosse)-Strandberg-phone','Caleb-Bolen-phone','C.-Scott-Gilbert-phone','Buddy-Benford-phone','Budd-Kuyper-phone','Bryce-Stevens-phone','Bryan-Preeshl-phone','Bryan-Healy-phone','Bryan-Ball-phone','Bruce-Morrisseau-phone','Bruce-Meyer-phone','Bruce-Grau-phone','Bruce-Campbell-phone','Bruce-Arndt-CMRP-phone','Bruce-Adkins-phone','Brittany-Neish-phone','Britt-Morris-phone','Brinda-Balakrishnan,-M.D.,-Ph.D.-phone','Brielle-Maxwell-phone','Brian-Stewart-phone','Brian-Spears-phone','Brian-Smith-phone','Brian-Peterson-phone','Brian-Pascavis-phone','Brian-Moriarty-phone','Brian-Loma-phone','Brian-Kann-phone','Brett-Fisher-phone','Brete-Bigley-phone','Brandon-McMahon-phone','Brandon-Lee-phone','Bradley-S.-Helm-phone','Bradley-Hufstetler-phone','Brad-Roetman-phone','Brad-Feilmeier-phone','Bobby-North,-CPA.-phone','Bob-OHara,-CQE-phone','Bob-Mondore-phone','Bob-Jamieson,-Ed.D.,-CISSP-phone','Bob-Hadcock-phone','Blake-Carnes-phone','Blair-Gilgallon-phone','Bill-Schumacher-phone','Bill-Pearson-phone','Bill-Lechten-phone','Bill-Carbone-phone','Bill-Berg-phone','Bilawal-Channan-phone','Beverly-Conklin-phone','Bennett-Noreen,-MBA-phone','Benjiman-Williams-phone','Ben-Schreivogel-phone','Belinda-Bentley,-PhD-phone','Basil-Horangic-phone','Barry-Higgins-phone','Barbara-Mariner-phone','Ayan-Gonzalez-phone','Atif-Zafar-phone','Asif-Mehdi-phone','Ashley-Molson-phone','Ashlee-Weeks-phone','Artie-Tessmann-phone','Art-Bourasseau-phone','Arlen-Burger-Ph.D.-phone','Arlen-Burger-Ph.D.-phone','April-Mendez-phone','Anushka-B.-phone','Antony-Wilson-phone','Antony-Ng-Yukshing-phone','Antonio-Shappley-phone','Antoine-Dennison-phone','ANTHONY-ZELLARS-phone','Anthony-Stark-phone','Anthony-Schiro-phone','Anthony-Morris-phone','Anthony-Moore-phone','Anthony-Luiz,-CP-FS-phone','Angela-Biles-phone','Angel-Diaz-phone','Andrew-Poole-phone','Andrew-Nunenkamp-phone','Andrew-Konkle-phone','Andrew-Forcucci-phone','Andrew-Bidlen-phone','Andrew-Betz-phone','Andreas-Huber-phone','Ana-Elisa-Cazares,-MBA-phone','Amy-Gibby-phone','Amber-Mabry-phone','Amanda-Burns-phone','Alyn-Cardarelli-phone','Alton-Jordan-phone','Alton-Jordan-phone','Altaf-Mulla-phone','Allistair-Lee-phone','Allison-Taylor-phone','Allen-Leslie-Savage-Jr.-phone','Allen-Goldberg-phone','Ali-Habib-phone','Alfonso-iniguez-phone','Alex-Courtney-phone','Aleem-L.-Morris-phone','Alden-Doyle-phone','Alberto-Villalon-phone','Alan-Matejak-phone','Addison-Carey-phone','Adam-Perez-phone','Adam-Maulick-phone','Adam-Lewis-phone','Adam-Kimmel-phone','Adam-Childs-phone','Abraham-Thomas-phone','Abiy-Makonnen-Berehe-(Capt.)-JDUSA-phone','Abhijeet-Gole-phone','Aaron-Pontow-phone','A.-Fard-phone','Terry-Hobson-phone','Steve-Julson-phone','Ben-Ancona-phone']

for name in names:
    print (name,)

    cursor = conn.execute("SELECT * from outbound_all where field1 LIKE  '%"+name+"%'")
    row = cursor.fetchone()

    if not row is None:
        print (row[0].split('_')[1])
    else:
        print()


conn.close()
