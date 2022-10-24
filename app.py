
import poker.driver as driver


class FlaskAppWrapper:

    def __init__(self, app, **configs):
        self.app = app
        self.configs(**configs)

    def configs(self, **configs):
        for config, value in configs:
            self.app.config[config.upper()] = value

    def add_endpoint(self, endpoint=None, endpoint_name=None, handler=None, methods=['GET'], *args, **kwargs):
        self.app.add_url_rule(endpoint, endpoint_name,
                              handler, methods=methods, *args, **kwargs)

    def run(self, **kwargs):
        self.app.run(**kwargs)


flask_app = Flask(__name__)
app = FlaskAppWrapper(flask_app)
CORS(app.app)


class Game:
    def hand():

        card = driver.playerHand()
        score = driver.checkHand()

        cardData = {
            "card": card,
            "score": score
        }
        return jsonify({"cardData": cardData})


class endPoints:

    app.add_endpoint('/hand', 'hand', Game.hand, methods=['GET'])


if __name__ == "__main__":
    app.run(debug=True)

# enable CORS


"""

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)
# sanity check route
@app.route('/hand', methods=['GET'])
def hand():

    card = driver.playerHand()

    return jsonify({'cards': card})


@app.route('/score', methods=['GET'])
def handRank():
    score = driver.getHandRanks()
    return jsonify(score)


"""
