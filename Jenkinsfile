pipeline {
    agent { label 'slave' }
    stages {
        stage('Build-application') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: 'docker-login', passwordVariable: 'PASSWORD', usernameVariable: 'USERNAME')]) {
                        sh """
                            docker build -t abdelrahman58/django-app .
                            docker login -u '${USERNAME}' -p '${PASSWORD}'
                            docker push abdelrahman58/django-app
                        """
                     }   
                    }

                }
             }
      stage('Build-nginx') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: 'docker-login', passwordVariable: 'PASSWORD', usernameVariable: 'USERNAME')]) {
                        sh """
                            cd nginx/
                            docker build -t abdelrahman58/nginx-app-django .
                            docker push abdelrahman58/nginx-app-django
                        """
                     }   
                    }

                }
             }
      stage('Deploy') {
            steps {
                script {
                        sh """
                            cd deploy-appdjango/
                            kubectl apply -f .
                        """
                    }
                }
            }
      }
    
}
