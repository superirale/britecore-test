def deploy_app():
    "Deploy to the server specified"
    root_path = '/var/www/html/britecore'

    with cd(root_path):
        with prefix("source %s/bin/activate" % root_path):
            with cd('flask_catalog_deployment'):
                run('git pull')
                run('python setup.py install')

            sudo('bin/supervisorctl restart all')