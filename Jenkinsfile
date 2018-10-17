
   
pipeline {
  
   agent { docker{ image 'mahadevann/mytestenv:test1'}
         }

   stages{
     stage('Setting Up Selenium Grid') {
         steps{        
            sh "docker network create ${network}"
            sh "docker run -d -p 4444:4444 --name ${seleniumHub} --network ${network} selenium/hub"
            sh "docker run -d -e HUB_PORT_4444_TCP_ADDR=${seleniumHub} -e HUB_PORT_4444_TCP_PORT=4444 --network ${network} --name ${chrome} selenium/node-chrome"
         }
      }

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
