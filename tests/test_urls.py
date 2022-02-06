def test_all_endpoints(testing_client, urls):

    for i in urls:
        assert testing_client.get(i).status_code == 200



