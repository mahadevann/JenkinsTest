//variables
def network='jenkins-${BUILD_NUMBER}'
def seleniumHub='selenium-hub-${BUILD_NUMBER}'
def chrome='chrome-${BUILD_NUMBER}'
def firefox='firefox-${BUILD_NUMBER}'
def containertest='conatinertest-${BUILD_NUMBER}'
   
pipeline {
  
   agent { docker{ image 'mahadevann/myen:test1'}
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
      stage('Tearing Down Selenium Grid') {
          steps {
             //remove all the containers and volumes
             sh "docker rm -vf ${chrome}"
             sh "docker rm -vf ${firefox}"
             sh "docker rm -vf ${seleniumHub}"
             sh "docker network rm ${network}"
          }
        }   
   }
}
