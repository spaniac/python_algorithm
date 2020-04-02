import unittest


def solution(genres, plays):
    answer = []

    genre_plays_sum = {genre: 0 for genre in set(genres)}
    for i in range(len(genres)):
        genre_plays_sum[genres[i]] += plays[i]
    genre_plays_sum = sorted(genre_plays_sum.items(), key=lambda x: x[1], reverse=True)

    genre_song = {}
    for i in range(len(genres)):
        if genre_song.get(genres[i]) is None:
            genre_song[genres[i]] = {}
        genre_song[genres[i]][i] = plays[i]

    for k, v in genre_plays_sum:
        genre_info = sorted(genre_song[k].items(), key=lambda x: x[1], reverse=True)
        if len(genre_info) >= 2:
            first_two = genre_info[:2]
            if first_two[0][1] == first_two[1][1]:
                first_two = sorted(first_two, key=lambda x: x[0])
            first_two = list(map(lambda x: x[0], first_two))
            answer += first_two
        else:
            answer.append(genre_info[0][0])

    return answer


def solution_best(genres, plays):
    answer = []
    d = {e: [] for e in set(genres)}
    for e in zip(genres, plays, range(len(plays))):
        d[e[0]].append([e[1], e[2]])
    genreSort = sorted(list(d.keys()), key=lambda x: sum(map(lambda y: y[0], d[x])), reverse=True)
    for g in genreSort:
        temp = [e[1] for e in sorted(d[g], key=lambda x: (x[0], -x[1]), reverse=True)]
        answer += temp[:min(len(temp), 2)]
    return answer


def solution_practice(genres, plays):
    answer = []

    db = {genre: [] for genre in set(genres)}
    zip_data = zip(genres, plays, range(len(genres)))
    for data in zip_data:
        db[data[0]].append((data[1], data[2]))
    db_sort = sorted(list(db.keys()), key=lambda x: sum(map(lambda y: y[0], db[x])), reverse=True)
    for item in db_sort:
        item = [e[1] for e in sorted(db[item], key=lambda x: (x[0], -x[1]), reverse=True)]
        answer += item[:min(len(item), 2)]
    return answer


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.genres = ['classic', 'pop', 'classic', 'classic', 'pop']
        self.plays = [500, 600, 150, 800, 2500]
        self.expected_result = [4, 1, 3, 0]

    def tearDown(self) -> None:
        pass

    def test_solution(self):
        result = solution(self.genres, self.plays)
        self.assertEqual(self.expected_result, result)

    def test_solution_best(self):
        result = solution_best(self.genres, self.plays)
        self.assertEqual(self.expected_result, result)

    def test_solution_practice(self):
        result = solution_practice(self.genres, self.plays)
        self.assertEqual(self.expected_result, result)