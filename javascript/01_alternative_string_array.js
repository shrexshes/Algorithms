function alternative_string_array(first_str, second_str) {
    const first_str_length = first_str.length;
    const second_str_length = second_str.length;
    const abs_length = (first_str_length > second_str_length ? first_str_length : second_str_length)

    const output = []

    for (let char_count = 0; char_count < abs_length; char_count++) {
        if (char_count < first_str_length) output.push(first_str[char_count]);
        if (char_count < second_str_length) output.push(second_str[char_count])
    }
    return output.join(' ')
}

const result = alternative_string_array("ABCD", "XY")
console.log(result)


