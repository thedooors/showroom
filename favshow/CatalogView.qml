import "CatalogDelegate.qml";

import "js/constants.js" as constants;

GridView {
    id: catalogView;

    property bool loading: false;

    cellWidth: constants.poster["width"] + (constants.margin / 3);
    cellHeight: constants.poster["height"] + (constants.margin / 3);

    visible: !loading;

    focus: true;
    clip: true;

    delegate: CatalogDelegate {}
    model: ListModel { id: catalogModel; }

    function loadCatalog(url) {
        catalogView.loading = true;
        var request = new XMLHttpRequest();
        request.onreadystatechange = function() {
            if (request.readyState !== XMLHttpRequest.DONE)
                return;

            if (request.status && request.status === 200) {
                log("response was received");
                //log(request.responseText);
                catalogModel.reset();

                var catalog = JSON.parse(request.responseText);
                catalog.forEach(function (catalogItem) {
                    catalogModel.append( {  id: catalogItem["content_id"],
                                            title: catalogItem["title"],
                                            background: catalogView.extractBackgroundImage(catalogItem),
                                            titleSeason: catalogItem["title_season"] ? catalogItem["title_season"] : "-",
                                            restrict: catalogItem["restricty"] ? catalogItem["restricty"] : "12",
                                            trailer: catalogItem["trailer"] ? catalogItem["trailer"] : "http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerEscapes.mp4",
                                            favshowRating: catalogItem["kp_rating"] ? catalogItem["kp_rating"] : "3",
                                            flagStatus: catalogItem["flag_status"] ? catalogItem["flag_status"] : "FREEZE",
                                            actors: catalogItem["actors"] ? catalogItem["actors"] : "-",
                                            description: catalogItem["description"] ? catalogItem["description"] : "",
                                            whenontv: catalogItem["whenontv"] ? catalogItem["whenontv"] : "",
                                            numSeries: catalogItem["num_of_series"] ? catalogItem["num_of_series"] : "-",
                                            poster: catalogItem["poster"] ? catalogItem["poster"] : constants.defaultPoster,
                                            releaseDate: catalogItem["release_date"] ? catalogItem["release_date"] : "2020",
                                            genre: catalogItem["genre"] ? catalogItem["genre"] : "-",
                                            country: catalogItem["country"] ? catalogItem["country"] : "США",
                                            advertise: catalogItem["advertise"] ? catalogItem["advertise"] : "advertise2",
                                            serDur: catalogItem["serial_duration"] ? catalogItem["serial_duration"] : "-",
                                            serList: catalogItem["series_list"] ? catalogItem["series_list"] : "",
                                            tvChannel: catalogItem["tv_channel"] ? catalogItem["tv_channel"] : "empty"} );
                });
                catalogView.loading = false;
                catalogView.setFocus();
                log("Catalog update");
            } else
                log("Error in catalog updating - ", request.status);
        }

        request.open("GET", url, true);
        request.send();
        log("Request sended");
    }

    function extractBackgroundImage(catalogItem) {
        var result = "";
        if (catalogItem.hasOwnProperty("selectservice")){
            if (catalogItem["selectservice"] == "AMC"){
                result = constants.amcBackground;
            }
            else if (catalogItem["selectservice"] == "NETFLIX"){
                result = constants.netflixBackground;
            }
            else if (catalogItem["selectservice"] == "HBO"){
                result = constants.hbogoBackground;
            }
            else if (catalogItem["selectservice"] == "AMAZON"){
                result = constants.amazonBackground;
            }
            else if (catalogItem["selectservice"] == "DISNEY"){
                result = constants.disneyBackground;
            }
            else if (catalogItem["selectservice"] == "APPLE-TV"){
                result = constants.appleBackground;
            }
            else if (catalogItem["selectservice"] == "FX"){
                result = constants.fxBackground;
            }
            else if (catalogItem["selectservice"] == "SHOWTIME"){
                result = constants.showtimeBackground;
            }
            else if (catalogItem["selectservice"] == "THE-CW"){
                result = constants.cwBackground;
            }
            else if (catalogItem["selectservice"] == "FOX"){
                result = constants.othersBackground;
            }
            else if (catalogItem["selectservice"] == "ABC"){
                result = constants.abcBackground;
            }
            else if (catalogItem["selectservice"] == "CBS"){
                result = constants.cbsBackground;
            }
            else if (catalogItem["selectservice"] == "SYFY"){
                result = constants.syfyBackground;
            }
            else if (catalogItem["selectservice"] == "СЕЙЧАС"){
                result = constants.netflixBackground;
            }
            else if (catalogItem["selectservice"] == "BBC"){
                result = constants.bbcBackground;
            }
            else {
                result = constants.huluBackground;
            }
        }
        else {
            result = constants.defaultBackground;
        }
        return result;
    }
}
