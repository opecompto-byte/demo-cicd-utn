pipeline {
    agent any
    
    environment {
        WEBHOOK_URL = 'https://discord.com/api/webhooks/1549818234499371088/lFt-hnB6H-TFMOvpLDZKCVCKQog2TJFce67HJOlPqGB3-_BjnHI3DYAPohoKkyYwrwbC'
        APP_NAME = 'web-utn-demo'
    }

    stages {
        stage('1. Obtener Código') {
            steps {
                // Jenkins descarga automáticamente la última versión de GitHub
                echo 'Clonando repositorio...'
            }
        }
        stage('2. Construir Imagen') {
            steps {
                echo 'Empaquetando la aplicación en Docker...'
                sh 'docker build -t ${APP_NAME}:latest .'
            }
        }
        stage('3. Desplegar en Producción') {
            steps {
                echo 'Levantando el nuevo contenedor...'
                // Detenemos la versión vieja si existe, y levantamos la nueva en el puerto 8090
                sh '''
                docker stop ${APP_NAME} || true
                docker rm ${APP_NAME} || true
                docker run -d -p 8090:80 --name ${APP_NAME} ${APP_NAME}:latest
                '''
            }
        }
    }
    
    post {
            success {
                sh """
                    curl -H "Content-Type: application/json" \
                    -X POST \
                    -d '{"content": "✅ **ÉXITO**: Jenkins desplegó la nueva versión correctamente. Revisa el puerto 8090."}' \
                    ${WEBHOOK_URL}
                """
            }
            failure {
                sh """
                    curl -H "Content-Type: application/json" \
                    -X POST \
                    -d '{"content": "🚨 **ERROR**: El pipeline falló. Revisa los logs en la consola de Jenkins."}' \
                    ${WEBHOOK_URL}
                """
            }
        }
}





