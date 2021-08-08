import json
import anton
from anton.lights.modes import RgbColor, Lights
from flask import make_response, jsonify, request, abort

lights = Lights()

@anton.app.route('/api/')
def api():
    return jsonify({'about':'REST API for managing Anton Audio Lights','url':request.path})

# Error Handlers
# =======================================================

@anton.app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'message': 'Bad Request', 'status_code': 400}), 400)

@anton.app.errorhandler(403)
def forbidden(error):
    return make_response(jsonify({'message': 'Forbidden', 'status_code': 403}), 403)

@anton.app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'message': 'Not Found', 'status_code': 404}), 404)

# Light Mode Requests
# =======================================================
@anton.app.route('/api/modes/', methods=['GET'])
def get_light_modes():
    print('FUCK')
    return jsonify(
        {
            'modes': Lights.list_modes(), 
            'current_mode': lights.get_current_mode(),
            'current_submode': lights.get_current_submode(),
            'current_color': lights.get_current_color(),
            'url': request.path
        })

@anton.app.route('/api/modes/', methods=['POST'])
def set_light_mode():
    lights.set_mode(**request.json)
    return jsonify({'mode':lights.get_current_mode(),'url':request.path})

@anton.app.route('/api/modes/<string:mode>/', methods=['GET','POST']) #debug route
def set_lights(mode):
    lights.set_mode(mode, **request.args)
    return jsonify({'mode':mode,'url':request.path})

# Arduino Updates
# =======================================================
@anton.app.route('/arduino/',methods=['POST'])
def arduino_boot():
    pass
