# https://leetcode.com/problems/minimum-number-of-people-to-teach/description/?envType=daily-question&envId=2025-09-10


class Solution:
    def minimumTeachings(
        self, n: int, languages: list[list[int]], friendships: list[list[int]]
    ) -> int:
        person_lang = {i + 1: set(lang) for i, lang in enumerate(languages)}
        options = dict()
        options_lang = set()
        lang_person_teach = dict()
        min_person = float("inf")

        for pair in friendships:
            common_lang = person_lang[pair[0]].intersection(person_lang[pair[1]])

            if len(common_lang) > 0:
                continue

            pair_tuple = (pair[0], pair[1])
            languages = set()
            for i in range(len(person_lang[pair[1]])):
                language = list(person_lang[pair[1]])[i]
                person = pair[0]

                languages.add(language)
                options.setdefault(pair_tuple, []).append((person, language))
                lang_person_teach.setdefault(language, set()).add(person)

            for i in range(len(person_lang[pair[0]])):
                language = list(person_lang[pair[0]])[i]
                person = pair[1]

                languages.add(language)
                options.setdefault(pair_tuple, []).append((person, language))
                lang_person_teach.setdefault(language, set()).add(person)

            if len(options_lang) == 0:
                options_lang = languages
            else:
                options_lang = options_lang.intersection(languages)

        if len(options_lang) == 0:
            return 0

        for lang in list(options_lang):
            min_person = min(len(lang_person_teach[lang]), min_person)

        return min_person


print(
    Solution().minimumTeachings(
        n=3,
        languages=[[2], [1, 3], [1, 2], [3]],
        friendships=[[1, 4], [1, 2], [3, 4], [2, 3]],
    )
)
print(
    Solution().minimumTeachings(
        n=2, languages=[[1], [2], [1, 2]], friendships=[[1, 2], [1, 3], [2, 3]]
    )
)

print(
    Solution().minimumTeachings(
        n=11,
        languages=[
            [3, 11, 5, 10, 1, 4, 9, 7, 2, 8, 6],
            [5, 10, 6, 4, 8, 7],
            [6, 11, 7, 9],
            [11, 10, 4],
            [6, 2, 8, 4, 3],
            [9, 2, 8, 4, 6, 1, 5, 7, 3, 10],
            [7, 5, 11, 1, 3, 4],
            [3, 4, 11, 10, 6, 2, 1, 7, 5, 8, 9],
            [8, 6, 10, 2, 3, 1, 11, 5],
            [5, 11, 6, 4, 2],
        ],
        friendships=[
            [7, 9],
            [3, 7],
            [3, 4],
            [2, 9],
            [1, 8],
            [5, 9],
            [8, 9],
            [6, 9],
            [3, 5],
            [4, 5],
            [4, 9],
            [3, 6],
            [1, 7],
            [1, 3],
            [2, 8],
            [2, 6],
            [5, 7],
            [4, 6],
            [5, 8],
            [5, 6],
            [2, 7],
            [4, 8],
            [3, 8],
            [6, 8],
            [2, 5],
            [1, 4],
            [1, 9],
            [1, 6],
            [6, 7],
        ],
    )
)
