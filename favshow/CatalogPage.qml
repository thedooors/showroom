import controls.Button;

import "js/constants.js" as constants;

Item {
    id: catalogPage;

    signal closed;
    signal watch;

    property alias title: titleText.text;
    property alias poster: posterImage.source;
    property alias year: yearText.text;
    property alias description: descriptionText.text;
    property string duration;
    property string restrict;
    property string favshowRating;
    property string kpRating;
    property string imdbRating;
    property string whenontv;
    property string season;

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

    SubheadText {
        id: titleText;

        anchors.top: catalogPage.top;
        anchors.left: posterDefaultImage.visible ? posterDefaultImage.right : posterImage.right;
        anchors.leftMargin: constants.margin / 2;
        anchors.right: parent.right;

        color: "#000000";

        wrapMode: ui.Text.Wrap;
    }

    BodyText {
        id: yearText;

        anchors.top: titleText.bottom;
        anchors.left: posterDefaultImage.visible ? posterDefaultImage.right : posterImage.right;
        anchors.leftMargin: constants.margin / 2;

        color: "#000000";
    }

    Image {
        id: restrictText;

        anchors.top: titleText.bottom;
        anchors.left: yearText.right;
        anchors.leftMargin: constants.margin / 4;

        width: 32;
        height: 32;
        source: "apps/favshow/resources/" + catalogPage.restrict + ".png";
    }

    Image {
        id: durationText;

        anchors.top: titleText.bottom;
        anchors.left: restrictText.right;
        anchors.leftMargin: constants.margin / 4;

        width: 160;
        height: 32;
        source: "apps/favshow/resources/" + catalogPage.favshowRating + ".png";
    }

    Item {
        id: ratingItem;

        anchors.top: yearText.bottom;
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
            source: "apps/favshow/resources/" + catalogPage.kpRating + ".png";
        }

        SecondaryText {
            id: kpRatingText;

            anchors.left: favshowRatingText.right;
            anchors.leftMargin: constants.margin / 2;

            text: "Ep: " + catalogPage.season;

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
        text: "'" + yearText.text + "' в ожидании";
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
            notifyWaiting.addNotify();
        }
    }

    ScrollingText {
        id: actorsText;

        anchors.top: watchButton.bottom;
        anchors.topMargin: constants.margin / 2;
        anchors.left: posterDefaultImage.visible ? posterDefaultImage.right : posterImage.right;
        anchors.leftMargin: constants.margin / 2;
        anchors.right: catalogPage.right;

        opacity: activeFocus ? 1.0 : constants.inactiveOpacity;

        color: "#000000";

        font: secondaryFont;

        height: 35;

        text: catalogPage.whenontv;

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
        anchors.topMargin: constants.margin / 2;
        anchors.left: posterDefaultImage.visible ? posterDefaultImage.right : posterImage.right;
        anchors.leftMargin: constants.margin / 2;
        anchors.right: catalogPage.right;

        opacity: activeFocus ? 1.0 : constants.inactiveOpacity;

        color: "#000000";

        font: secondaryFont;

        height: 35;

        text: catalogPage.imdbRating;

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
        anchors.topMargin: constants.margin / 2;
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
