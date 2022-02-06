
def test_if_response_json(testing_client, urls):

    for i in urls:
        res = testing_client.get(i)
        assert res.content_type == 'application/json'


def util_function(res, schema):

    for i in schema:
        assert i.encode() in res


def test_voivodeship_schema_response(testing_client, urls):

    res = testing_client.get(urls[0]).data

    schema_keys = ['woj', 'id', 'nazwa']

    util_function(res, schema_keys)

def test_district_schema_response(testing_client, urls):

    res = testing_client.get(urls[1]).data

    schema_keys = ['woj', 'id', 'nazwa', 'pow']

    util_function(res, schema_keys)



def test_commune_schema_response(testing_client, urls):

    res = testing_client.get(urls[2]).data

    schema_keys = ['woj', 'id', 'nazwa', 'pow', 'gmi', 'rodz']

    util_function(res, schema_keys)

def test_stats_schema_response(testing_client, urls):


    res = testing_client.get(urls[3]).data

    schema_keys = ['gmi_count', 'pow_count', 'pow_name_max_gmi', 'woj_count', 'woj_name_max_gmi', 'woj_name_max_pow']

    util_function(res, schema_keys)