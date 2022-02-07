import sys
sys.path.insert(0, '../')
from flask import Flask, request, jsonify
import json
from init import config
from datetime import datetime
from manage_list import tools,list_manager

app = Flask(__name__)


@app.route("/")
def hello():
	return '''Hello world !
    Try the following commands:
    - /get_list'''

@app.route('/get_list', methods=['OPTIONS', 'GET', 'POST'])
def get_list():
    if(config.CLEAN_DATABASE == True):
        tools.clean_up_df_symbol(config.INPUT_FILE_IMPORTED_DATA)
        tools.clean_up_df_symbol(config.INPUT_FILE_IMPORTED_DATA_ISNI)
    
    str_markets = request.args.get("markets")
    print(str_markets)
    markets = str_markets.split(',')

    start = datetime.now()
    print("get_list...")
    result = list_manager.api_get_list(markets)

    result_for_response = {}
    for key in result.keys():
        df = result[key]
        result_for_response[key] = df.to_json()

    end = datetime.now()
    delta = end - start
    elapsed_time = str(delta)
    print(elapsed_time)

    response = {
        "result":result_for_response,
        "elapsed_time":elapsed_time
    }

    response = jsonify(response)
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Credentials", "true")
    response.headers.add("Access-Control-Allow-Methods", "GET,HEAD,OPTIONS,POST,PUT")
    response.headers.add("Access-Control-Allow-Headers", "Access-Control-Allow-Headers, Origin,Accept, X-Requested-With, Content-Type, Access-Control-Request-Method, Access-Control-Request-Headers")
    return response




if __name__ == "__main__":
	app.run(debug=False, host= '0.0.0.0')
