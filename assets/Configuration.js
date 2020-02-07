/* -*- Mode: rjsx -*- */

/*******************************************
 * Copyright (2018)
 *  Marcus Dillavou <line72@line72.net>
 *  http://line72.net
 *
 * Montclair:
 *  https://github.com/line72/montclair
 *  https://montclair.line72.net
 *
 * Licensed Under the GPLv3
 *******************************************/

import GTFSRTParser from './GTFSRTParser';

class Configuration {
    constructor() {
        // Columbus, OH
        this.center = [39.9622601, -83.0007065];

        this.agencies = [
            {
                name: 'Routes',
                parser: new GTFSRTParser('montclair', '/columbus-gtfs.zip',
                                         'https://columbusoh.gotransitapp.com/api/no.php/Vehicle/VehiclePositions.pb',
                                         'https://columbusoh.gotransitapp.com/api/no.php/TripUpdate/TripUpdates.pb')
            }
        ];
    }
}

export default Configuration;
