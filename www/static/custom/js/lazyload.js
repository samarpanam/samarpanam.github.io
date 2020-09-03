$(document).ready(function () {
    $.ajax({
        "type": "post",
        "url": "{{url_for('api')}}",
        "data": {
            "action": "lazy_load"
        },
        'success': function (response_text) {
            var response = JSON.parse(response_text);
            if (response['success']) {
                var lazy_list = [];
                var sutra_list = response['data'];
                var sutra_url = "{{url_for('show_sutra')}}";
                for (sutra of sutra_list) {
                    lazy_list.push(
                        '<li class="list-group-item">',
                        '<span class="btn btn-light mx-2 disabled">' + sutra['di'] + '</span>',
                        '<span>' + sutra['s'] + '</span>',
                        '<a href="' + sutra_url + '/' + sutra['i'] + '">',
                        '<button type="button" class="btn btn-primary float-right">View</button>',
                        '</a>',
                        '</li>',
                    );
                };
                $("#sutra_list").append(lazy_list.join("\n"));
            }
        }
    });
});