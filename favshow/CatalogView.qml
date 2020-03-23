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
                                            year: catalogItem["year"] ? catalogItem["year"] : "-",
                                            restrict: catalogItem["restrict"] ? catalogItem["restrict"] : "12",
                                            duration: catalogItem["duration"] ? catalogItem["duration"] : "http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerEscapes.mp4",
                                            favshowRating: catalogItem["rating"] ? catalogItem["rating"] : "3",
                                            kpRating: catalogItem["kp_rating"] ? catalogItem["kp_rating"] : "FREEZE",
                                            imdbRating: catalogItem["imdb_rating"] ? catalogItem["imdb_rating"] : "-",
                                            description: catalogItem["description"] ? catalogItem["description"] : "",
                                            whenontv: catalogItem["whenontv"] ? catalogItem["whenontv"] : "",
                                            season: catalogItem["season"] ? catalogItem["season"] : "S1E1",
                                            poster: catalogItem["poster"] ? catalogItem["poster"] : constants.defaultPoster } );
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
            else if (catalogItem["selectservice"] == "HBO-GO"){
                result = constants.hbogoBackground;
            }
            else if (catalogItem["selectservice"] == "AMAZON"){
                result = constants.amazonBackground;
            }
            else if (catalogItem["selectservice"] == "DISNEY"){
                result = constants.disneyBackground;
            }
            else if (catalogItem["selectservice"] == "APPLE"){
                result = constants.appleBackground;
            }
            else if (catalogItem["selectservice"] == "FX"){
                result = constants.fxBackground;
            }
            else if (catalogItem["selectservice"] == "SHOWTIME"){
                result = constants.showtimeBackground;
            }
            else if (catalogItem["selectservice"] == "CW"){
                result = constants.cwBackground;
            }
            else if (catalogItem["selectservice"] == "OTHERS"){
                result = constants.othersBackground;
            }
            else if (catalogItem["selectservice"] == "ABC"){
                result = constants.abcBackground;
            }
            else if (catalogItem["selectservice"] == "CBS"){
                result = constants.cbsBackground;
            }
            else if (catalogItem["selectservice"] == "SCY-FI"){
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
