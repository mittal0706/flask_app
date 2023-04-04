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
    stage('Checkout K8S manifest SCM'){
            steps {
                git branch: 'main',
                url: 'https://github.com/mittal0706/cicd-demo-manifests-repo.git'
            }
        }
        
        stage('Update K8S manifest & push to Repo'){
            steps {
                script{
                       sh '''
		       withCredentials([gitUsernamePassword(credentialsId: 'github', gitToolName: 'Default')]) {
                        cat deploy.yaml
                        sed -i 's/${APP_NAME}.*/${APP_NAME}:${IMAGE_TAG}/g' deploy.yaml
                        cat deploy.yaml
			git add deploy.yaml    
                        git commit -m 'Updated the deploy yaml | Jenkins Pipeline'
                        git remote -v
                        git push https://github.com/mittal0706/cicd-demo-manifests-repo.git HEAD:main
                       '''                      
                }
	    }	    
            }
        }
  }
}
