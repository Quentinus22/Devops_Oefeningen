node {
    stage('Preparation') {
        catchError(buildResult: 'SUCCESS') {
            sh 'docker container stop samplerunning'
            sh 'docker container rm samplerunning'
        }
    }
    stage('Build') {
        build 'BuildFlaskAppJob'
    }
    stage('Results') {
        build 'TestFlaskAppJob'
    }
}