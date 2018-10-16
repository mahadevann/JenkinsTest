
   
pipeline {
  
   agent { docker{ image 'mahadevann/mytestenv:test1'}
         }

   stages{

      stage('Run Test') {
         steps{
            sh '''
            python3 --version
            behave
            '''
         }
      }   
   }
}
