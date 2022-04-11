from crypt import methods
from flask import render_template
from app.front import front

@front.route('/', methods=['GET', 'POST'])
def frontend_map():
    return render_template('openlayers.html')

@front.route('/mvt', methods=['GET'])
def frontend_map_mvt():
    return render_template('openlayers-mvt.html')


@front.route('/purge_cache', methods=['GET'])
def delete_cache():
    import shutil
    from config import Config
    shutil.rmtree(Config.CACHE_PATH)

    return 'ok'