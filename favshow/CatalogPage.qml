import controls.Button;

import "js/constants.js" as constants;

Item {
    id: catalogPage;

    signal closed;
    signal watch;

    property alias title: titleText.text;
    property alias poster: posterImage.source;
    property alias titleSeason: titleSeasonText.text;
    property alias description: descriptionText.text;
    property string id;
    property string trailer;
    property string restrict;
    property string favshowRating;
    property string flagStatus;
    property string actors;
    property string whenontv;
    property string numSeries;
    property string genre;
    property string serDur;
    property string tvChannel;
    property string advertise;
    property string releaseDate;
    property string country;

    Image {
        id: posterDefaultImage;

        anchors.top: catalogPage.top;
        anchors.left: catalogPage.left;

        width: 172;
        height: 264;

        visible: posterImage.status !== ui.Image.Ready;

        source: constants.defaultPoster172x264;
        sourceSize.width: 172;
        sourceSize.height: 264;
        fillMode: Stretch;
    }

    Image {
        id: posterImage;

        anchors.top: catalogPage.top;
        anchors.left: catalogPage.left;
        
        width: 172;
        height: 264;
        sourceSize.width: 172;
        sourceSize.height: 264;
        fillMode: Stretch;
    }

    Image {
        id: advertiseImage;

        anchors.top: posterImage.bottom;
        anchors.left: catalogPage.left;
        anchors.topMargin: 8;
        
        width: 172;
        height: 83;
        source: "apps/favshow/resources/" + catalogPage.advertise + ".png";
        fillMode: Stretch;
    }

    SecondaryText {
            id: releaseDateText;

            anchors.top: advertiseImage.bottom;
            anchors.left: catalogPage.left;
            anchors.topMargin: 4;

            width: 172;

            text: "Релиз: " + catalogPage.releaseDate;

            color: "#858585";
        }
    
    SecondaryText {
            id: countryText;

            anchors.top: releaseDateText.bottom;
            anchors.left: catalogPage.left;
            anchors.topMargin: 4;

            width: 172;

            text: "Страна: " + catalogPage.country;

            color: "#858585";
        }

    SubheadText {
        id: titleText;

        anchors.top: catalogPage.top;
        anchors.left: posterDefaultImage.visible ? posterDefaultImage.right : posterImage.right;
        anchors.leftMargin: constants.margin / 2;
        anchors.right: parent.right;

        color: "#000000";

        wrapMode: ui.Text.Wrap;
    }

    Image {
        id: tvchannelImage;

        anchors.top: catalogPage.top;
        anchors.left: restrictText.left;

        width: 32;
        height: 32;
        source: "apps/favshow/resources/" + catalogPage.tvChannel + ".png";
    }

    BodyText {
        id: titleSeasonText;

        anchors.top: titleText.bottom;
        anchors.left: posterDefaultImage.visible ? posterDefaultImage.right : posterImage.right;
        anchors.leftMargin: constants.margin / 2;

        color: "#000000";
    }

    Image {
        id: restrictText;

        anchors.top: titleText.bottom;
        anchors.left: titleSeasonText.right;
        anchors.leftMargin: constants.margin / 4;

        width: 32;
        height: 32;
        source: "apps/favshow/resources/" + catalogPage.restrict + ".png";
    }

    Image {
        id: trailerText;

        anchors.top: titleText.bottom;
        anchors.left: restrictText.right;
        anchors.leftMargin: constants.margin / 4;

        width: 160;
        height: 32;
        source: "apps/favshow/resources/" + catalogPage.favshowRating + ".png";
    }

    Item {
        id: ratingItem;

        anchors.top: titleSeasonText.bottom;
        anchors.topMargin: constants.margin / 4;
        anchors.left: posterDefaultImage.visible ? posterDefaultImage.right : posterImage.right;
        anchors.leftMargin: constants.margin / 2;
        anchors.right: parent.right;

        height: favshowRatingText.height;

        Image {
            id: favshowRatingText;

            anchors.left: parent.left;

            width: 160;
            height: 32;
            source: "apps/favshow/resources/" + catalogPage.flagStatus + ".png";
        }

        SecondaryText {
            id: flagStatusText;

            anchors.left: favshowRatingText.right;
            anchors.leftMargin: constants.margin / 2;

            text: catalogPage.numSeries + " серий по " + catalogPage.serDur;

            color: "#000000";
        }

        SecondaryText {
            id: genreText;

            anchors.left: flagStatusText.right;
            anchors.leftMargin: constants.margin / 2;

            text: "Жанр: " + catalogPage.genre;

            color: "#000000";
        }
    }

    Button {
        id: watchButton;

        anchors.top: ratingItem.bottom;
        anchors.topMargin: constants.margin / 2;
        anchors.left: posterDefaultImage.visible ? posterDefaultImage.right : posterImage.right;
        anchors.leftMargin: constants.margin / 2;

        opacity: activeFocus ? 1.0 : constants.inactiveOpacity;

        color: activeFocus ? constants.colors["active"] : constants.colors["inactive"];

        text: "Трейлер";

        onDownPressed: {
            actorsText.setFocus();
        }

        onRightPressed: {
            waitingButton.setFocus();
        }

        onSelectPressed: {
            log("watch button pressed");
            catalogPage.watch();
        }
    }

    NotificatorManager {
        id: notifyWaiting;
        text: "'" + titleText.text + "' в ожидании";
    }

    NotificatorManager {
        id: notifyAlreadyExist;
        text: "'" + titleText.text + "' уже в списке ожидания";
    }

    NotificatorManager {
        id: notifyAlreadyOnTV;
        text: "Отмена.'" + titleText.text + "' уже на ТВ";
    }

    Button {
        id: waitingButton;

        anchors.top: ratingItem.bottom;
        anchors.topMargin: constants.margin / 2;
        anchors.left: watchButton.right;
        anchors.leftMargin: constants.margin / 2;

        opacity: activeFocus ? 1.0 : constants.inactiveOpacity;

        color: activeFocus ? constants.colors["active"] : constants.colors["inactive"];

        text: "Жду";

        onDownPressed: {
            actorsText.setFocus();
        }

        onLeftPressed: {
            watchButton.setFocus();
        }

        onSelectPressed: {
            log("wait button pressed");
            var waitlist = load("waitlist");
            var waitlistArray;
            if (waitlist === "") {
                waitlistArray = new Array();
            }
            else{
                waitlistArray = waitlist.split(",");
            }
            if (waitlistArray.indexOf(catalogPage.id) != -1){
                notifyAlreadyExist.addNotify();
            }
            else if (catalogPage.flagStatus == "NOW"){
                notifyAlreadyOnTV.addNotify();
            }
            else {
                waitlistArray.push(catalogPage.id);
                var waitlistString = waitlistArray.join(",");
                save("waitlist", waitlistString);
                log(load("waitlist"));
                var request = new XMLHttpRequest();
                request.onreadystatechange = function() {
                        if (request.readyState !== XMLHttpRequest.DONE)
                            return;
                        if (request.status && request.status === 201) {
                            log("Waitlist updated on server");
                        } else
                            log("ResponseError ", request.status);
                    }
                
                var url = "http://35.228.3.191:9090/api/waitlists/" + constants.usercode + "/" + waitlistString;
                log(url);
                request.open("POST", url, true);
                request.send();
                notifyWaiting.addNotify();
            }
        }
    }

    ScrollingText {
        id: actorsText;

        anchors.top: watchButton.bottom;
        anchors.topMargin: 15;
        anchors.left: posterDefaultImage.visible ? posterDefaultImage.right : posterImage.right;
        anchors.leftMargin: constants.margin / 2;
        anchors.right: catalogPage.right;

        opacity: activeFocus ? 1.0 : constants.inactiveOpacity;

        color: "#000000";

        font: secondaryFont;

        height: 35;

        text: "Расписание: " + catalogPage.whenontv;

        onUpPressed: {
            watchButton.setFocus();
        }

        onDownPressed: {
            whenText.setFocus();
        }
    }

    ScrollingText {
        id: whenText;

        anchors.top: actorsText.bottom;
        anchors.topMargin: 15;
        anchors.left: posterDefaultImage.visible ? posterDefaultImage.right : posterImage.right;
        anchors.leftMargin: constants.margin / 2;
        anchors.right: catalogPage.right;

        opacity: activeFocus ? 1.0 : constants.inactiveOpacity;

        color: "#000000";

        font: secondaryFont;

        height: 35;

        text: "В ролях: " + catalogPage.actors;

        onUpPressed: {
            actorsText.setFocus();
        }

        onDownPressed: {
            descriptionText.setFocus();
        }
    }

    ScrollingText {
        id: descriptionText;

        anchors.top: whenText.bottom;
        anchors.topMargin: 15;
        anchors.left: posterDefaultImage.visible ? posterDefaultImage.right : posterImage.right;
        anchors.leftMargin: constants.margin / 2;
        anchors.right: catalogPage.right;
        anchors.bottom: catalogPage.bottom;

        opacity: activeFocus ? 1.0 : constants.inactiveOpacity;

        color: "#000000";

        font: secondaryFont;

        onUpPressed: {
            whenText.setFocus();
        }
    }

    onVisibleChanged: {
        watchButton.setFocus();
    }

    onBackPressed: {
        closed();
    }
}
