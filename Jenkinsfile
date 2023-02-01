/* Requires the Docker Pipeline plugin */
pipeline {
    agent {         docker {
            image 'ubuntu'
            args '--user=root'
        } }
    
    stages {
        stage('build') {
            steps {
                sh ' pat-get install python3'
                sh 'export FLASK_APP=app'
                sh 'export FLASK_ENV=development'
                sh 'flask run --host=0.0.0.0'
            }
        }
    }
}
