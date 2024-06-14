import unittest
from persona import Persona
from dottore import Dottore
from paziente import Paziente
from fatture import Fatture

class TestPersona(unittest.TestCase):

    def setUp(self):
        self.persona = Persona('Mario', 'Rossi')

    def test_init(self):
        self.assertEqual(self.persona.getName(), 'Mario')
        self.assertEqual(self.persona.getLastName(), 'Rossi')
        self.assertEqual(self.persona.getAge(), 0)

    def test_setname(self):
        self.persona.setname('Luigi')
        self.assertEqual(self.persona.getName(), 'Luigi')
        result = self.persona.setname(123)
        self.assertEqual(result, "Il nome inserito non è una stringa!")
        self.assertEqual(self.persona.getName(), 'Luigi')

    def test_setLastName(self):
        self.persona.setLastName('Bianchi')
        self.assertEqual(self.persona.getLastName(), 'Bianchi')
        result = self.persona.setLastName(123)
        self.assertEqual(result, "Il cognome inserito non è una stringa!")
        self.assertEqual(self.persona.getLastName(), 'Bianchi')

    def test_setAge(self):
        self.persona.setAge(25)
        self.assertEqual(self.persona.getAge(), 25)
        result = self.persona.setAge('venticinque')
        self.assertEqual(result, "L'età deve essere un numero intero!")
        self.assertEqual(self.persona.getAge(), 25)

class TestDottore(unittest.TestCase):

    def setUp(self):
        self.dottore = Dottore('Mario', 'Rossi', 'Cardiologo', 100.0)

    def test_init(self):
        self.assertEqual(self.dottore.getName(), 'Mario')
        self.assertEqual(self.dottore.getLastName(), 'Rossi')
        self.assertEqual(self.dottore.getSpecialization(), 'Cardiologo')
        self.assertEqual(self.dottore.getParcel(), 100.0)

    def test_isAValidDoctor(self):
        self.dottore.setAge(35)
        self.assertEqual(self.dottore.isAValidDoctor(), "Doctor nome e cognome is valid!")
        self.dottore.setAge(25)
        self.assertEqual(self.dottore.isAValidDoctor(), "Doctor nome e cognome is not valid!")

class TestPaziente(unittest.TestCase):

    def setUp(self):
        self.paziente = Paziente('Mario', 'Rossi')

    def test_init(self):
        self.assertEqual(self.paziente.getName(), 'Mario')
        self.assertEqual(self.paziente.getLastName(), 'Rossi')

    def test_setIdCode(self):
        self.paziente.setIdCode('ABC123')
        self.assertEqual(self.paziente.getIdCode(), 'ABC123')

class TestFatture(unittest.TestCase):

    def setUp(self):
        self.dottore = Dottore('Mario', 'Rossi', 'Cardiologo', 100.0)
        self.dottore.setAge(35)
        self.paziente1 = Paziente('Luigi', 'Bianchi')
        self.paziente1.setIdCode('XYZ789')
        self.paziente2 = Paziente('Anna', 'Verdi')
        self.paziente2.setIdCode('DEF456')
        self.fatture = Fatture([self.paziente1], self.dottore)

    def test_init(self):
        self.assertEqual(self.fatture.getFatture(), 1)
        self.assertEqual(self.fatture.getSalary(), 100.0)

    def test_add_remove_patient(self):
        self.fatture.addPatient(self.paziente2)
        self.assertEqual(self.fatture.getFatture(), 2)
        self.assertEqual(self.fatture.getSalary(), 200.0)
        self.fatture.removePatient('XYZ789')
        self.assertEqual(self.fatture.getFatture(), 1)
        self.assertEqual(self.fatture.getSalary(), 100.0)

if __name__ == '__main__':
    unittest.main()
