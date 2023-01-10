from trakt import init, movies

import configs


class Trakttv:
    def __init__(self):
        init(configs.trakt_username, client_id=configs.trakt_client_id, client_secret=configs.trakt_client_secret)

    def get_trending_movies(self):
        return movies.trending_movies()


if __name__ == '__main__':
    trakttv = Trakttv()
    trending = trakttv.get_trending_movies()
    print("Trending:", trending)
    movie = trending[1]
    print('First:', movie.title, '->', f"{movie.ids['ids']['trakt']}_{movie.slug}")