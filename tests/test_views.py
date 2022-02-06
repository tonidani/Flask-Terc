'''from flask.views import MethodView


def test_method_views(testing_client):
    class VoivodeshipViewTest(MethodView):
        def get(self):
            return "GET"

    url = "/v1/api/wojewodztwa"
    testing_client.add_url_rule(url, view_func=VoivodeshipViewTest.as_view('voivodeship_view_test'))

    testing_client.get(url).status_code == 200

'''