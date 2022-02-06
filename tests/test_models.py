from app.models.voivodeship import Voivodeship
from app.models.district import District
from app.models.commune import Commune


def test_voivodeship(transaction):
    test_voi = Voivodeship(name='test', voivodeship_number=9999)
    assert test_voi.__str__() == 'Województwo: test , Numer_woj: 9999'
    assert test_voi.__repr__() == 'Województwo: test , Numer_woj: 9999'
    assert Voivodeship.counter(Voivodeship) > 0
    assert Voivodeship.get_all(Voivodeship, 1) is not None

def test_district(transaction):
    test_voi = Voivodeship(name='test', voivodeship_number=9999)
    test_dist = District(name='testP', voivodeship=test_voi, district_number=9009)
    voi = 9999
    assert test_dist.__str__() == 'Powiat: testP, Województwo: test '
    assert test_dist.__repr__() == 'Województwo: test , Powiat: testP'
    assert test_dist.search_by_voivodeship_and_paginate(1, arg=voi) is not None
    assert test_dist.search_by_voivodeship(arg=voi) is not None
    assert District.counter(District) > 0
    assert District.get_all(District, 1) is not None


def test_commune(transaction):
    test_voi = Voivodeship(name='test', voivodeship_number=9999)
    test_dist = District(name='testP', voivodeship=test_voi, district_number=9009)
    test_com = Commune(name='testC', voivodeship=test_voi, district=9999, type=1000, commune=1000)
    voi, dis = 9999, 9999
    assert test_com.__str__() == 'Gmina: testC, Rodz : 1000, Województwo: test , Powiat: 9999'
    assert test_com.__repr__() == 'Województwo: test , Powiat: 9999, Gmina: testC, Rodz : 1000'
    assert test_com.search_by_voivodeship_and_district_paginate(1, voi=voi, dis=dis) is not None
    assert test_com.search_by_voivodeship_and_district(voi=voi, dis=dis) is not None
    assert test_com.search_by_voivodeship_and_paginate(1, voi=voi) is not None
    assert test_com.search_by_voivodeship(voi=voi) is not None
    assert test_com.search_by_district_and_paginate(1, dis=dis) is not None
    assert test_com.search_by_district(dis=dis) is not None
    assert Commune.counter(District) > 0
    assert Commune.get_all(District, 1) is not None


