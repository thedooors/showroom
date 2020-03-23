
import controls.Player;

import "js/constants.js" as constants;

Player {
    id: favshowPlayer;

    focus: true;

    isFullscreen: true;

    function playVideoById(urlid) {
        log("Start play URL");
        favshowPlayer.playUrl(urlid);
        favshowPlayer.setFocus();
        log("Focused");
    }
}
