import pytest
import primes

@pytest.mark.skipif(primes.TESTSTEP != 4, reason='Test not relevant for this step')
def test_sieve_4a(monkeypatch, capsys):
    inputs = iter([1, 18])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    sieve = primes.main()
    assert sieve == [0, 1, 2, 3, 0, 5, 0, 7, 0, 0, 0, 11, 0, 13, 0, 0, 0, 17, 0]

@pytest.mark.skipif(primes.TESTSTEP != 4, reason='Test not relevant for this step')
def test_sieve_4b(monkeypatch, capsys):
    inputs = iter([4, 13])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    sieve = primes.main()
    assert sieve == [0, 1, 2, 3, 0, 5, 0, 7, 0, 0, 0, 11, 0, 13]

@pytest.mark.skipif(primes.TESTSTEP != 4, reason='Test not relevant for this step')
def test_prime_1(monkeypatch, capsys):
    inputs = iter([1, 18])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    sieve = primes.main()
    assert sieve == [0, 1, 2, 3, 0, 5, 0, 7, 0, 0, 0, 11, 0, 13, 0, 0, 0, 17, 0]
    captured = capsys.readouterr()
    assert captured.out == ('2\n3\n5\n7\n11\n13\n17\n')


@pytest.mark.skipif(primes.TESTSTEP != 4, reason='Test not relevant for this step')
def test_prime_2(monkeypatch, capsys):
    inputs = iter([4, 18])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    sieve = primes.main()
    assert sieve == [0, 1, 2, 3, 0, 5, 0, 7, 0, 0, 0, 11, 0, 13, 0, 0, 0, 17, 0]
    captured = capsys.readouterr()
    assert captured.out == ('5\n7\n11\n13\n17\n')


@pytest.mark.skipif(primes.TESTSTEP != 4, reason='Test not relevant for this step')
def test_prime_3(monkeypatch, capsys):
    inputs = iter([5, 18])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    sieve = primes.main()
    assert sieve == [0, 1, 2, 3, 0, 5, 0, 7, 0, 0, 0, 11, 0, 13, 0, 0, 0, 17, 0]
    captured = capsys.readouterr()
    assert captured.out == ('5\n7\n11\n13\n17\n')


@pytest.mark.skipif(primes.TESTSTEP != 4, reason='Test not relevant for this step')
def test_prime_4(monkeypatch, capsys):
    inputs = iter([5, 19])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    sieve = primes.main()
    assert sieve == [0, 1, 2, 3, 0, 5, 0, 7, 0, 0, 0, 11, 0, 13, 0, 0, 0, 17, 0, 19]
    captured = capsys.readouterr()
    assert captured.out == ('5\n7\n11\n13\n17\n19\n')
