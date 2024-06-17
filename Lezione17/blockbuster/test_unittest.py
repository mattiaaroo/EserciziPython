import unittest

from film import Film
from movie_genre import Azione, Commedia, Drama
from noleggio import Noleggio

class TestFilm(unittest.TestCase):

    def setUp(self):
        # Create 10 films
        self.films = [
            Azione(1, "Azione 1"),
            Azione(2, "Azione 2"),
            Azione(3, "Azione 3"),
            Azione(4, "Azione 4"),
            Azione(5, "Azione 5"),
            Commedia(6, "Commedia 1"),
            Commedia(7, "Commedia 2"),
            Commedia(8, "Commedia 3"),
            Commedia(9, "Commedia 4"),
            Drama(10, "Drama 1")
        ]
        self.noleggio = Noleggio(self.films.copy())

    def test_isAvailable_true(self):
        self.assertTrue(self.noleggio.isAvailable(self.films[0]))
        self.assertTrue(self.noleggio.isAvailable(self.films[5]))
        self.assertTrue(self.noleggio.isAvailable(self.films[9]))

    def test_isAvailable_false(self):
        film_not_in_list = Azione(11, "Non Esistente")
        self.assertFalse(self.noleggio.isAvailable(film_not_in_list))
        film_not_in_list = Commedia(12, "Commedia Non Esistente")
        self.assertFalse(self.noleggio.isAvailable(film_not_in_list))
        film_not_in_list = Drama(13, "Drama Non Esistente")
        self.assertFalse(self.noleggio.isAvailable(film_not_in_list))

    def test_rentAMovie_success(self):
        client_id = "Client1"
        self.assertTrue(self.noleggio.rentAMovie(self.films[0], client_id))
        self.assertTrue(self.noleggio.rentAMovie(self.films[5], client_id))
        self.assertTrue(self.noleggio.rentAMovie(self.films[9], client_id))

    def test_rentAMovie_afterRent(self):
        client_id = "Client1"
        self.noleggio.rentAMovie(self.films[0], client_id)
        self.assertFalse(self.noleggio.isAvailable(self.films[0]))
        self.noleggio.rentAMovie(self.films[5], client_id)
        self.assertFalse(self.noleggio.isAvailable(self.films[5]))
        self.noleggio.rentAMovie(self.films[9], client_id)
        self.assertFalse(self.noleggio.isAvailable(self.films[9]))

    def test_rentAMovie_inClientList(self):
        client_id = "Client1"
        self.noleggio.rentAMovie(self.films[0], client_id)
        self.assertIn(self.films[0], self.noleggio.rented_film[client_id])
        self.noleggio.rentAMovie(self.films[5], client_id)
        self.assertIn(self.films[5], self.noleggio.rented_film[client_id])
        self.noleggio.rentAMovie(self.films[9], client_id)
        self.assertIn(self.films[9], self.noleggio.rented_film[client_id])

    def test_rentUnavailableMovie(self):
        film_to_rent = self.films[0]
        client_id1 = "Client1"
        client_id2 = "Client2"
        self.assertTrue(self.noleggio.rentAMovie(film_to_rent, client_id1))
        self.assertFalse(self.noleggio.rentAMovie(film_to_rent, client_id2))
        film_to_rent = self.films[5]
        self.assertTrue(self.noleggio.rentAMovie(film_to_rent, client_id1))
        self.assertFalse(self.noleggio.rentAMovie(film_to_rent, client_id2))
        film_to_rent = self.films[9]
        self.assertTrue(self.noleggio.rentAMovie(film_to_rent, client_id1))
        self.assertFalse(self.noleggio.rentAMovie(film_to_rent, client_id2))

    def test_giveBack_available(self):
        client_id = "Client1"
        self.noleggio.rentAMovie(self.films[0], client_id)
        self.assertFalse(self.noleggio.isAvailable(self.films[0]))
        self.noleggio.giveBack(self.films[0], client_id, 2)
        self.assertTrue(self.noleggio.isAvailable(self.films[0]))
        self.noleggio.rentAMovie(self.films[5], client_id)
        self.assertFalse(self.noleggio.isAvailable(self.films[5]))
        self.noleggio.giveBack(self.films[5], client_id, 2)
        self.assertTrue(self.noleggio.isAvailable(self.films[5]))
        self.noleggio.rentAMovie(self.films[9], client_id)
        self.assertFalse(self.noleggio.isAvailable(self.films[9]))
        self.noleggio.giveBack(self.films[9], client_id, 2)
        self.assertTrue(self.noleggio.isAvailable(self.films[9]))

    def test_giveBack_notInClientList(self):
        client_id = "Client1"
        self.noleggio.rentAMovie(self.films[0], client_id)
        self.noleggio.giveBack(self.films[0], client_id, 2)
        self.assertNotIn(self.films[0], self.noleggio.rented_film[client_id])
        self.noleggio.rentAMovie(self.films[5], client_id)
        self.noleggio.giveBack(self.films[5], client_id, 2)
        self.assertNotIn(self.films[5], self.noleggio.rented_film[client_id])
        self.noleggio.rentAMovie(self.films[9], client_id)
        self.noleggio.giveBack(self.films[9], client_id, 2)
        self.assertNotIn(self.films[9], self.noleggio.rented_film[client_id])

    def test_calcolaPenaleRitardo(self):
        client_id = "Client1"
        self.noleggio.rentAMovie(self.films[0], client_id)
        penale = self.noleggio.giveBack(self.films[0], client_id, 2)
        self.assertEqual(penale, 6)
        self.noleggio.rentAMovie(self.films[5], client_id)
        penale = self.noleggio.giveBack(self.films[5], client_id, 3)
        self.assertEqual(penale, 7.5)
        self.noleggio.rentAMovie(self.films[9], client_id)
        penale = self.noleggio.giveBack(self.films[9], client_id, 4)
        self.assertEqual(penale, 12)

    def test_printMovies(self):
        expected_titles = [film.getTitle() for film in self.films]
        actual_titles = [film.getTitle() for film in self.noleggio.film_list]
        self.assertListEqual(expected_titles, actual_titles)
        
        self.noleggio.rentAMovie(self.films[0], "Client1")
        self.assertNotIn(self.films[0].getTitle(), [film.getTitle() for film in self.noleggio.film_list])
        
        self.noleggio.giveBack(self.films[0], "Client1", 2)
        self.assertIn(self.films[0].getTitle(), [film.getTitle() for film in self.noleggio.film_list])

    def test_printRentMovies(self):
        client_id = "Client1"
        self.noleggio.rentAMovie(self.films[0], client_id)
        self.noleggio.rentAMovie(self.films[1], client_id)
        rented_titles = [film.getTitle() for film in self.noleggio.rented_film[client_id]]
        expected_titles = [self.films[0].getTitle(), self.films[1].getTitle()]
        self.assertListEqual(rented_titles, expected_titles)
        
        self.noleggio.rentAMovie(self.films[5], client_id)
        rented_titles.append(self.films[5].getTitle())
        self.assertListEqual([film.getTitle() for film in self.noleggio.rented_film[client_id]], rented_titles)
        
        self.noleggio.rentAMovie(self.films[9], client_id)
        rented_titles.append(self.films[9].getTitle())
        self.assertListEqual([film.getTitle() for film in self.noleggio.rented_film[client_id]], rented_titles)

if __name__ == "__main__":
    unittest.main()
