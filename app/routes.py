from app import app, db, request, jsonify, json, Response, render_template, url_for
from app.models import Client, FeatureRequest, ProductArea

# pages
@app.route('/')
def home():
    feature_requests = FeatureRequest.query.all()
    return render_template('index.html', feature_requests=feature_requests)

@app.route('/feature-requests/create')
def create():
    product_areas = ProductArea.query.all()
    clients = Client.query.all()
    return render_template('create.html', product_areas=product_areas, clients=clients)

@app.route('/feature-requests/edit/<int:id>', methods=['GET'])
def edit(id):
    feature_request = FeatureRequest.query.get(id)
    product_areas = ProductArea.query.all()
    clients = Client.query.all()
    return render_template('edit.html', feature_request=feature_request, product_areas=product_areas, clients=clients)

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
def product_areas():
    if request.method == 'POST':
        name = str(request.form['name'])
        if name:
            product_area = ProductArea(name=name)
            db.session.add(product_area)
            db.session.commit()
            response = jsonify({
                'id': product_area.id,
                'name': product_area.name
            })
            response.status_code = 201
            return response
    else:
        product_areas = ProductArea.query.all()
        results = []
        for item in product_areas:
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
        if "client" in request.form and request.form['client'] != "":
            client = Client(name=request.form['client'])
            db.session.add(client)
            db.session.commit()
            client_id = client.id
        else:
            client_id = request.form['client_id']

        if "product_area" in request.form and request.form['product_area'] != "":
            product_area = ProductArea(name=request.form['product_area'])
            db.session.add(product_area)
            db.session.commit()
            product_area_id = product_area.id
        else:
            product_area_id = request.form['product_area_id']

        target_date = str(request.form['target_date'])
        priority = int(request.form['priority'])

        feature_request = FeatureRequest(title=title, description=description, client_id=client_id,
                                        target_date=target_date, priority=priority,
                                        product_area_id=product_area_id)

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
            'client': feature_request.client.name,
            'target_date': feature_request.target_date,
            'product_area_id': feature_request.product_area_id,
            'product_area': feature_request.product_area.name,
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
                    'client': item.client.name,
                    'product_area_id': item.product_area_id,
                    'product_area': item.product_area.name,
                    'priority': item.priority
                })
        response = jsonify(results)
        response.status_code = 200
        return response

@app.route('/api/feature-requests/<int:id>', methods=['PUT'])
def update_feature_requests(id):
    if request.method == 'PUT':
        feature_request = FeatureRequest.query.get(id)
        feature_request.title = str(request.form['title'])
        feature_request.description = str(request.form['description'])
        if "client" in request.form and request.form['client'] != "":
            client = Client(name=request.form['client'])
            db.session.add(client)
            db.session.commit()
            feature_request.client_id = client.id
        else:
            feature_request.client_id = request.form['client_id']

        if "product_area" in request.form and request.form['product_area'] != "":
            product_area = ProductArea(name=request.form['product_area'])
            db.session.add(product_area)
            db.session.commit()
            feature_request.product_area_id = product_area.id
        else:
            feature_request.product_area_id = request.form['product_area_id']

        feature_request.target_date = str(request.form['target_date'])
        feature_request.priority = int(request.form['priority'])


        priority_to_update = int(request.form['priority'])
        feat_requests_to_update_count = FeatureRequest.query.filter_by(client_id=feature_request.client_id, priority=priority_to_update).count()

        while feat_requests_to_update_count > 1:
            feat_requests_to_update = FeatureRequest.query.filter_by(client_id=feature_request.client_id, priority=priority_to_update).order_by('id').first()
            feat_requests_to_update.priority = feat_requests_to_update.priority + 1
            priority_to_update = priority_to_update + 1
            feat_requests_to_update_count = FeatureRequest.query.filter_by(client_id=feature_request.client_id, priority=priority_to_update).count()


        db.session.commit()

        response = jsonify({
            'id': feature_request.id,
            'title': feature_request.title,
            'description': feature_request.description,
            'client_id': feature_request.client_id,
            'client': feature_request.client.name,
            'target_date': feature_request.target_date,
            'product_area_id': feature_request.product_area_id,
            'product_area': feature_request.product_area.name,
            'priority': feature_request.priority
        })
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
