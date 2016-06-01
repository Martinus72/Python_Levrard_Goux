$(document).ready(function() {

  /**
	 * Initialisation de la map google
	 */
  map = new GMaps({ /*crÃ©ation de la map, avec comme centre, le centre de la ville choisie*/
     div: '#maps',
     lat:  47.1302,
     lng: 1.3312,
     width: '100%',
     height: '590px',
     zoom: 7,
     zoomControl: true,
     zoomControlOpt: {
         style: 'SMALL',
         position: 'TOP_LEFT'
     },
     panControl: false
    });

    // Ajout du marker
    map.addMarker({
      lat: parseFloat(latitude),
      lng: parseFloat(longitude),
    });

    // Changemet des propriétés de la map pour se centrer sur la ville et avoir un zoom correct
      map.setCenter(parseFloat(latitude),parseFloat(longitude));
      map.setZoom(15);

});
