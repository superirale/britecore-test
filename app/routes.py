from app import app, db, request, jsonify, json, Response, render_template, url_for
from app.models import Client, FeatureRequest, ProductionArea

# pages
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/create')
def create():
    return render_template('create.html')

#api endpoints
@app.route('/api/clients', methods=['GET','POST'])
def clients():
    if request.method == 'POST':
        name = str(request.form['name'])
        if name:
            client = Client(name=name)
            db.session.add(client)
            db.session.commit()
            response = jsonify({
                'id': client.id,
                'name': client.name
            })
            response.status_code = 201
            return response
    else:
        clients = Client.query.all()
        results = []
        for item in clients:
            results.append({
                    'id': item.id,
                    'name': item.name
                })
        response = jsonify(results)
        response.status_code = 200
        return response

@app.route('/api/production-areas', methods=['GET','POST'])
def production_areas():
    if request.method == 'POST':
        name = str(request.form['name'])
        if name:
            production_area = ProductionArea(name=name)
            db.session.add(production_area)
            db.session.commit()
            response = jsonify({
                'id': production_area.id,
                'name': production_area.name
            })
            response.status_code = 201
            return response
    else:
        production_areas = ProductionArea.query.all()
        results = []
        for item in production_areas:
            results.append({
                    'id': item.id,
                    'name': item.name
                })
        response = jsonify(results)
        response.status_code = 200
        return response

@app.route('/api/feature-requests', methods=['GET','POST'])
def feature_requests():
    if request.method == 'POST':
        title = str(request.form['title'])
        description = str(request.form['description'])
        client_id = int(request.form['client_id'])
        target_date = str(request.form['target_date'])
        production_area_id = str(request.form['production_area_id'])
        priority = int(request.form['priority'])

        feature_request = FeatureRequest(title=title, description=description, client_id=client_id,
                                        target_date=target_date, priority=priority,
                                        production_area_id=production_area_id)
        db.session.add(feature_request)

        priority_to_update = priority
        feat_requests_to_update_count = FeatureRequest.query.filter_by(client_id=client_id, priority=priority_to_update).count()
        while feat_requests_to_update_count > 1:
            feat_requests_to_update = FeatureRequest.query.filter_by(client_id=client_id, priority=priority_to_update).order_by('id').first()
            feat_requests_to_update.priority = feat_requests_to_update.priority + 1
            priority_to_update = priority_to_update + 1
            feat_requests_to_update_count = FeatureRequest.query.filter_by(client_id=client_id, priority=priority_to_update).count()
        db.session.commit()
        response = jsonify({
            'id': feature_request.id,
            'title': feature_request.title,
            'description': feature_request.description,
            'client_id': feature_request.client_id,
            'target_date': feature_request.target_date,
            'production_area_id': feature_request.production_area_id,
            'priority': feature_request.priority
        })
        response.status_code = 201
        return response
    else:
        feature_requests = FeatureRequest.query.all()
        results = []
        for item in feature_requests:
            results.append({
                    'id': item.id,
                    'title': item.title,
                    'description': item.description,
                    'client_id': item.client_id,
                    'target_date': item.target_date,
                    'production_area_id': item.production_area_id,
                    'priority': item.priority
                })
        response = jsonify(results)
        response.status_code = 200
        return response

@app.route('/api/feature-requests/<int:feature_request_id>', methods=['GET', 'DELETE'])
def deleteFeature(feature_request_id):
    if request.method == 'DELETE':
        if feature_request_id:
            feature_to_delete = FeatureRequest.query.get(feature_request_id)
            db.session.delete(feature_to_delete)
            db.session.commit()

            return "", 204
        else:

            return 404
