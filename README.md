Generating GOST's Last S-Box
============================

Our script illustrates the main result of the report titled _The Secret Structure of the S-Box of Streebog, Kuznechik and Stribob_ published by Alex Biryukov, Léo Perrin and Aleksei Udovenko ([eprint report 2015/812](http://eprint.iacr.org/2015/812)), namely the decomposition of the S-Box of the last Russian standards in symmetric cryptography:
* [Streebog](https://en.wikipedia.org/wiki/Streebog), a hash function ([website](https://www.streebog.net/)), and
* Kuznyechik, a block cipher ([specification draft](http://www.tc26.ru/en/standard/draft/ENG_GOST_R_bsh.pdf)).

Running the sage script `gen-pi.py` simply prints the S-Box `pi` but it does so by generating it using the results from Biruykov et al.

Thanks to [@okazymyrov](https://github.com/okazymyrov) for pointing out this target for cryptanalysis!

**Authors:** Léo Perrin ([@picarresursix](https://github.com/picarresursix)), Aleksei Udovenko ([@hellman](https://github.com/hellman))
