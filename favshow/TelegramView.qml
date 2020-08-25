import "js/constants.js" as constants;

Item {
    id: telegramView;

    Image {
        id: telegramImage;
        anchors.centerIn: mainWindow;

        width: mainWindow.width - 200;
        height: mainWindow.height - 200;

        source: constants.telegramImage;
        fillMode: PreserveAspectFit;
    }

    BodyText {
            id: telegramText;

            anchors.centerIn:telegramImage;
            font.bold: true;

            text: "Ваш код: " + constants.usercode;

            color: "#ffffff";
        }
}
