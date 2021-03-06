import "js/constants.js" as constants;

Rectangle {
    id: catalogDelegate;

    width: constants.poster["width"]  + (constants.margin / 3);
    height: constants.poster["height"] + (constants.margin / 3);

    opacity: activeFocus ? 1.0 : 0.8;

    color:"#FFFFFF";

    focus: true;

    Image {
        id: posterDefaultImage;

		width:  catalogDelegate.activeFocus ? constants.poster["width"]  + (constants.margin / 3)  : constants.poster["width"];
		height: catalogDelegate.activeFocus ? constants.poster["height"] + (constants.margin / 3)  : constants.poster["height"];

        anchors.centerIn: parent;

        visible: posterImage.status !== ui.Image.Ready;

        source: constants.defaultPoster;

        fillMode: PreserveAspectFit;

        Behavior on width  { animation: Animation { duration: constants.animationDuration; } }
        Behavior on height { animation: Animation { duration: constants.animationDuration; } }
    }

    Image {
        id: posterImage;

		width:  catalogDelegate.activeFocus ? constants.poster["width"]  + (constants.margin / 3)  : constants.poster["width"];
		height: catalogDelegate.activeFocus ? constants.poster["height"] + (constants.margin / 3)  : constants.poster["height"];

        anchors.centerIn: parent;

        registerInCacheSystem: false;

        source: model.poster;

        fillMode: PreserveAspectFit;

        Behavior on width  { animation: Animation { duration: constants.animationDuration; } }
        Behavior on height { animation: Animation { duration: constants.animationDuration; } }
    }

    Image {
        id: chanImage;

		width: constants.tvChannel["width"];
		height: constants.tvChannel["height"];

        anchors.centerIn: parent;

        registerInCacheSystem: false;

        source: "apps/favshow/resources/" + model.tvChannel + ".png";

        fillMode: PreserveAspectFit;

        Behavior on width  { animation: Animation { duration: constants.animationDuration; } }
        Behavior on height { animation: Animation { duration: constants.animationDuration; } }
    }
}

