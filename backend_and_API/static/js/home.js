// Пространство имен - для MVC
let ns = {};

// Создаю model для значений
ns.model = (function() {
    'use strict';

    let $event_pump = $('body');

    // Данные получвем посредством запросов к API. Описание запросов, обработка ошибок и сериализация
    return {
        'read': function() {
            let ajax_options = {
                type: 'GET',
                url: 'api/shows',
                accepts: 'application/json',
                dataType: 'json'
            };
            $.ajax(ajax_options)
            .done(function(data) {
                $event_pump.trigger('model_read_success', [data]);
            })
            .fail(function(xhr, textStatus, errorThrown) {
                $event_pump.trigger('model_error', [xhr, textStatus, errorThrown]);
            })
        },
        create: function(content) {
            let ajax_options = {
                type: 'POST',
                url: 'api/shows',
                accepts: 'application/json',
                contentType: 'application/json',
                dataType: 'json',
                data: JSON.stringify(content)
            };
            $.ajax(ajax_options)
            .done(function(data) {
                $event_pump.trigger('model_create_success', [data]);
            })
            .fail(function(xhr, textStatus, errorThrown) {
                $event_pump.trigger('model_error', [xhr, textStatus, errorThrown]);
            })
        },
        update: function(content) {
            let ajax_options = {
                type: 'PUT',
                url: `api/shows/${content.content_id}`,
                accepts: 'application/json',
                contentType: 'application/json',
                dataType: 'json',
                data: JSON.stringify(content)
            };
            $.ajax(ajax_options)
            .done(function(data) {
                $event_pump.trigger('model_update_success', [data]);
            })
            .fail(function(xhr, textStatus, errorThrown) {
                $event_pump.trigger('model_error', [xhr, textStatus, errorThrown]);
            })
        },
        'delete': function(content_id) {
            let ajax_options = {
                type: 'DELETE',
                url: `api/shows/${content_id}`,
                accepts: 'application/json',
                contentType: 'plain/text'
            };
            $.ajax(ajax_options)
            .done(function(data) {
                $event_pump.trigger('model_delete_success', [data]);
            })
            .fail(function(xhr, textStatus, errorThrown) {
                $event_pump.trigger('model_error', [xhr, textStatus, errorThrown]);
            })
        }
    };
}());

// Создаем view в ns - через jquery получаем значения в колонках
ns.view = (function() {
    'use strict';

    let $content_id = $('#content_id'),
        $title = $('#title'),
        $title_season = $('#title_season'),
        $restricty = $('#restricty'),
        $selectservice = $('#selectservice'),
        $num_of_series = $('#num_of_series'),
        $trailer = $('#trailer'),
        $kp_rating = $('#kp_rating'),
        $flag_status = $('#flag_status'),
        $actors = $('#actors'),
        $description = $('#description'),
        $advertise = $('#advertise'),
        $poster = $('#poster'),
        $whenontv = $('#whenontv'),
        $release_date = $('#release_date'),
        $country = $('#country'),
        $genre = $('#genre'),
        $serial_duration = $('#serial_duration'),
        $series_list = $('#series_list'),
        $tv_channel = $('#tv_channel'),
        $temp_col1 = $('#temp_col1'),
        $temp_col2 = $('#temp_col2');

    return {
        reset: function() {
            $content_id.val('');
            $title_season.val('');
            $title.val('').focus();
            $selectservice.val('FX');
            $restricty.val('18');
            $num_of_series.val('');
            $trailer.val('http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerJoyrides.mp4');
            $kp_rating.val('3');
            $flag_status.val('GO');
            $actors.val('');
            $description.val('');
            $advertise.val('advertise2');
            $poster.val('');
            $whenontv.val('');
            $release_date.val('2020');
            $country.val('USA');
            $genre.val('');
            $serial_duration.val('');
            $series_list.val('');
            $tv_channel.val('');
            $temp_col1.val('');
            $temp_col2.val('');
        },
        update_editor: function(content) {
            $content_id.val(content.content_id);
            $title_season.val(content.title_season);
            $title.val(content.title);
            $selectservice.val(content.selectservice);
            $restricty.val(content.restricty);
            $num_of_series.val(content.num_of_series);
            $trailer.val(content.trailer);
            $kp_rating.val(content.kp_rating);
            $flag_status.val(content.flag_status);
            $actors.val(content.actors);
            $description.val(content.description);
            $advertise.val(content.advertise);
            $poster.val(content.poster);
            $whenontv.val(content.whenontv).focus();
            $release_date.val(content.release_date);
            $country.val(content.country);
            $genre.val(content.genre);
            $serial_duration.val(content.serial_duration);
            $series_list.val(content.series_list);
            $tv_channel.val(content.tv_channel);
            $temp_col1.val(content.temp_col1);
            $temp_col2.val(content.temp_col2).focus();
        },
        build_table: function(shows) {
            let rows = ''

            // очищаем
            $('.shows table > tbody').empty();

            // Если получили - отрисовываем
            if (shows) {
                for (let i=0, l=shows.length; i < l; i++) {
                    rows += `<tr data-content-id="${shows[i].content_id}">
                        <td class="poster"><img src="${shows[i].poster}" alt="${shows[i].poster}" style="width:90px;height:130px;"></td>
                        <td class="title">${shows[i].title}</td>
                        <td class="title_season">${shows[i].title_season}</td>
                        <td class="restricty">${shows[i].restricty}</td>
                        <td class="selectservice">${shows[i].selectservice}</td>
                        <td class="num_of_series">${shows[i].num_of_series}</td>
                        <td class="kp_rating">${shows[i].kp_rating}</td>
                        <td class="flag_status">${shows[i].flag_status}</td>
                        <td class="actors">${shows[i].actors}</td>
                        <td class="description" style="font-size: 0;">${shows[i].description}</td>
                        <td class="advertise">${shows[i].advertise}</td>
                        <td class="whenontv" style="font-size: 0;">${shows[i].whenontv}</td>
                        <td class="trailer" style="font-size: 0;">${shows[i].trailer}</td>
                        <td class="release_date">${shows[i].release_date}</td>
                        <td class="country">${shows[i].country}</td>
                        <td class="genre">${shows[i].genre}</td>
                        <td class="serial_duration">${shows[i].serial_duration}</td>
                        <td class="series_list" style="font-size: 0;">${shows[i].series_list}</td>
                        <td class="tv_channel">${shows[i].tv_channel}</td>
                        <td class="temp_col1" style="font-size: 0;">${shows[i].temp_col1}</td>
                        <td class="temp_col2" style="font-size: 0;">${shows[i].temp_col2}</td>
                    </tr>`;
                }
                $('table > tbody').append(rows);
            }
        },
        error: function(error_msg) {
            $('.error')
                .text(error_msg)
                .css('visibility', 'visible');
            setTimeout(function() {
                $('.error').css('visibility', 'hidden');
            }, 3000)
        }
    };
}());

// Создаем controller
ns.controller = (function(m, v) {
    'use strict';

    let model = m,
        view = v,
        $event_pump = $('body'),
        $content_id = $('#content_id'),
        $title = $('#title'),
        $title_season = $('#title_season'),
        $selectservice = $('#selectservice'),
        $num_of_series = $('#num_of_series'),
        $restricty = $('#restricty'),
        $trailer = $('#trailer'),
        $kp_rating = $('#kp_rating'),
        $flag_status = $('#flag_status'),
        $actors = $('#actors'),
        $description = $('#description'),
        $advertise = $('#advertise'),
        $poster = $('#poster'),
        $whenontv = $('#whenontv'),
        $release_date = $('#release_date'),
        $country = $('#country'),
        $genre = $('#genre'),
        $serial_duration = $('#serial_duration'),
        $series_list = $('#series_list'),
        $tv_channel = $('#tv_channel'),
        $temp_col1 = $('#temp_col1'),
        $temp_col2 = $('#temp_col2');

    // Берем данные из model после того как controller инициалируется
    setTimeout(function() {
        model.read();
    }, 100)

    // Валидация только по названиям: title - это рунэйм (накосячил - поправить потом)
    function validate(title, title_season) {
        return title !== "" && title_season !== "";
    }

    // Обработчики кнопочек
    $('#create').click(function(e) {
        let title = $title.val(),
            title_season = $title_season.val(),
            restricty = $restricty.val(),
            selectservice = $selectservice.val(),
            num_of_series = $num_of_series.val(),
            trailer = $trailer.val(),
            kp_rating = $kp_rating.val(),
            flag_status = $flag_status.val(),
            actors = $actors.val(),
            description = $description.val(),
            advertise = $advertise.val(),
            poster = $poster.val(),
            whenontv = $whenontv.val(),
            release_date = $release_date.val(),
            country = $country.val(),
            genre = $genre.val(),
            serial_duration = $serial_duration.val(),
            series_list = $series_list.val(),
            tv_channel = $tv_channel.val(),
            temp_col1 = $temp_col1.val(),
            temp_col2 = $temp_col2.val();

        e.preventDefault();

        if (validate(title, title_season)) {
            model.create({
                'title': title,
                'title_season': title_season,
                'restricty': restricty,
                'selectservice': selectservice,
                'num_of_series': num_of_series,
                'trailer': trailer,
                'kp_rating': kp_rating,
                'flag_status': flag_status,
                'actors': actors,
                'description': description,
                'advertise': advertise,
                'poster': poster,
                'whenontv': whenontv,
                'release_date': release_date,
                'country': country,
                'genre': genre,
                'serial_duration': serial_duration,
                'series_list': series_list,
                'tv_channel': tv_channel,
                'temp_col1': temp_col1,
                'temp_col2': temp_col2,
            })
        } else {
            alert('Please fill all');
        }
    });

    $('#update').click(function(e) {
        let content_id = $content_id.val(),
            title = $title.val(),
            title_season = $title_season.val(),
            selectservice = $selectservice.val(),
            restricty = $restricty.val(),
            num_of_series = $num_of_series.val(),
            trailer = $trailer.val(),
            kp_rating = $kp_rating.val(),
            flag_status = $flag_status.val(),
            actors = $actors.val(),
            description = $description.val(),
            advertise = $advertise.val(),
            poster = $poster.val(),
            whenontv = $whenontv.val(),
            release_date = $release_date.val(),
            country = $country.val(),
            genre = $genre.val(),
            serial_duration = $serial_duration.val(),
            series_list = $series_list.val(),
            tv_channel = $tv_channel.val(),
            temp_col1 = $temp_col1.val(),
            temp_col2 = $temp_col2.val();
            

        e.preventDefault();

        if (validate(title, title_season)) {
            model.update({
                content_id: content_id,
                title: title,
                title_season: title_season,
                restricty: restricty,
                selectservice: selectservice,
                num_of_series: num_of_series,
                trailer: trailer,
                kp_rating: kp_rating,
                flag_status: flag_status,
                actors: actors,
                description: description,
                advertise: advertise,
                poster: poster,
                whenontv: whenontv,
                release_date: release_date,
                country: country,
                genre: genre,
                serial_duration: serial_duration,
                series_list: series_list,
                tv_channel: tv_channel,
                temp_col1: temp_col1,
                temp_col2: temp_col2,
            })
        } else {
            alert('Problem with first or last name input');
        }
        e.preventDefault();
    });

    $('#delete').click(function(e) {
        let content_id = $content_id.val();

        e.preventDefault();

        if (validate('placeholder', title_season)) {
            model.delete(content_id)
        } else {
            alert('Problem with first or last name input');
        }
        e.preventDefault();
    });

    $('#reset').click(function() {
        view.reset();
    })

    $('table > tbody').on('click', 'tr', function(e) {
        let $target = $(e.target),
            content_id,
            title,
            title_season,
            selectservice,
            restricty,
            num_of_series,
            trailer,
            kp_rating,
            flag_status,
            actors, 
            description, 
            advertise,
            poster,
            whenontv,
            release_date,
            country,
            genre,
            serial_duration,
            series_list,
            tv_channel,
            temp_col1,
            temp_col2;

        content_id = $target
            .parent()
            .attr('data-content-id');

        title = $target
            .parent()
            .find('td.title')
            .text();

        title_season = $target
            .parent()
            .find('td.title_season')
            .text();

        restricty = $target
            .parent()
            .find('td.restricty')
            .text();

        selectservice = $target
            .parent()
            .find('td.selectservice')
            .text();

        num_of_series = $target
            .parent()
            .find('td.num_of_series')
            .text();

        trailer = $target
            .parent()
            .find('td.trailer')
            .text();

        kp_rating = $target
            .parent()
            .find('td.kp_rating')
            .text();

        flag_status = $target
            .parent()
            .find('td.flag_status')
            .text();

        actors = $target
            .parent()
            .find('td.actors')
            .text();

        description = $target
            .parent()
            .find('td.description')
            .text();

        advertise = $target
            .parent()
            .find('td.advertise')
            .text();

        poster = $target
            .parent()
            .find('td.poster')
            .find('img')
            .attr('src');

        whenontv = $target
            .parent()
            .find('td.whenontv')
            .text();
        
        release_date = $target
            .parent()
            .find('td.release_date')
            .text();

        country = $target
            .parent()
            .find('td.country')
            .text();

        genre = $target
            .parent()
            .find('td.genre')
            .text();

        serial_duration = $target
            .parent()
            .find('td.serial_duration')
            .text();

        series_list = $target
            .parent()
            .find('td.series_list')
            .text();

        tv_channel = $target
            .parent()
            .find('td.tv_channel')
            .text();

        temp_col1 = $target
            .parent()
            .find('td.temp_col1')
            .text();

        temp_col2 = $target
            .parent()
            .find('td.temp_col2')
            .text();

        view.update_editor({
            content_id: content_id,
            title: title,
            title_season: title_season,
            restricty: restricty,
            selectservice: selectservice,
            num_of_series: num_of_series,
            trailer: trailer,
            kp_rating: kp_rating,
            flag_status: flag_status,
            actors: actors,
            description: description,
            advertise: advertise,
            poster: poster,
            whenontv: whenontv,
            release_date: release_date,
            country: country,
            genre: genre,
            serial_duration: serial_duration,
            series_list: series_list,
            tv_channel: tv_channel,
            temp_col1: temp_col1,
            temp_col2: temp_col2,
        });
    });

    // Цепляем eventы - поправить - иногда неверный exeption, и html error класс
    $event_pump.on('model_read_success', function(e, data) {
        view.build_table(data);
        view.reset();
    });

    $event_pump.on('model_create_success', function(e, data) {
        model.read();
    });

    $event_pump.on('model_update_success', function(e, data) {
        model.read();
    });

    $event_pump.on('model_delete_success', function(e, data) {
        model.read();
    });

    $event_pump.on('model_error', function(e, xhr, textStatus, errorThrown) {
        let error_msg = textStatus + ': ' + errorThrown + ' - ' + xhr.responseJSON.detail;
        view.error(error_msg);
        console.log(error_msg);
    })
}(ns.model, ns.view));


