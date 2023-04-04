pipeline{
  agent any
  stages{
    stage('Git Checkout'){
      steps{
        script{
          git branch: 'main', url: 'https://github.com/mittal0706/flask_app.git'
        }
      }
    }
    stage('install dependecies'){
      Steps{
        script{
          sh 'pip install -r requirements.txt'
        }
      }
    }
  }
}
