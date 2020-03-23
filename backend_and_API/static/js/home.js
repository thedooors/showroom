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
        $year = $('#year'),
        $title = $('#title'),
        $restrict = $('#restrict'),
        $selectservice = $('#selectservice'),
        $season = $('#season'),
        $duration = $('#duration'),
        $rating = $('#rating'),
        $kp_rating = $('#kp_rating'),
        $imdb_rating = $('#imdb_rating'),
        $description = $('#description'),
        $background = $('#background'),
        $poster = $('#poster'),
        $whenontv = $('#whenontv');

    return {
        reset: function() {
            $content_id.val('');
            $title.val('');
            $year.val('').focus();
            $selectservice.val('FX');
            $restrict.val('0');
            $season.val('');
            $duration.val('');
            $rating.val('3');
            $kp_rating.val('GO');
            $imdb_rating.val('');
            $description.val('');
            $background.val('');
            $poster.val('');
            $whenontv.val('');
        },
        update_editor: function(content) {
            $content_id.val(content.content_id);
            $title.val(content.title);
            $year.val(content.year);
            $selectservice.val(content.selectservice);
            $restrict.val(content.restrict);
            $season.val(content.season);
            $duration.val(content.duration);
            $rating.val(content.rating);
            $kp_rating.val(content.kp_rating);
            $imdb_rating.val(content.imdb_rating);
            $description.val(content.description);
            $background.val(content.background);
            $poster.val(content.poster);
            $whenontv.val(content.whenontv).focus();
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
                        <td class="year">${shows[i].year}</td>
                        <td class="title">${shows[i].title}</td>
                        <td class="restrict">${shows[i].restrict}</td>
                        <td class="selectservice">${shows[i].selectservice}</td>
                        <td class="season">${shows[i].season}</td>
                        <td class="duration">${shows[i].duration}</td>
                        <td class="rating">${shows[i].rating}</td>
                        <td class="kp_rating">${shows[i].kp_rating}</td>
                        <td class="imdb_rating" style="font-size: 0;">${shows[i].imdb_rating}</td>
                        <td class="description" style="font-size: 0;">${shows[i].description}</td>
                        <td class="background"><img src="${shows[i].background}" alt="${shows[i].background}" style="width:85px;height:60px;"></td>
                        <td class="whenontv" style="font-size: 0;">${shows[i].whenontv}</td>
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
        $year = $('#year'),
        $title = $('#title'),
        $selectservice = $('#selectservice'),
        $season = $('#season'),
        $restrict = $('#restrict'),
        $duration = $('#duration'),
        $rating = $('#rating'),
        $kp_rating = $('#kp_rating'),
        $imdb_rating = $('#imdb_rating'),
        $description = $('#description'),
        $background = $('#background'),
        $poster = $('#poster'),
        $whenontv = $('#whenontv');

    // Берем данные из model после того как controller инициалируется
    setTimeout(function() {
        model.read();
    }, 100)

    // Валидация только по названиям: year - это рунэйм (накосячил - поправить потом)
    function validate(year, title) {
        return year !== "" && title !== "";
    }

    // Обработчики кнопочек
    $('#create').click(function(e) {
        let year = $year.val(),
            title = $title.val(),
            restrict = $restrict.val(),
            selectservice = $selectservice.val(),
            season = $season.val(),
            duration = $duration.val(),
            rating = $rating.val(),
            kp_rating = $kp_rating.val(),
            imdb_rating = $imdb_rating.val(),
            description = $description.val(),
            background = $background.val(),
            poster = $poster.val(),
            whenontv = $whenontv.val();

        e.preventDefault();

        if (validate(year, title)) {
            model.create({
                'year': year,
                'title': title,
                'restrict': restrict,
                'selectservice': selectservice,
                'season': season,
                'duration': duration,
                'rating': rating,
                'kp_rating': kp_rating,
                'imdb_rating': imdb_rating,
                'description': description,
                'background': background,
                'poster': poster,
                'whenontv': whenontv,
            })
        } else {
            alert('Please fill all');
        }
    });

    $('#update').click(function(e) {
        let content_id = $content_id.val(),
            year = $year.val(),
            title = $title.val(),
            selectservice = $selectservice.val(),
            restrict = $restrict.val(),
            season = $season.val(),
            duration = $duration.val(),
            rating = $rating.val(),
            kp_rating = $kp_rating.val(),
            imdb_rating = $imdb_rating.val(),
            description = $description.val(),
            background = $background.val(),
            poster = $poster.val(),
            whenontv = $whenontv.val();
            

        e.preventDefault();

        if (validate(year, title, restrict, selectservice, season)) {
            model.update({
                content_id: content_id,
                year: year,
                title: title,
                restrict: restrict,
                selectservice: selectservice,
                season: season,
                duration: duration,
                rating: rating,
                kp_rating: kp_rating,
                imdb_rating: imdb_rating,
                description: description,
                background: background,
                poster: poster,
                whenontv: whenontv,
            })
        } else {
            alert('Problem with first or last name input');
        }
        e.preventDefault();
    });

    $('#delete').click(function(e) {
        let content_id = $content_id.val();

        e.preventDefault();

        if (validate('placeholder', title)) {
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
            year,
            title,
            selectservice,
            restrict,
            season,
            duration,
            rating,
            kp_rating,
            imdb_rating, 
            description, 
            background,
            poster,
            whenontv;

        content_id = $target
            .parent()
            .attr('data-content-id');

        year = $target
            .parent()
            .find('td.year')
            .text();

        title = $target
            .parent()
            .find('td.title')
            .text();

        restrict = $target
            .parent()
            .find('td.restrict')
            .text();

        selectservice = $target
            .parent()
            .find('td.selectservice')
            .text();

        season = $target
            .parent()
            .find('td.season')
            .text();

        duration = $target
            .parent()
            .find('td.duration')
            .text();

        rating = $target
            .parent()
            .find('td.rating')
            .text();

        kp_rating = $target
            .parent()
            .find('td.kp_rating')
            .text();

        imdb_rating = $target
            .parent()
            .find('td.imdb_rating')
            .text();

        description = $target
            .parent()
            .find('td.description')
            .text();

        background = $target
            .parent()
            .find('td.background')
            .find('img')
            .attr('src');

        poster = $target
            .parent()
            .find('td.poster')
            .find('img')
            .attr('src');

        whenontv = $target
            .parent()
            .find('td.whenontv')
            .text();

        view.update_editor({
            content_id: content_id,
            year: year,
            title: title,
            restrict: restrict,
            selectservice: selectservice,
            season: season,
            duration: duration,
            rating: rating,
            kp_rating: kp_rating,
            imdb_rating: imdb_rating,
            description: description,
            background: background,
            poster: poster,
            whenontv: whenontv,
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


