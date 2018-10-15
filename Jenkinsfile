pipeline {
    agent { docker { image 'selenium/standalone-chrome:3.4.0' } }
    stages {
        stage('build') {
            steps {
                sh '''
		docker run -d -p 4444:4444 selenium/standalone-chrome:3.4.0
		python --version
		behave
		'''
            }
        }
    }
}
