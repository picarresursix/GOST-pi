#!/usr/bin/sage

# AUTHORS: Leo "pi^2/6" Perrin, Aleksei "Hellman" Udovenko
# Time-stamp: <2015-09-16 15:00:19 leo>


from sage.all import *

# The finite field used and its multiplication

X = GF(2).polynomial_ring().gen()
F = GF(2**4, name="a", modulus=X**4+X**3+1)

def F_mult(x, y):
    return (F.fetch_int(x) * F.fetch_int(y)).integer_representation()


# The non-linear 4-bit functions

inv   = [(F.fetch_int(x)**14).integer_representation() for x in xrange(0, 16)]
nu_0  = [0x2,0x5,0x3,0xb,0x6,0x9,0xe,0xa,0x0,0x4,0xf,0x1,0x8,0xd,0xc,0x7]
nu_1  = [0x7,0x6,0xc,0x9,0x0,0xf,0x8,0x1,0x4,0x5,0xb,0xe,0xd,0x2,0x3,0xa]
sigma = [0xc,0xd,0x0,0x4,0x8,0xb,0xa,0xe,0x3,0x9,0x5,0x2,0xf,0x1,0x6,0x7]
phi   = [0xb,0x2,0xb,0x8,0xc,0x4,0x1,0xc,0x6,0x3,0x5,0x8,0xe,0x3,0x6,0xb]


# The linear 8-bit functions

def applymat8(x, mat):
    y = mat * Matrix(GF(2), 8, 1, map(int, bin(x)[2:].zfill(8)))
    return int("".join(map(str, y.T[0][:8])), 2)

alpha = Matrix(GF(2), 8, 8, [
    0,0,0,0,1,0,0,0,
    0,1,0,0,0,0,0,1,
    0,1,0,0,0,0,1,1,
    1,1,1,0,1,1,1,1,
    1,0,0,0,1,0,1,0,
    0,1,0,0,0,1,0,0,
    0,0,0,1,1,0,1,0,
    0,0,1,0,0,0,0,0,
])

omega = Matrix(GF(2), 8, 8, [
    0,0,0,0,1,0,1,0,
    0,0,0,0,0,1,0,0,
    0,0,1,0,0,0,0,0,
    1,0,0,1,1,0,1,0,
    0,0,0,0,1,0,0,0,
    0,1,0,0,0,1,0,0,
    1,0,0,0,0,0,1,0,
    0,0,0,0,0,0,0,1,
])


# Computing pi using our decomposition

pi = []
for x in xrange(256):
    x = applymat8(x, alpha)
    l, r = x >> 4, x & 0xf
    l = (r == 0) * nu_0[l] + (r != 0) * nu_1[F_mult(l, inv[r])]
    r = sigma[F_mult(r, phi[l])]
    x = applymat8((l << 4) | r, omega)
    pi.append(x)


# Displaying pi as it is described in the specification of Streebog

print pi
