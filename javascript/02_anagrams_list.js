
// Write a program that takes in a word list and outputs a 
// list of all the words that are anagrams of another word in the list.


let word_list = [
    "supersonic",
    "car",
    "tree",
    "boy",
    "percussion",
    "girl",
    "arc"
];
let anagram_list = [];

function AnagramsList(list) {
    for (let i = 0; i < list.length; i++) {
        for (let j = i + 1; j < list.length; j++) {
            if (
                list[i] != list[j] &&
                list[i].split("").sort().join("") === list[j].split("").sort().join("")
            ) {
                anagram_list.push(list[i])
            }
        }

    }
    console.log(anagram_list)
}
AnagramsList(word_list)