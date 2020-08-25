import "js/constants.js" as constants;

Item {
    id: googlePlayView;

    Image {
        id: googlePlayImage;
        anchors.centerIn: mainWindow;

        width: mainWindow.width - 200;
        height: mainWindow.height - 200;

        source: constants.googleplayImage;
        fillMode: PreserveAspectFit;
    }

    BodyText {
            id: googlePlayText;

            anchors.centerIn: googlePlayImage;
            font.bold: true;

            text: "Ваш код: " + constants.usercode;

            color: "#ffffff";
        }
}
