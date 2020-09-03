$(document).ready(function () {
    const sutra_url = "{{url_for('show_sutra')}}";
    lazy_list = [];
    for (sutra_id in sutra_index) {
        var sutra_text = sutra_index[sutra_id];
        lazy_list.push(
            '<li class="list-group-item">',
            '<span class="btn btn-light mx-2 disabled">' + format_sutra_id(sutra_id) + '</span>',
            '<span>' + sutra_text + '</span>',
            '<a href="' + sutra_url + '/' + sutra_id + '">',
            '<button type="button" class="btn btn-primary float-right">View</button>',
            '</a>',
            '</li>',
        );
    };
    $("#sutra_list").append(lazy_list.join("\n"));
});