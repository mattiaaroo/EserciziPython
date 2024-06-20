import unittest

from film import Film
from movie_genre import Azione, Commedia, Drama
from noleggio import Noleggio

class TestFilm(unittest.TestCase):
    def test_film_initialization(self):
        film = Film(1, "Film Title")
        self.assertEqual(film.getID(), 1)
        self.assertEqual(film.getTitle(), "Film Title")

    def test_film_setters(self):
        film = Film(1, "Film Title")
        film.setID(2)
        film.setTitle("New Title")
        self.assertEqual(film.getID(), 2)
        self.assertEqual(film.getTitle(), "New Title")

    def test_film_isEqual(self):
        film1 = Film(1, "Film Title")
        film2 = Film(1, "Another Title")
        film3 = Film(2, "Different Film")
        self.assertTrue(film1.isEqual(film2))
        self.assertFalse(film1.isEqual(film3))

class TestAzione(unittest.TestCase):
    def test_azione_initialization(self):
        film = Azione(1, "Action Movie")
        self.assertEqual(film.getGenere(), "Azione")
        self.assertEqual(film.getPenale(), 3)

    def test_azione_penale_ritardo(self):
        film = Azione(1, "Action Movie")
        self.assertEqual(film.calcolaPenaleRitardo(film, 5), 15)

class TestCommedia(unittest.TestCase):
    def test_commedia_initialization(self):
        film = Commedia(2, "Comedy Movie")
        self.assertEqual(film.getGenere(), "Commedia")
        self.assertEqual(film.getPenale(), 2.5)

    def test_commedia_penale_ritardo(self):
        film = Commedia(2, "Comedy Movie")
        self.assertEqual(film.calcolaPenaleRitardo(film, 5), 12.5)

class TestDrama(unittest.TestCase):
    def test_drama_initialization(self):
        film = Drama(3, "Drama Movie")
        self.assertEqual(film.getGenere(), "Drama")
        self.assertEqual(film.getPenale(), 3)

    def test_drama_penale_ritardo(self):
        film = Drama(3, "Drama Movie")
        self.assertEqual(film.calcolaPenaleRitardo(film, 5), 15)

class TestNoleggio(unittest.TestCase):
    def setUp(self):
        self.film1 = Azione(1, "Action Movie")
        self.film2 = Commedia(2, "Comedy Movie")
        self.film3 = Drama(3, "Drama Movie")
        self.noleggio = Noleggio([self.film1, self.film2, self.film3])

    def test_isAvailable(self):
        self.assertTrue(self.noleggio.isAvailable(self.film1))
        self.assertTrue(self.noleggio.isAvailable(self.film2))
        self.assertTrue(self.noleggio.isAvailable(self.film3))

    def test_rentAMovie(self):
        self.assertTrue(self.noleggio.rentAMovie(self.film1, 123))
        self.assertFalse(self.noleggio.isAvailable(self.film1))
        self.assertTrue(self.noleggio.isAvailable(self.film2))
        self.assertTrue(self.noleggio.isAvailable(self.film3))

    def test_giveBack(self):
        self.noleggio.rentAMovie(self.film1, 123)
        penalty = self.noleggio.giveBack(self.film1, 123, 5)
        self.assertEqual(penalty, 15)
        self.assertTrue(self.noleggio.isAvailable(self.film1))

    def test_printMovies(self):
        expected_output = [
            f"{self.film1.getTitle()} - {self.film1.getGenere()} -",
            f"{self.film2.getTitle()} - {self.film2.getGenere()} -",
            f"{self.film3.getTitle()} - {self.film3.getGenere()} -"
        ]
        actual_output = [f"{film.getTitle()} - {film.getGenere()} -" for film in self.noleggio.film_list]
        self.assertEqual(actual_output, expected_output)

    def test_printRentMovies(self):
        self.noleggio.rentAMovie(self.film1, 123)
        expected_output = [f"{self.film1.getTitle()} - {self.film1.getGenere()} -"]
        actual_output = [f"{film.getTitle()} - {film.getGenere()} -" for film in self.noleggio.rented_film[123]]
        self.assertEqual(actual_output, expected_output)
        self.assertFalse(456 in self.noleggio.rented_film)

if __name__ == '__main__':
    unittest.main()
