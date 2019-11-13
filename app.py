import json
from common.file_storage import MogileFileSys
from common import log
from flask import Flask, jsonify, request
from conf import confg
import traceback
app = Flask(__name__)
app.config.update(DEBUG=True)


@app.route('/api/upload', methods=['POST'], strict_slashes=False)
def upload():
    try:
        params = {}
        if request.form.get('param', ''):
            params = json.loads(request.form.get('param', ''))
        # elif request.get_json():
        #     params = request.get_json()
        file_lis = request.files.getlist('file[]')

        if request.method == 'POST':
            key = params.get('file_name', )
            ms = MogileFileSys('images', confg.tracker)
            # file_lis[0].save('./%s'%file_lis[0].filename)
            ret = ms.upload_file(key, file_lis[0])
            if ret:
                return jsonify({"errno": 0, "errmsg": "succ", "data": ret})
            else:
                return jsonify({"errno": 1, "errmsg": "fail"})
    except Exception as data:
        log.LOG.error('fail %s, %s', data, traceback.format_exc())
        return jsonify({"errno": -1, 'erromsg': 'Operate fail'})


if __name__ == '__main__':
    app.run()
