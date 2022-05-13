import unittest
from lab11_functions import *

i = 2
s = 'string'
f = 3.5
n= -1


class MyTestCase(unittest.TestCase):
    
    def test_crc(self):
        self.assertAlmostEqual(crc(1), 3.141, delta=0.001)
        self.assertAlmostEqual(crc(1.5), 7.068, delta=0.001)

        with self.assertRaises(TypeError):
            crc(s)
            
        with self.assertRaises(ValueError):
            crc(-i)
            crc(-f)
            crc(0)

    def test_rct(self):
        self.assertEqual(rct(i,f), 7.0)
        self.assertEqual(rct(f, i), 7.0)
        self.assertEqual(rct(i,i),4.0)
        self.assertEqual(rct(f,f),12.25)
        
        with self.assertRaises(TypeError):
            rct(i,s)
            rct(s,i)
            rct(s,s)
            rct(f,s)
            rct(s,f)
            
            

        with self.assertRaises(ValueError):
            rct(i,0)
            rct(0,i)
            rct(0,0)
            rct(0,n)
            rct(n,0)
            rct(n,n)
            rct(n,f)
            rct(f,n)
            rct(0,f)
            rct(f,0)
            rct(i,n)
            rct(n,i)
            
    def test_sqr(self):
        self.assertEqual(sqr(i), 4)
        self.assertEqual(sqr(f), 12.25)

        with self.assertRaises(TypeError):
            sqr(s)
        with self.assertRaises(ValueError):
            sqr(0)
            sqr(n)

    def test_trg(self):
        self.assertEqual(trg(i,f), 3.5)
        self.assertEqual(trg(f,i), 3.5)
        self.assertEqual(trg(i,i), 4.0)
        self.assertEqual(trg(0.5,0.5),0.125)

        with self.assertRaises(TypeError):
            trg(i,s)
            trg(s,i)
            trg(f,s)
            trg(s,f)
            trg(s,s)

        with self.assertRaises(ValueError):
            trg(i,0)
            trg(i,n)
            trg(0,i)
            trg(n,i)
            trg(f,0)
            trg(f,n)
            trg(0,f)
            trg(n,f)
            trg(n,n)
            trg(0,0)
            trg(0,n)
            trg(n,0)

if __name__ == '__main__':
    unittest.main()
