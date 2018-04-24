import os
import yaml
from flask.ext.restful import reqparse, abort, Resource
from flask import jsonify
from flask import request

jar_dir = "/tmp"
root_dir = "/tmp/"

class APITasks(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('type', type=str, help='Rate to charge for this resource')

    def get(self, name):
        args = self.parser.parse_args()
        print("test:", args.type)
        if args.type == "":
            print("true")
        return {'hello': 'world'}

    def delete(self, name):
        print(name)
        return '', 204

    def put(self, name):
        args = self.parser.parse_args()
        if args.type == "lucene":
            pass
        elif args.type == "esdsl":
            rtn = request.get_json(force=True)
            print(rtn)
        elif args.type == "yaml":
            pass
        elif args.type == "json" or args.type is None:
            rtn = request.get_json(force=True)
            print("json")
        else:
            return '', 405
        return '', 201

    def post(self, name):
        return '', 201


class APITaskUpload(Resource):
    def put(self):
        file = request.files['file']
        if not file.filename.endswith('yml'):
            return jsonify({'failed': 'only yml file accepted'})
        try:
            data = file.read()
            yml = yaml.load(data)
        except Exception as e:
            return jsonify({'failed': 'only yml file accepted'})
        if 'title' not in yml:
            return jsonify({'failed': 'title needed'})
        newf = os.path.join(root_dir, yml['title']+'.yml')
        if os.path.isfile(newf):
            return jsonify({'failed': 'rule <%s> exists' % yml['title']})
        with open(newf, 'wb')as f:
            f.write(data)
        return jsonify({'success': 'rule <%s> upload success' % yml['title']})


class APITaskRun(Resource):
    def post(self, name):
        if not os.path.isfile(os.path.join(root_dir, name+'.yml')):
            return jsonify({'failed': 'rule <%s> dose not exists' % name})
        

        return jsonify({'success': 'rule <%s> started' % name})

