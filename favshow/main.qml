import "CatalogPage.qml";
import "CatalogView.qml";
import "CategoryMenu.qml";
import "FavshowPlayer.qml";
import "GooglePlayView.qml";
import "TelegramView.qml";

import controls.Spinner;

import "js/constants.js" as constants;

Application {
    id: favshow;

    color: "#FFFFFF";

    property alias background: backgroundImage.source;

    Image {
        id: backgroundImage;

        anchors.fill: favshow;
        fillMode: Stretch;
    }

    Item {
        id: menuItem;

        width: constants.menuWidth;

        anchors.left: mainWindow.left;
        anchors.top: mainWindow.top;
        anchors.bottom: mainWindow.bottom;

        Image {
            id: favshowImage;

            anchors.top: parent.top;
            anchors.left: parent.left;
            anchors.leftMargin: 60;
            anchors.topMargin: 12;

            source: "apps/favshow/resources/menu.png";

            fillMode: PreserveAspectFit;
        }
        
        Image {
            id: googleplayButton;
            focus: true;
            anchors.top: favshowImage.bottom;
            anchors.left: parent.left;
            anchors.topMargin: 4;
            anchors.bottomMargin: 36;
            anchors.leftMargin: 64;

            width:  googleplayButton.activeFocus ? 48 : 36;
            height: googleplayButton.activeFocus ? 48 : 36;

            source: constants.googleplayButton;

            fillMode: PreserveAspectFit;

            onDownPressed: {
                googlePlayView.visible = false;
                categoryMenu.setFocus();
            }

            onRightPressed: {
                googlePlayView.visible = false;
                telegramButton.setFocus();
            }

            onKeyPressed: {
                if (key === "Select") {
                    if (googlePlayView.visible != true) {
                        googlePlayView.visible = true;
                    }
                    else {
                        googlePlayView.visible = false;
                    }
                }
            }

            Behavior on width  { animation: Animation { duration: constants.animationDuration; } }
            Behavior on height { animation: Animation { duration: constants.animationDuration; } }
        }

        Image {
            id: telegramButton;
            focus: true;
            anchors.top: favshowImage.bottom;
            anchors.left: googleplayButton.right;
            anchors.topMargin: 4;
            anchors.leftMargin: 12;
            anchors.bottomMargin: 36;

            width:  telegramButton.activeFocus ? 48 : 36;
            height: telegramButton.activeFocus ? 48 : 36;

            source: constants.telegramButton;

            fillMode: PreserveAspectFit;

            onKeyPressed: {
                if (key === "Select") {
                    if (telegramView.visible != true) {
                        telegramView.visible = true;
                    }
                    else {
                        telegramView.visible = false;
                    }
                }
            }

            onLeftPressed: {
                telegramView.visible = false;
                googleplayButton.setFocus();
            }

            onRightPressed: {
                telegramView.visible = false;
                catalogView.setFocus();
            }

            onDownPressed: {
                telegramView.visible = false;
                categoryMenu.setFocus();
            }

            Behavior on width  { animation: Animation { duration: constants.animationDuration; } }
            Behavior on height { animation: Animation { duration: constants.animationDuration; } }
        }

        

        CategoryMenu {
            id: categoryMenu;

            anchors.top: favshowImage.bottom;
            anchors.left: parent.left;
            anchors.right: parent.right;
            anchors.bottom: parent.bottom;
            anchors.margins: constants.margin;

            spacing: constants.margin / 2;

            color: activeFocus ? "#60a0e0" : "#000000";

            opacity: activeFocus ? 1.0 : 0.7;

            onUpPressed: {
                googleplayButton.setFocus();
            }

            onKeyPressed: {
                if (key === "Select" || key === "Right") {
                    catalogPage.visible = false;
                    catalogView.visible = true;
                    catalogTextUp.visible = true;
                    var currentCategory = model.get(categoryMenu.currentIndex);
                    catalogView.loadCatalog(currentCategory.url);
                    catalogTextUp.source = "apps/favshow/resources/" + currentCategory.title + ".png";
                    log(catalogTextUp.source);
                    log("Category select - ", currentCategory.title);
                }
            }
        }
    }

    CatalogPage {
        id: catalogPage;

        anchors.top: mainWindow.top;
        anchors.left: menuItem.right;
        anchors.right: mainWindow.right;
        anchors.bottom: mainWindow.bottom;
        anchors.margins: constants.margin;

        opacity: activeFocus ? 1.0 : constants.inactiveOpacity;

        visible: false;

        onWatch: {
            this.visible = false;
            menuItem.visible = false;
            favshowPlayer.visible = true;
            favshowPlayer.title = catalogView.model.get(catalogView.currentIndex).title;
            log("Start watching URL - ", catalogView.model.get(catalogView.currentIndex).id);
            favshowPlayer.playVideoById(catalogView.model.get(catalogView.currentIndex).trailer);
        }

        onUpPressed: {
                telegramButton.setFocus();
            }

        onLeftPressed: {
            categoryMenu.setFocus();
        }

        onClosed: {
            this.visible = false;
            backgroundImage.source = null;
            favshowPlayer.abort();
            catalogView.visible = true;
            catalogTextUp.visible = true;
            catalogView.setFocus();
        }
    }

    Image {
        id: catalogTextUp;
        anchors.top: mainWindow.top;
        anchors.left: menuItem.right;
        anchors.topMargin: 12;
        anchors.leftMargin: 60;

        width: 128;
        height: 64;
        source: "apps/favshow/resources/СЕЙЧАС.png";
    }

    CatalogView {
        id: catalogView;

        anchors.top: catalogTextUp.bottom;
        anchors.left: menuItem.right;
        anchors.right: mainWindow.right;
        anchors.bottom: mainWindow.bottom;
        anchors.topMargin: 20;
        anchors.leftMargin: constants.margin;
        anchors.rightMargin: constants.margin;
        anchors.bottomMargin: constants.margin;

        opacity: activeFocus ? 1.0 : constants.inactiveOpacity;

        keyNavigationWraps: false;

        onSelectPressed: {
            this.visible = false;
            catalogTextUp.visible = false;

            var currentCatalogItem = model.get(catalogView.currentIndex);
            catalogPage.id = currentCatalogItem.id;
            catalogPage.title = currentCatalogItem.title;
            catalogPage.titleSeason = currentCatalogItem.titleSeason;
            catalogPage.favshowRating = currentCatalogItem.favshowRating;
            catalogPage.flagStatus = currentCatalogItem.flagStatus;
            catalogPage.actors = currentCatalogItem.actors;
            catalogPage.numSeries = currentCatalogItem.numSeries;
            catalogPage.poster = currentCatalogItem.poster;
            catalogPage.duration = currentCatalogItem.duration;
            catalogPage.whenontv = currentCatalogItem.whenontv;
            favshow.background = currentCatalogItem.background;
            catalogPage.restrict = currentCatalogItem.restrict;
            catalogPage.description = currentCatalogItem.description;
            catalogPage.releaseDate = currentCatalogItem.releaseDate;
            catalogPage.genre = currentCatalogItem.genre;
            catalogPage.country = currentCatalogItem.country;
            catalogPage.advertise = currentCatalogItem.advertise;
            catalogPage.serList = currentCatalogItem.serList;
            catalogPage.serDur = currentCatalogItem.serDur;
            catalogPage.tvChannel = currentCatalogItem.tvChannel;
            backgroundImage.visible = true;
            catalogPage.visible = true;
        }

        onLeftPressed: {
            categoryMenu.setFocus();
        }

        onKeyPressed: {
            if (key === "Red")
                categoryMenu.setFocus();
        }
    }

    Spinner {
        id: loadingCatalogSpinner;

        anchors.centerIn: mainWindow;

        visible: catalogView.loading;
    }

    GooglePlayView {
        id: googlePlayView;

        visible: false;

        anchors.centerIn: mainWindow;
    }

    TelegramView {
        id: telegramView;

        visible: false;

        anchors.centerIn: mainWindow;
    }

    FavshowPlayer {
        id: favshowPlayer;

        anchors.fill: mainWindow;

        visible: false;

        onBackPressed: {
            log("On Back Pressed - Player Shut Down");
            favshowPlayer.abort();
            this.visible = false;
            log("Go to Catalog Page");
            menuItem.visible = true;
            catalogPage.visible = true;
            catalogPage.setFocus();
        }

        onFinished: {
            favshow.hidePlayer();
        }
    }

    onBackPressed: {
        viewsFinder.closeApp();
    }

    onCompleted: {
        catalogView.loadCatalog(constants.categories[0].url);
    }

    onVisibleChanged: {
        viewsFinder.ignoreScreenSaverForApp("favshow", this.visible);
        favshowPlayer.abort();

        if(favshowPlayer.visible) {
            favshow.hidePlayer();
        }
    }

    function hidePlayer() {
        favshowPlayer.visible = false;
        menuItem.visible = true;
        catalogPage.visible = true;
        catalogPage.setFocus();
    }
}
