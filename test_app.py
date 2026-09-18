import unittest
from app import app

class BasicTests(unittest.TestCase):
    def setUp(self):
        # Crea un cliente de pruebas sin levantar el servidor real
        self.app = app.test_client()

    def test_hello_route(self):
        # Simula una petición HTTP a la raíz
        response = self.app.get('/')
        # Verifica que el servidor responda OK (200)
        self.assertEqual(response.status_code, 200)
        # Verifica que la respuesta contenga la palabra clave
        self.assertIn(b'UTN', response.data)

if __name__ == '__main__':
    unittest.main()