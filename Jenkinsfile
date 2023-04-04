pipeline{
  agent any
  environment {
	    DOCKERHUB_USERNAME = "mittal0706"
	    APP_NAME = "flask_app"
	    IMAGE_TAG = "${BUILD_NUMBER}"
	    IMAGE_NAME = "${DOCKERHUB_USERNAME}/${APP_NAME}"
	    REGISTRY_CREDS = "dockerhub"
	}
  stages{
    stage('Git Checkout'){
      steps{
        script{
          withCredentials([gitUsernamePassword(credentialsId: 'github', gitToolName: 'Default')]) {
 	  }
        }
      }
    }
    stage('install dependecies'){
      steps{
        script{
          sh 'pip install -r requirements.txt'
        }
      }
    }
    stage('docker build image'){
	steps{
	  script{
		docker_image = docker.build("${IMAGE_NAME}:${IMAGE_TAG}")
	  }
	}
     }

    stage('push docker image'){
	steps{
	  script{
		withDockerRegistry([credentialsId: "${REGISTRY_CREDS}", url: '']) {
		docker_image.push("${BUILD_NUMBER}")
		docker_image.push('latest')
	 }
	}
      }
    }
  }
}
