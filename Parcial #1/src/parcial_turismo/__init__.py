from parcial_turismo.data import Region, Zona, Reserva


regiones = [
        Region(1, "Bocas del Toro",
               "La provincia de Bocas del Toro tiene un área de 4.643,9 kilómetros cuadrados, que comprende el "
               "continente y nueve islas principales. La provincia consiste en el Archipiélago de Bocas del Toro, "
               "Bahía Almirante, Laguna de Chiriquí, y la tierra firme adyacente.",
               [
                   Zona("Archipiélago de Bocas del Toro", 500,
                        "El archipiélago de Bocas del Toro es un grupo de islas en el mar Caribe el cual se localiza "
                        "al noroeste de la república de Panamá. Este conjunto de islas separa la bahía del Almirante "
                        "y la laguna de Chiriquí, desde la apertura del mar Caribe.",
                        "\u29BF 1 Noche\n"
                        "\u29BF Desayuno\n"
                        "\u29BF Masaje\n"),
                   Zona("Laguna de Chiriquí", 800,
                        "La laguna de Chiriquí Grande es una laguna costera del mar Caribe de Panamá; puerto natural "
                        "localizado junto a la frontera sureste de Costa Rica, en la provincia de Bocas del Toro. "
                        "Está flanqueada por las puntas Térraba al noroeste, y Valiente y Chiriquí Grande en la "
                        "península Valiente al sureste.",
                        "\u29BF 3 Noches\n"
                        "\u29BF Desayuno\n"
                        "\u29BF Masaje"),
                   Zona("Isla Colón", 800,
                        "La isla Colón es la península principal del archipiélago de Bocas del Toro, situado al "
                        "noroeste de Panamá en el mar Caribe. Con una superficie de 61 km², es la isla más grande de "
                        "la provincia de Bocas del Toro y la cuarta más grande del país.",
                        "\u29BF 4 Noches\n"
                        "\u29BF Cena\n"
                        "\u29BF Viaje en barco"
                        ),
                   Zona("Parque Nacional Isla Bastimentos", 750,
                        "El Parque nacional marino Isla Bastimentos se encuentra ubicado en el Archipiélago "
                        "de Bocas del Toro al norte de la provincia del mismo nombre, cerca de la ciudad de Bocas del "
                        "Toro y la aldea indígena Ngäbe-Buglé Salt Creek. Fue creado en 1988 y cuenta "
                        "con una superficie de 13.226 hectáreas, representando el 6.6% del área total del "
                        "archipiélago.",
                        "\u29BF 6 Noches\n"
                        "\u29BF Almuerzo\n"
                        "\u29BF Ver cangrejos"
                        )
               ]),
        Region(1, "Chiriquí",
               "Chiriquí es una provincia de Panamá. Su capital es David. La provincia de Chiriquí se encuentra "
               "ubicada en el sector occidental de Panamá teniendo como límites al norte la provincia de Bocas del "
               "Toro y la comarca Ngäbe-Buglé, al oeste la provincia de Puntarenas (en la República de Costa Rica), "
               "al este la provincia de Veraguas y al sur el océano Pacífico. "
               "Chiriquí tiene una superficie de 6547,7 km². Tiene algunos ríos como el Palo Alto, Caldera, Chiriquí, "
               "Chiriquí Viejo, Los Valles, Cochea, Colgá, Papayal, Agua Blanca, Piedra, David, Fonseca, San Félix, "
               "Tabasará. Limita al norte con Bocas del Toro y la comarca Ngäbe Buglé, al oeste con Costa Rica, "
               "al este con Veraguas y al sur con el océano Pacífico.",
               [
                   Zona("David", 600,
                        "Es la capital de la provincia. Posee una población de 118 000 y esta ciudad es la tercera en "
                        "popularidad. Para los finales de el siglo XIX, David tenía solo seis calles, de las cuales "
                        "cuatro le pertenecían al centro del pueblo, lo cual hoy se conoce como el Barrio Bolívar, "
                        "en el centro del pueblo podemos hallar.",
                        "\u0085 1 Noche\n"
                        "\u0085 Almuerzo\n"
                        ),
                   Zona("Boquete", 800,
                        "A solo 45 minutos de la ciudad de David se encuentra Boquete, un lugar conocido como “la "
                        "ciudad de la eterna primavera” o “la ciudad de las flores y el café",
                        "\u0085 1 Noche\n"
                        "\u0085 Desayuno\n"
                        ),
                   Zona("Cerro Punta", 500,
                        "Es un pueblo situado en el norte de la provincia de Chiriquí que tiene de un clima "
                        "agradable, bellas flores, hermosas vistas y complementado por el trabajo de agricultura que "
                        "se realiza en esta zona. Con una población aproximada de 7000. Cerro Punta se encuentra a "
                        "unos 1970 m s. n. m. con una temperatura entre los 10 y 15 ºC",
                        "\u0085 1 Noche\n"
                        "\u0085 Cena\n"
                        ),
                   Zona("Volcán", 750,
                        "Es un pueblo situado en las faldas del volcán Barú. Desde su pico situado a 3475 m s. n. m., "
                        "puede ver el océano Pacífico y el mar Caribe. Volcán es comúnmente conocido como “La pequeña "
                        "Suiza”, desde que muchos inmigrantes de este país se establecieron aquí y construyeron "
                        "pequeñas villas con la arquitectura típica de su ciudad de origen",
                        "\u0085 2 Noches\n"
                        "\u0085 Almuerzo\n"
                        )
               ]),
        Region(1, "Veraguas",
               "La novena provincia de Panamá, Veraguas, considerara “la perla entre dos océanos”  por ser la única "
               "provincia que tiene costas en el océano Atlántico y Pacifico. Está dividida en 12 (doce) distritos: "
               "Atalaya, Calobre, Cañazas, La Mesa, Las Palmas, Mariato, Montijo, Río de Jesús, San Francisco, "
               "Santa Fe, Santiago y Soná. Su capital es la ciudad de Santiago de Veraguas. "
               "Ubicada a tan solo 5 horas en automóvil de la capital de panamá, cuenta con un clima tropical húmedo "
               "en las áreas mas bajas y templado muy humeado de altura en el área de la cordilla. Aquí podrás "
               "encontrar un sinfín de lugares para visitar.",
               [
                   Zona("Parque Nacional de Coiba", 400,
                        "El Parque Nacional Coiba protege los mejores arrecifes de coral del Pacífico panameño y es "
                        "la reserva marina más importante del país. Esta isla está formada con las rocas más antiguas "
                        "de Panamá, que se crearon hace 70 millones de años en el fondo del mar, a 1.300 kilómetros "
                        "de distancia y que luego fueron movidas a su ubicación actual a través de poderosas fuerzas "
                        "geológicas. Por 85 años, Coiba albergó la prisión más temida de Panamá pero hoy es un "
                        "santuario de biodiversidad y Patrimonio de la Humanidad UNESCO.",
                        "\u0085 Observación de Vida Marina\n"
                        "\u0085 Bucear e ir a Playas\n"
                        ),
                   Zona("Santa Fe", 600,
                        "Santa Fe se encuentra en las tierras altas de Veraguas, un paraíso ecológico, hogar a una "
                        "amplia variedad de animales y plantas, incluidas las orquídeas.  Esta selva tropical es "
                        "ideal para practicar senderismo y observación de aves. Cuenta con más de 50 cascadas para "
                        "explorar, nadar y reconectarse con la naturaleza.",
                        "\u0085 1 Noche\n"
                        "\u0085 Rapel\n"
                        "\u0085 Biccleta de Montaña\n"
                        ),
                   Zona("La Yeguada", 800,
                        "La Yeguada pertenece al complejo volcánico Chitra – Calobre, de la provincia de Veraguas, "
                        "su última erupción fue en 1620 y aún no se considera extinto. La Reserva La Yeguada ofrece "
                        "áreas para camping, fogata y un sendero que lleva a la Cascada El Desvío.",
                        "\u0085 1 Noche\n"
                        "\u0085 Almuerzo\n"
                        ),
                   Zona("Santa Catalina", 640,
                        "Santa Catalina es una población costera, perteneciente a la provincia de Veraguas, "
                        "ubicada en el Golfo de Montijo, Costa Pacífica. La playa se ha dado a conocer mayormente por "
                        "las excelentes olas que su mar brinda a los surfistas que llegan constantemente a disfrutar "
                        "del deporte. Competencias nacionales e internacionales tienen lugar durante todo el año y su "
                        "nombre ya circula en el ambiente del surf internacional.",
                        "\u0085 2 Noches\n"
                        "\u0085 1 Lagartija de mascota\n"
                        )
               ]),
        Region(1, "Herrera",
               "Herrera esta situada en el norte de la península de Azuero y su cabecera es la ciudad de Chitré. "
               "Limita al norte con las provincias de Veraguas y Coclé, al sur con la provincia de Los Santos, "
               "al este con el golfo de Parita y la provincia de Los Santos y al oeste con la provincia de Veraguas "
               "concretamente con el distrito de Mariato. Tiene una extensión de 2.340,7 km² y en 2008 contaba con "
               "una población de 111.647 habitantes, población que se estimó en 107.911 habitantes en 2010."
               "Es en honor al General Tomás Herrera. Herrera fue un militar y político neogranadino, presidente de "
               "la República de Colombia y jefe de estado del Estado Libre del Istmo durante 1840 y 1841. La "
               "etimología de Herrera, proviene del apellido patronímico castellano Herrera",
               [
                   Zona("Parque nacional de sarigua", 400,
                        "Ubicado en la ribera de la península de Azuero, en el estado de Herrera. Es una reserva "
                        "natural con un área de 7.000 hectáreas que contiene ecosistemas semidesérticos y albinos. "
                        "Albina, figura que esta área ha sufrido un proceso natural por el cual este territorio posee "
                        "un alto nivel de salinización con un 80%. Allí, viven animales extraños y curiosos como la "
                        "boa constrictora, la temible iguana negra, el lagarto ojigordo y los tradicionales "
                        "armadillos. El Parque Nacional Sarigua ha erosionado los panoramas, los colores "
                        "contrastantes y las impresionantes formaciones rocosas. Igualmente posee restos de "
                        "civilizaciones precolombinas que han depuesto de un legado de objetos metálicos y "
                        "herramientas que es invaluable.",
                        "\u0085 1 Noche\n"
                        "\u0085 Almuerzo\n"
                        ),
                   Zona("Sarigua La Mula", 350,
                        "Es la ciudad más vieja de la península de Azuero. Era una población grande que fue ocupado "
                        "entre 870 y 20 aC. Los lugareños se dedicaban primordialmente al cultivo del maíz, "
                        "la caza y la pesca. Cerca de la población, hay un reservorio de Jaspe que fue explotado para "
                        "fabricar armas y herramientas. Es un parque precolombino y arqueológico, dentro del Parque "
                        "Nacional Sarigua, que muestra el proceso de desertificación en la región que limita con el "
                        "Golfo de Parita.",
                        "\u0085 1 Noche\n"
                        "\u0085 Almuerzo\n"
                        ),
                   Zona("Cenegon del Mangle", 800,
                        "Es conocido y concurrido por los aldeanos porque dicen que cura. Situado en la ciudad de "
                        "París en Parita, es un viaje con grandes intereses ecológicos que cuenta con seis tipos de "
                        "manglares. Igualmente se encuentran pantanos y humedales. Asimismo se conoce con el nombre "
                        "de nido de garza porque estas aves habitan allí. Por otro lado, consigue visitar la Cueva "
                        "Del Tigre, que tiene unos 12,000 años de antigüedad o pozos minerales calientes en forma de "
                        "cráteres. Allí podrás nadar y sentir sus poderes curativos.",
                        "\u0085 1 Noche\n"
                        "\u0085 Almuerzo\n"
                        ),
                   Zona("Museo de Arte", 4000,
                        "El Museo de Arte Religioso Colonial se localizaba en la antigüedad, la Capilla de Santo "
                        "Domingo, consagrada a la devoción de la Virgen del Rosario. El lugar donde se encuentra el "
                        "museo estaba compuesto por una iglesia, está en ruinas, una capilla y un monasterio que "
                        "tenía un claustro en un gran patio. Fue uno de los retiros pioneros en la capital. En el año "
                        "1941 los restos de la capilla de este grupo fueron declarados Monumento Nacional. Fue "
                        "restaurada en el año 1971 y la antigua iglesia y el claustro del Convento de Santo Domingo "
                        "se convirtieron en lugares para actividades culturales de verano.",
                        "\u0085 1 Noche\n"
                        "\u0085 Almuerzo\n"
                        )
               ]),
        Region(1, "Los Santos",
               "Los Santos es una provincia panameña, situada al sureste de la península de Azuero. Las Tablas es su "
               "capital y localidad más poblada. Está compuesta por los distritos de Los Santos, Guararé, Las Tablas, "
               "Macaracas, Pedasí, Pocrí y Tonosí. Con una superficie de 3 809,4 km² y una población de 89 592 "
               "habitantes,4limita al sur y al este con el océano Pacífico, al norte con el océano Pacífico y la "
               "provincia de Herrera, y al oeste con la provincia de Veraguas, concretamente con el distrito de "
               "Mariato.",
               [
                   Zona("Parque Nacional Cerro Hoya", 400,
                        "Pertenece a las jurisdicciones de los Santos y veraguas. Está a 350 km de la capital de "
                        "Panamá. Este parque volcánico posee una extensión de 32,579 acres y tiene los tres picos más "
                        "altos en la península de Azuero, Cerro Hoya, Moya y Soja. Se puede ver desde los boscajes "
                        "tropicales en las montañas, hasta un clima tropical húmedo a lo largo de la playa. Por ello "
                        "tiene una gran diversidad de fauna y flora, por ejemplo: árboles, guayacanes, cóndores reyes "
                        "u manchotas. Los principales ríos nacen el Parque Nacional Cerro Hoya, que posee fantásticas "
                        "cascadas y piscinas termales con agua cristalina.",
                        "\u0085 1 Noche\n"
                        "\u0085 Almuerzo\n"
                        ),
                   Zona("El Coche Los Santos", 600,
                        "Desde la ciudad de Panamá hasta la jurisdicción de Veraguas es accesible por Atalaya a "
                        "Mariato y Arenas. Desde allí consigue ir directamente a Las Flores, Changuales, "
                        "Puerto Payita y Restingue. Coche de la ciudad de Panamá a la jurisdicción de Los Santos. Se "
                        "llega a la ruta de Las Tablas Pedasì por medio de Los Vallerrico o asientos, o por medio de "
                        "Llano de Piedras Macaracas desde donde se alcanza a Tonosí. Desde allí consigue ir a "
                        "Cambutal, Cucu, Window o El Cortez, jurisdicciones, bancos de arena.",
                        "\u0085 1 Noche\n"
                        "\u0085 Almuerzo\n"
                        ),
                   Zona("Playa Venao", 500,
                        "Es una playa donde cada fin de semana 500 jóvenes vienen a disfrutar de la naturaleza y del "
                        "surf. Es popular porque es donde se celebran competiciones nacionales e internacionales para "
                        "surfistas. Posee 3.5 km de playa y su ambiente es seco con un clima desértico. Tiene un "
                        "divino amanecer, por lo que si anhela pasar unos días explorando la playa, consigue acampar "
                        "o arrendar cabañas.",
                        "\u0085 1 Noche\n"
                        "\u0085 Almuerzo\n"
                        ),
                   Zona("Playa El Arenal", 780,
                        "Es una playa linda de arena fina y aguas tranquilas. Es ideal para tomar el sol, "
                        "nadar o practicar deportes acuáticos. Esta playa no posee instalaciones turísticas por lo "
                        "que es digno llevar paraguas, comida y agua. Si quieres comer en un refectorio tendrás que "
                        "ir al pueblo de Pedasí. Aquí consigue tomar un barco a la isla Iguana que se halla frente a "
                        "esa playa.",
                        "\u0085 1 Noche\n"
                        "\u0085 Almuerzo\n"
                        )
               ]),
        Region(1, "Coclé",
               "Su superficie es de 4,927km² y cuenta con 260 292 habitantes (2010).1 Su capital es Penonomé. Su "
               "nombre se origina probablemente del caudaloso Río Coclé del norte y Río Coclé del Sur, que atraviesan "
               "sus territorios. Otro origen posible se debe al Cacique Coclé que dominaba la Llanura Central. "
               "También es una provincia de gran riqueza natural y material. Se encuentra el acceso por tierra a la "
               "mina de Petaquilla ubicada en Coclésito, distrito de Donoso en la provincia de Colon."
               "La provincia de Coclé es un paraíso de grandes atractivos naturales y turísticos. En la provincia de "
               "Coclé se puede disfrutar de una riqueza cultural, folklórica, clima fresco en el Valle de Antón o "
               "tropical en sus hermosas playas",
               [
                   Zona("El Parque Arqueológico El Caño", 400,
                        "Se encuentra en el distrito de Natá, provincia de Coclé. Aproximadamente a unos 117 "
                        "kilómetros de la Ciudad de Panamá. El parque posee unas 8 hectáreas. El parque ofrece una "
                        "muestra vestigios de la época pre-colombina. La historia de ese sitio data del año 800 D.C. "
                        "y muestra las costumbres y cultura de los grupos humanos que se desarrollaron en esta zona. "
                        "El descubrimiento de este sitio arqueológico ocurre entre 1926 y 1927, por parte del "
                        "norteamericano Hyatt Verrill. El mismo realiza algunas excavaciones por parte de la Heye "
                        "Foundation y envía valiosas piezas tallada con rostros, columnas y megalitos, al Museo del "
                        "Indio Americano de New York.",
                        "\u0085 1 Noche\n"
                        "\u0085 Almuerzo\n"
                        ),
                   Zona("El Valle de Antón", 2000,
                        "Es un sitio muy agradable cuenta con un clima fresco que oscila en los 18°C durante todo el "
                        "año. Se encuentra situado en un cráter volcánico extinto de 18.3 km2. Hay muchos lugares "
                        "para visitar como: La Piedra Pintada, La India Dormida, El zoológico El Nispero y muchos "
                        "más.",
                        "\u0085 1 Noche\n"
                        "\u0085 Almuerzo\n"
                        ),
                   Zona("Caño la Angostura de Penonomé", 3000,
                        "Un poco más allá de la ciudad de Penonomé, en la provincia de Coclé se encuentra La "
                        "Angostura. Considerado uno de los sitios de mayor belleza natural de la provincia, "
                        "del cual hasta compositores famosos, han escrito sobre él, como por ejemplo Gladys De La "
                        "Lastra que le refirió como “la garganta del río Zaratí”. Ciertamente “la serpiente de plata” "
                        "es conocido como un punto de atracción y diversión para locales y extranjeros por igual, "
                        "y saben que hay mucho para disfrutar de este lugar. La naturaleza encoge al río en este "
                        "punto y hasta veces hasta se convierte en cascadas, pasa fuertemente por medio de un par de "
                        "montañas que crean un cañón. Por su particularidad geológica, este lugar ha sido comparado a "
                        "el Gran Cañón de Colorado.",
                        "\u0085 1 Noche\n"
                        "\u0085 Almuerzo\n"
                        ),
                   Zona("Las Salinas de Aguadulce", 4000,
                        "Los depósitos de sal han tenido, desde la antigüedad, especial relevancia en el "
                        "emplazamiento de los asentamientos humanos. Por este motivo se crearon rutas específicas "
                        "para el mercadeo de sal y se han producido numerosas guerras por controlar los depósitos de "
                        "este mineral, las rutas de su comercialización y los mercados. El término sal es derivado "
                        "del latín salarium, y tiene su origen en la cantidad de sal que se le daba a los legionarios "
                        "romanos para que pudiesen conservar sus alimentos, en las largas campañas militares.",
                        "\u0085 1 Noche\n"
                        "\u0085 Almuerzo\n"
                        )
               ]),
        Region(1, "Colón",
               "Su extensión territorial es de 4.868,4 km². Su población es de 294.060 habitantes (2019) y su "
               "densidad es de 60,4 habitantes por km² (2019). En su territorio se localiza la sección norte del "
               "canal de Panamá. es el principal puerto para el tráfico de casi toda la mercancía de importación y "
               "reexportación del país",
               [
                   Zona("Centro de Observación de la Ampliación", 250,
                        "Cerca de las Esclusas de Gatún, en Colón, aproximadamente a unos 77 kilómetros de la ciudad "
                        "capital, se encuentra el nuevo Centro de Observación de la Ampliación del Canal. El centro "
                        "ofrece las facilidades para poder observar los trabajos de construcción de la nueva esclusa "
                        "del lado Atlántico. Desde una área techada podrás apreciar los trabajos, más de 18 enormes "
                        "grúas se entremezclan con áreas de concreto y cuentan de los avances en esta nueva esclusa "
                        "que permitirá el paso de los barcos Postpanamax.",
                        "\u0085 Barcos\n"
                        "\u0085 Almuerzo\n"
                        ),
                   Zona("Fuerte San Lorenzo", 450,
                        "El Fuerte de San Lorenzo está localizado a la entrada del río Chagres en la provincia de "
                        "Colón, Panamá. Fue declarado por la UNESCO como Patrimonio de la Humanidad en el año 1980 "
                        "bajo la denominación de las Fortificaciones de la costa Caribe de Panamá, "
                        "con las fortificaciones de la ciudad de Portobelo. Formaban el sistema defensivo para el "
                        "comercio transatlántico de la Corona española y constituyen un magnífico ejemplo de la "
                        "arquitectura militar de los siglos XVII y XVIII.",
                        "\u0085 Cañones\n"
                        "\u0085 Fantasmas\n"
                        ),
                   Zona("Las Esclusas Del Canal", 600,
                        "Las esclusas del canal de Panamá, que levantan las naves 25,9 m hasta el punto más alto "
                        "del canal en el lago Gatún y luego las hacen descender,  fueron en su momento una de las "
                        "obras de ingeniería más grandes de su época, superada solamente por otras etapas del "
                        "proyecto de la vía interoceánica. No había otra construcción en hormigón armado comparable "
                        "en tamaño, hasta la construcción de la represa Hoover en la década de 1930. La longitud "
                        "total de las estructuras de las esclusas, incluyendo el acceso a las paredes, es de tres "
                        "kilómetros.",
                        "\u0085 Barquitos\n"
                        "\u0085 Agua marina\n"
                        ),
                   Zona("Isla Galeta", 800,
                        "Isla Galeta es el nombre de una isla de 299 hectáreas  situada en el lado atlántico de la "
                        "República de Panamá, al este de la ciudad de Colón. Isla Galeta fue el sitio donde se "
                        "encontraba un centro de comunicaciones militares de Estados Unidos de América mientras se "
                        "ocupó parte de ese país, la instalación estuvo activa desde la década de 1930 hasta el año "
                        "2002 momento en el que fue entregada oficialmente al gobierno de la República de Panamá.",
                        "\u0085 Iguanas\n"
                        "\u0085 Solo Iguanas\n"
                        )
               ]),
        Region(1, "Panamá Oeste",
               "Es la décima provincia del país, llena de una rica diversidad turística natural. Entre los sitios de "
               "interés para visitar está el Parque Nacional Campana, La Laguna de San Carlos , el cerro Trinidad "
               "entre otros. Las bellas playas que posee esta provincia han servido de atractivo para el "
               "establecimiento de hoteles y resorts. El Chorro de La Chorrera forma parte también del ecoturismo que "
               "ofrece Panamá Oeste, un destino perfecto para la recreación ecológica. ",
               [
                   Zona("Punta Chame", 500,
                        "Es un corregimiento del distrito de Chame en la provincia de Panamá Oeste. Punta Chame es un "
                        "lugar de windsurf popular a lo largo de la Bahía de Chame. Punta está al final de una "
                        "península larga y fina, bordeada por granjas camaroneras y manglares. Está a tan sólo una "
                        "hora y media en coche desde la ciudad de Panamá, por lo que es un sitio popular entre los "
                        "adictos a la adrenalina de la ciudad. De alguna manera, este es un lugar para escaparse de "
                        "todo, ya que solo hay una escuela de windsurf, algunos alojamientos y unas residencias.",
                        "\u0085 Surfing\n"
                        "\u0085 Almuerzo\n"
                        ),
                   Zona("Playa Gorgona", 500,
                        "Playa Gorgona, a 50 minutos de la ciudad de Panamá. Gorgona es un lugar tranquilo y "
                        "familiar. Es un lugar ideal como escaparate de la bulla de la ciudad o como destino "
                        "turístico para sus vacaciones. Rodeado de naturaleza, cuenta con tres playas de arena blanca "
                        "y negra. Entre ellas Playa Malibú, famosa como punto de surrf; Arena Negra, comúnmente "
                        "utilizada por los pescadores.",
                        "\u0085 1 Noche\n"
                        "\u0085 Almuerzo\n"
                        ),
                   Zona("La Arenosa", 400,
                        "La Arenosa es una pequeña localidad ubicada en el corregimiento de Iturralde, distrito de La "
                        "Chorrera, esta se encuentra a una hora de la ciudad de Panamá y desde finales de los 60, "
                        "principios de los 70 se ha convertido en uno de los lugares favoritos de los fanáticos de la "
                        "pesca de agua dulce. Es común que se le llame Lago La Arenosa a esta zona; sin embargo, "
                        "es la zona Occidental del Lago Gatún",
                        "\u0085 1 Noche\n"
                        "\u0085 Almuerzo\n"
                        ),
                   Zona("El Chorro de la Chorrera", 300,
                        "A una hora de la capital, a unos 20 minutos del centro de la ciudad, podrá encontrar una "
                        "impresionante cascada de agua que se forma del caudal del río Caimito, que nace en el cerro "
                        "Trinidad y atraviesa el Distrito de La Chorrera, enormes rocas que forman una escalinata "
                        "natural dan vida a este chorro.",
                        "\u0085 1 Noche\n"
                        "\u0085 Almuerzo\n"
                        )
               ]),
        Region(1, "Panamá",
               "En la provincia de Panamá, fundada en 1519, se encuentra ubicada la capital del país, la ciudad de "
               "Panamá. Esta es la octava provincia del país y es el principal centro cultural y económico del país, "
               "posee  una intensa actividad financiera y un centro bancario internacional. Panamá es una ciudad "
               "cosmopolita y dinámica, donde lo moderno y lo tradicional se unen para crear un ambiente alegre y "
               "relajado. ",
               [
                   Zona("Archipielado de Las Perlas", 250,
                        "Conformado por las islas: Contadora, Bartolomé, Saboga, Bayoneta, Viveros, Bolaños, Pacheco, "
                        "Mogo, Gibraleón, la Mina, Casayeta, Casaya, Galera, Cañas y San Telmo. Su nombre proviene de "
                        "la época colonial cuando fue nombrado así por Vasco Núñez de Balboa, por su abundancia de "
                        "perlas en sus alrededores. Aquí se halló la perla más famosa del mundo “ La Peregrina”, "
                        "única por su brillo, color y forma de pera, que fue parte del joyero de la actriz Elizabeth "
                        "Taylor, obsequio de su esposo Richard Burton.",
                        "\u0085 1 Noche\n"
                        "\u0085 Almuerzo\n"
                        ),
                   Zona("Canal de Panamá", 250,
                        "El Canal de Panamá es el mayor atajo del planeta y es una de las maravillas del mundo "
                        "moderno. Sus 80 kilómetros de longitud conectan los océanos Atlántico y Pacífico a través de "
                        "la porción más estrecha del continente. En toda su historia, más de 900.000 embarcaciones "
                        "han transitado el Canal para acercar el comercio, las culturas y las personas de todos los "
                        "rincones del mundo. Hoy esta maravilla de la tecnología puede ser descubierta en dos centros "
                        "de visitantes con miradores, exhibiciones y salas de proyección. Uno en las esclusas de "
                        "Miraflores, más cerca de la capital; y otro en las nuevas esclusas de Agua Clara, "
                        "a 25 minutos de la ciudad de Colón.",
                        "\u0085 1 Noche\n"
                        "\u0085 Almuerzo\n"
                        ),
                   Zona("Panamá Viejo", 800,
                        "El Conjunto Monumental Histórico de Panamá Viejo, designado como tal mediante la Ley 91 de "
                        "diciembre de 1976 y conocido también como Sitio Arqueológico de Panamá Viejo o como Panamá "
                        "La Vieja, se halla localizado dentro de la moderna ciudad de Panamá,  entre las "
                        "desembocaduras de los ríos Algarrobo y Abajo, frente a las costas del Océano Pacífico en la "
                        "sección más angosta del Istmo.",
                        "\u0085 1 Noche\n"
                        "\u0085 Almuerzo\n"
                        ),
                   Zona("Casco Antiguo", 600,
                        "El Casco Antiguo es el corazón histórico y cultural de la capital panameña. Fue fundado en "
                        "1673 como la ciudad de Panamá la Nueva, luego de la destrucción de la ciudad original "
                        "durante un ataque pirata. La arquitectura es una combinación de ruinas desde los días de los "
                        "Exploradores Españoles y Piratas, y Colonia Francesa del primer intento por construir el "
                        "Canal de Panamá por los franceses. Parques históricos cubren el conjunto del Casco Viejo, "
                        "con figuras como los generales heroicos a caballo, como el dedicado al Liberador Simón "
                        "Bolívar, que tiene su estatua situada en el centro del parque. Royal Palms destacan sobre "
                        "las plazas como centinelas de altura. La Iglesia de San Francisco, El Teatro Nacional, "
                        "Hotel Colonial, y el Colegio Bolívar ilustran detalles que llaman la atención de los "
                        "visitantes a la zona histórica",
                        "\u0085 1 Noche\n"
                        "\u0085 Resaca el dia siguiente\n"
                        )
               ]),
        Region(1, "Darién",
               "Su capital es la ciudad de La Palma. Tiene una extensión de 11 896,5 km², siendo por lo tanto la más "
               "extensa del país. Está ubicada en el extremo oriental del país y limita al norte con la provincia de "
               "Panamá y la comarca Guna Yala. Al sur limita con el océano Pacífico y la República de Colombia. Al "
               "este limita con el departamento de Chocó en la República de Colombia y al oeste limita con el Océano "
               "Pacífico y la Provincia de Panamá.",
               [
                   Zona("Parque nacional Darién", 400,
                        "Es uno de los sitios del Patrimonio de la Humanidad más importantes de Centroamérica"
                        "Fue declarado en 1981 como Patrimonio de la Humanidad1 y en 1983 como Reserva de Biosfera. "
                        "Sus especies más comunes son el guacamayo, el loro, el tapir y el águila arpía, "
                        "el Ave Nacional de Panamá. Este parque es valorado por su importante patrimonio genético, "
                        "la belleza de su paisaje escarpado y su selva",
                        "\u0085 1 Noche\n"
                        "\u0085 Almuerzo\n"
                        ),
                   Zona("La Palma", 600,
                        "La Palma es la capital de la provincia panameña de Darién,3 situada a orillas del océano "
                        "Pacífico, en el extremo de una amplia península que separa la desembocadura del río Tuira ("
                        "sinuoso estuario llamado golfo de San Miguel) de la recogida bahía o ensenada de Garachiné.",
                        "\u0085 1 Noche\n"
                        "\u0085 Almuerzo\n"
                        ),
                   Zona("Yaviza", 700,
                        "Está al final de la Carretera Panamericana, allí están los restos del fuerte español que "
                        "protegió la entrada a las minas de oro de cana y Rió Turquesa.",
                        "\u0085 1 Noche\n"
                        "\u0085 Almuerzo\n"
                        ),
                   Zona("Meteti", 650,
                        "Metetí es un corregimiento de la provincia de Darién de Panamá  Es una de las ciudades más "
                        "importante de esta provincia, siendo uno de los nueve corregimientos del distrito de "
                        "Pinogana y que cuenta según el Censo realizado en 2010 con una población de 7,976 habitantes",
                        "\u0085 1 Noche\n"
                        "\u0085 Almuerzo\n"
                        )
               ]),
        Region(2, "Ngöbe-Buglé",
               "Esta comarca fue creada en 1997 a partir del territorio de Bocas del Toro, Chiriquí y Veraguas. Su "
               "capital es Llano Tugrí (o Buabïti). El término Ngäbe-Buglé, está formado a partir del término ngäbere "
               "Ngäbe que a su vez proviene de los términos Ngä, 'personas, gente o nacer', y Be, 'ver, "
               "sentir o existir'. De hecho Ngäbe se puede traducir como 'nuestra gente' y es empleado como "
               "referencia a uno de los grupos étnicos que habitan la comarca.",
               [
                   Zona("Cascada La Tulivieja", 250,
                        "Este salto se encuentra ubicado en la comunidad de Soloy. Esta misteriosa cascada se forma "
                        "de las uniones de las quebradas Las Lajas y Magdalena",
                        "\u0085 1 Noche\n"
                        "\u0085 Una bruja?\n"
                        ),
                   Zona("Cascada Qui-Qui", 400,
                        "A una hora de camino, desde que aborda la chiva de Soloy a Cerro Banco, dentro del área "
                        "comarcal Ngäbe Buglé, se esconde una hermosa casada. ‘Kiki' también es conocida como el "
                        "chorro de ‘La Maestra' debido a que en ese lugar pereció una maestra muy querida por los "
                        "lugareños.",
                        "\u0085 Agua\n"
                        "\u0085 Almuerzo\n"
                        )
               ]),
        Region(2, "Guna Yala",
               "La comarca Guna Yala es una larga y angosta franja de paraíso tropical que se extiende por 5,"
               "571 kilómetros cuadrados a lo largo de la costa del Caribe panameño y que además cuenta más de 365 "
               "islas y playas de blanca arena que constituyen el archipiélago, entre la selva tropical que abunda en "
               "tierra firme y los arrecifes de coral en su línea costera. Se trata de un pueblo tranquilo, "
               "que mantiene la identidad cultural de su etnia",
               [
                   Zona("Archipiélago de San Blas", 400,
                        "Es un conjunto de más de 365 pequeñas islas e islotes pertenecientes a Panamá situadas "
                        "frente a la costa norte del Istmo, al este del Canal de Panamá, de las que solamente unas 80 "
                        "están habitadas. Es el hogar de los indígenas Guna, que forman parte de la comarca Guna Yala "
                        "a lo largo de la costa caribeña de Panamá",
                        "\u0085 Visitar la Cultura Guna \n"
                        "\u0085 Snorkeling \n"
                        )
               ]),
        Region(2, "Emberá",
               "Una comarca indígena de Panamá. Fue creada en 1983 a partir de dos enclaves ubicados en la provincia "
               "de Darién, específicamente de los distritos de Chepigana y Pinogana. Su capital es Unión Chocó.",
               [
                   Zona("Sambú", 1000,
                        "Las coloridas casas de Sambú, su gastronomía antillana-darienita, y la hospitalidad de su "
                        "gente, son solo una parte de su propuesta turística. Es un pintoresco pueblo donde conviven "
                        "en paz negros de abolengo antillano, latinos interioranos, e indígenas de la etnia "
                        "Emberá-Wounnan. Una vez instalado en Sambú, el visitante puede contratar viajes en piraguas "
                        "o en bote a motor para conocer comunidades como Trampa, Xuruco, Wira, Pavarandó, entre otras",
                        "\u0085 1 Noche\n"
                        "\u0085 Lagartos\n"
                        )
               ])
    ]


def get_regiones_list():
    return regiones
