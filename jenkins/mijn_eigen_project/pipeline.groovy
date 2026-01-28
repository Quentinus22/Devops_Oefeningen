pipeline {
    agent any
    stages {
        stage('Build & Deploy') {
            steps {
                echo 'J3: Container wordt opgestart...'
                sh 'chmod +x launch_calc.sh'
                sh './launch_calc.sh'
            }
        }
        stage('Health Check') {
            steps {
                echo 'J3: Controleren of de app reageert...'
                // We checken of de website "200 OK" teruggeeft
                sh 'curl -s -I http://localhost:6060 | grep "200 OK"'
            }
        }
    }
}