// https://leetcode.com/problems/adding-spaces-to-a-string/?envType=daily-question&envId=2024-12-03

/**
 * @param {string} s
 * @param {number[]} spaces
 * @return {string}
 */
var addSpaces = function (s, spaces) {
    const segments = [0, ...spaces, s.length];
    const subStrings = [];

    for (let i = 0; i < segments.length - 1; i++) {
        subStrings.push(s.substring(segments[i], segments[i + 1]));
    }

    return subStrings.join(' ');
};