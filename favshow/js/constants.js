function makeid(length) {
    var result           = '';
    var characters       = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    var charactersLength = characters.length;
    for ( var i = 0; i < length; i++ ) {
       result += characters.charAt(Math.floor(Math.random() * charactersLength));
    }
    log("Usercode created: " + result)
    return result;
 }

function userLoad(){
    var usercode = load("usercode");
    log("User loaded: " + usercode);
    if (usercode == null) {
        usercode = makeid(6);
        var request = new XMLHttpRequest();
                request.onreadystatechange = function() {
                        if (request.readyState !== XMLHttpRequest.DONE)
                            return;
                        if (request.status && request.status === 201) {
                            log("User created on server");
                        } else
                            log("ResponseError ", request.status);
                    }
        var url = "http://35.228.3.191:9090/api/appusers/" + usercode;
        log(url);
        request.open("POST", url, true);
        request.send();
        save("usercode", usercode);
        log("New user created: " + usercode);
    }
    return usercode;
}

function loadWaitlist(){
    var waitlist = load("waitlist");
    log("Waitlist: " + waitlist);
    if (waitlist == null) {
        waitlist = "";
        save("waitlist", waitlist);
        log("New waitlist created: " + load("waitlist"));
    }
}

this.usercode = userLoad();

this.loadWaitlist = loadWaitlist();

this.categories = [{ title: "СЕЙЧАС", url: "http://35.228.3.191:9090/api/now" },
                    { title: "ЖДУ", url: "http://35.228.3.191:9090/api/waitlists/" + this.usercode },
                    { title: "FX", url: "http://35.228.3.191:9090/api/services/fx" },
                   { title: "NETFLIX", url: "http://35.228.3.191:9090/api/services/netflix" },
                   { title: "AMC", url: "http://35.228.3.191:9090/api/services/amc" },
                   { title: "HBO-GO", url: "http://35.228.3.191:9090/api/services/hbo" },
                   { title: "AMAZON", url: "http://35.228.3.191:9090/api/services/amazon" },
                   { title: "CBS", url: "http://35.228.3.191:9090/api/services/cbs" },
                   { title: "SHOWTIME", url: "http://35.228.3.191:9090/api/services/showtime" },
                   { title: "DISNEY", url: "http://35.228.3.191:9090/api/services/disney" },
                   { title: "APPLE", url: "http://35.228.3.191:9090/api/services/apple-tv" },
                   { title: "CW", url: "http://35.228.3.191:9090/api/services/the-cw" },
                   { title: "ABC", url: "http://35.228.3.191:9090/api/services/abc" },
                   { title: "SYFY", url: "http://35.228.3.191:9090/api/services/syfy" },
                   { title: "BBC", url: "http://35.228.3.191:9090/api/services/bbc" },
                   { title: "FOX", url: "http://35.228.3.191:9090/api/services/fox" },
                   { title: "HULU", url: "http://35.228.3.191:9090/api/services/hulu" }];

this.colors = {"active" : "#295A9F",
               "inactive" : "#4B82BC",
                "uptextcolor" : "#000000"};

this.poster = {"width"  : 172,
               "height" : 264};

this.tvChannel = {"width"  : 24,
               "height" : 24};

this.menuWidth = 256;

this.inactiveOpacity = 0.5;

this.animationDuration = 150;

this.margin = 60;

this.telegramButton = "apps/favshow/resources/telegram_logo.png";

this.googleplayButton = "apps/favshow/resources/googleplay-logo.png";

this.googleplayImage = "apps/favshow/resources/googleplay.png";

this.telegramImage = "apps/favshow/resources/telegram.png";

this.defaultPoster = "apps/favshow/resources/catalog_default.png";

this.advertise = "apps/favshow/resources/advertise2.png";

this.defaultPoster172x264 = "apps/favshow/resources/catalog_default_172x264.png";

this.defaultAdvertImage = "apps/favshow/resources/advert_default.png";

this.defaultBackground = "apps/favshow/resources/defBackground.png";

this.amcBackground = "apps/favshow/resources/amcBackground.png";

this.fxBackground = "apps/favshow/resources/fxBackground.png";

this.netflixBackground = "apps/favshow/resources/netflixBackground.png";

this.amazonBackground = "apps/favshow/resources/amazonBackground.png";

this.hbogoBackground = "apps/favshow/resources/hbogoBackground.png";

this.appleBackground = "apps/favshow/resources/appleBackground.png";

this.showtimeBackground = "apps/favshow/resources/showtimeBackground.png";

this.abcBackground = "apps/favshow/resources/abcBackground.png";

this.syfyBackground = "apps/favshow/resources/syfyBackground.png";

this.cwBackground = "apps/favshow/resources/cwBackground.png";

this.cbsBackground = "apps/favshow/resources/cbsBackground.png";

this.bbcBackground = "apps/favshow/resources/bbcBackground.png";

this.othersBackground = "apps/favshow/resources/othersBackground.png";

this.disneyBackground = "apps/favshow/resources/disneyBackground.png";

this.huluBackground = "apps/favshow/resources/huluBackground.png";
