/* Requires the Docker Pipeline plugin */
pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                sh 'ls'
                sh 'pwd'
                sh 'docker build -t my_image .'
            }
        }
    }
}
