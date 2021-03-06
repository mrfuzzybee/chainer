import unittest

from cupy import testing


@testing.gpu
class TestShape(unittest.TestCase):

    _multiprocess_can_split_ = True

    @testing.numpy_cupy_array_equal()
    def test_reshape_strides(self, xp):
        a = testing.shaped_arange((1, 1, 1, 2, 2))
        return a.strides

    @testing.numpy_cupy_array_equal()
    def test_reshape2(self, xp):
        a = xp.zeros((8,), dtype=xp.float32)
        return a.reshape((1, 1, 1, 4, 1, 2)).strides

    @testing.for_all_dtypes()
    @testing.numpy_cupy_array_equal()
    def test_nocopy_reshape(self, xp, dtype):
        a = xp.zeros((2, 3, 4), dtype=dtype)
        b = a.reshape(4, 3, 2)
        b[1] = 1
        return a

    @testing.numpy_cupy_array_equal()
    def test_transposed_reshape(self, xp):
        a = testing.shaped_arange((2, 3, 4), xp).T
        return a.reshape(4, 6)

    @testing.numpy_cupy_array_equal()
    def test_transposed_reshape2(self, xp):
        a = testing.shaped_arange((2, 3, 4), xp).transpose(2, 0, 1)
        return a.reshape(2, 3, 4)

    @testing.numpy_cupy_array_equal()
    def test_reshape_with_unknown_dimension(self, xp):
        a = testing.shaped_arange((2, 3, 4), xp)
        return a.reshape(3, -1)

    def test_reshape_with_multiple_unknown_dimensions(self):
        a = testing.shaped_arange((2, 3, 4))
        with self.assertRaises(ValueError):
            a.reshape(3, -1, -1)

    @testing.numpy_cupy_array_equal()
    def test_ravel(self, xp):
        a = testing.shaped_arange((2, 3, 4), xp)
        a = a.transpose(2, 0, 1)
        return a.ravel()
