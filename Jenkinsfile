pipeline {
    agent { docker { image 'selenium/standalone-chrome:3.4.0' 
	   		args '-d -p 4444:4444'
		   }
	
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
