def test_not_found(testing_client):

    res = testing_client.get('/v1/api/wojewodztwa/2032323')

    assert res.status_code == 404

def test_bad_request(testing_client):

    res = testing_client.get('/v1/api/powiaty?lol=23123')

    assert res.status_code == 400