Generating GOST's Last S-Box
============================

Our illustrates the main result of the report titled _The Secret Structure of the S-Box of Streebog, Kuznechik and Stribob_ and published by Alex Biryukov, Léo Perrin and Aleksei Udovenko ([eprint report 2015/812](http://eprint.iacr.org/2015/812)), namely the decomposition of the S-Box of the last Russian standards in symmetric cryptography:
* [Streebog](https://en.wikipedia.org/wiki/Streebog), a hash function ([specification](https://www.streebog.net/))
* Kuznyechik, a block cipher ([specification draft](http://www.tc26.ru/en/standard/draft/ENG_GOST_R_bsh.pdf))

Running the sage script `gen-pi.py` simply prints the S-Box `pi` but it does so by generating it using the results from Biruykov et al.

Thanks to @okazymyrov for pointing out this target!

**Authors:** Léo Perrin (@picarresursix), Aleksei Udovenko (@hellman)
