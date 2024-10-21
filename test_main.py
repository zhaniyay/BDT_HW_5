import unittest
from main import is_prime, primes, checksum, pipeline

class TestMainFunctions(unittest.TestCase):

    # Тест для проверки простоты числа
    def test_is_prime(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertFalse(is_prime(4))
        self.assertTrue(is_prime(5))
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(0))

    # Тест для генерации списка простых чисел
    def test_primes(self):
        prime_list = primes(10)
        expected_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        self.assertEqual(prime_list, expected_primes)
        self.assertEqual(len(prime_list), 10)

    # Тест для расчёта контрольной суммы
    def test_checksum(self):
        test_list = [1, 2, 6, 24]
        self.assertEqual(checksum(test_list), 6012369)

    # Тест для полной обработки
    def test_pipeline(self):
        result = pipeline()
        self.assertEqual(result, 7785816)

if __name__ == "__main__":
    unittest.main()
