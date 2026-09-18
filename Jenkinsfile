pipeline {
    agent any
    
    environment {
        WEBHOOK_URL = 'https://discord.com/api/webhooks/1549818234499371088/lFt-hnB6H-TFMOvpLDZKCVCKQog2TJFce67HJOlPqGB3-_BjnHI3DYAPohoKkyYwrwbC'
        APP_NAME = 'python-utn-demo'
    }
	
    stages {
        stage('1. Obtener Código') {
            steps {
                echo 'Clonando repositorio...'
            }
        }
        stage('2. Construir Imagen') {
            steps {
                echo 'Empaquetando la aplicación en Docker...'
                sh 'docker build -t ${APP_NAME}:latest .'
            }
        }
        stage('3. Pruebas Unitarias (Control de Calidad)') {
            steps {
                echo 'Ejecutando tests unitarios...'
                // Levanta un contenedor efímero (--rm) solo para correr el test. 
                // Si el test falla, el contenedor se destruye y el pipeline aborta.
                sh 'docker run --rm ${APP_NAME}:latest python -m unittest test_app.py'
            }
        }
        stage('4. Despliegue en Producción') {
            steps {
                echo 'Desplegando la aplicación validada...'
                sh '''
                docker stop ${APP_NAME} || true
                docker rm ${APP_NAME} || true
                # Mapeamos el puerto 5000 de Flask al 8090 de tu Windows
                docker run -d -p 8090:5000 --name ${APP_NAME} ${APP_NAME}:latest
                '''
            }
        }
    }
    post {
        success {
            sh """
                curl -H "Content-Type: application/json" -X POST \
                -d '{"content": "✅ **ÉXITO**: Pruebas pasadas. Nueva versión de Python desplegada en el puerto 8090."}' \
                ${WEBHOOK_URL}
            """
        }
        failure {
            sh """
                curl -H "Content-Type: application/json" -X POST \
                -d '{"content": "🚨 **ALERTA CI**: El código no pasó las pruebas unitarias. Despliegue cancelado."}' \
                ${WEBHOOK_URL}
            """
        }
    }
}