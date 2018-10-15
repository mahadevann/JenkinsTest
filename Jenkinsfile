pipeline {
    node { docker { image 'mahadevann/myenv:test1' }
	
	  }
    stages {
        stage('build') {
            steps {
                sh '''
		python --version
		behave
		'''
            }
        }
    }
}
