/* Requires the Docker Pipeline plugin */
pipeline {
    agent {         docker {
            image 'python:3.10.7-alpine'
            args '--user=root'
        } }
    
    stages {
        stage('build') {
            steps {
                sh 'export FLASK_APP=app'
                sh 'export FLASK_ENV=development'
                sh 'python3 run flask'
            }
        }
    }
}
