function format_sutra_id(sutra_id) {
    const devanagari_numeral = {
        "1": "१", "2": "२", "3": "३", "4": "४", "5": "५",
        "6": "६", "7": "७", "8": "८", "9": "९", "0": "०"
    };
    sutra_id = sutra_id.toString();
    var sutra_id_compact = sutra_id.slice(0, 2) + sutra_id.slice(2).replace(/^0+/, '');
    var sutra_id_devanagari = Array.from(sutra_id_compact, digit => devanagari_numeral[digit]);
    var join_char = "।";
    sutra_id = [
        sutra_id_devanagari[0], sutra_id_devanagari[1], sutra_id_devanagari.slice(2).join("")
    ].join(join_char);
    return sutra_id;
}

function format_sutra_reference(sutra_id) {
    sutra_id = sutra_id.toString();
    sutra_id = sutra_id.replace(/[^0-9]/, "")
    sutra_id = sutra_id.slice(0, 2) + sutra_id.slice(2).padStart(3, '0')
    var sutra_display = format_sutra_id(sutra_id);

    reference_str = [
        "<a class=\"btn btn-light btn-sm text-info\" href=\"/sutra/"+ sutra_id + ">",
        sutra_display,
        "</a>",
    ].join("");
    return reference_str
}