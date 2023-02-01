/* Requires the Docker Pipeline plugin */
pipeline {
    agent {         docker {
            image 'ubuntu'
            args '--user=root'
        } }
    
    stages {
        stage('build') {
            steps {
                sh 'docker build -t my_image .'
            }
        }
    }
}
